import pandas as pd
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer, TrainingArguments
from transformers import DataCollatorForTokenClassification
import numpy as np
from sklearn.metrics import classification_report
from scripts.tokenization_alignment import *
from scripts.load_conll_dataset import *

def set_training_arguments():
    """Set up and return training arguments."""
    return TrainingArguments(
        output_dir='./results',
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,  # Reduced batch size
        per_device_eval_batch_size=8,
        num_train_epochs=2,  # Reduced number of epochs
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,  # Enable logging
    )

def fine_tune_model(train_dataset, eval_dataset, model, tokenizer):
    """Fine-tune the NER model using the Trainer API."""
    data_collator = DataCollatorForTokenClassification(tokenizer)

    trainer = Trainer(
        model=model,
        args=set_training_arguments(),
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )

    trainer.train()
    return trainer

def evaluate_model(trainer):
    """Evaluate the fine-tuned model."""
    return trainer.evaluate()

def save_model(trainer, model_dir, tokenizer):
    """Save the fine-tuned model and tokenizer."""
    trainer.save_model(model_dir)
    tokenizer.save_pretrained(model_dir)

def execute_codes():
    # Load the labeled dataset
    sentences, labels = load_conll_dataset('labeled_data.conll')

    # Define label mapping before loading the model
    label_set = set(label for label_list in labels for label in label_list)
    label_map = {label: i for i, label in enumerate(label_set)}

    # Load the tokenizer and model
    model_name = "xlm-roberta-base"  # Change to "bert-tiny-amharic" or "afroxmlr" as needed
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=len(label_set))

    # Tokenize and align labels
    tokenized_dataset = tokenize_and_align_labels(sentences, labels, tokenizer, label_map)

    # Fine-tune the model
    trainer = fine_tune_model(tokenized_dataset['train'], tokenized_dataset['validation'], model, tokenizer)

    # Evaluate the model
    eval_results = evaluate_model(trainer)
    print(eval_results)

    # Save the fine-tuned model and tokenizer
    save_model(trainer, tokenizer, "fine_tuned_ner_model")

# if __name__ == "__main__":
#     main()