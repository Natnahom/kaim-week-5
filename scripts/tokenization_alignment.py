# from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer, TrainingArguments

def tokenize_and_align_labels(sentences, labels, tokenizer, label_map):
    """Tokenize sentences and align labels with tokens."""
    tokenized_inputs = tokenizer(sentences, truncation=True, padding=True, is_split_into_words=True)
    labels_aligned = []
    
    for i, label in enumerate(labels):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        label_ids = []
        for word_id in word_ids:
            if word_id is None:
                label_ids.append(-100)  # Special token
            else:
                label_ids.append(label_map[label[word_id]])  # Map label to ID
        labels_aligned.append(label_ids)

    tokenized_inputs["labels"] = labels_aligned
    return tokenized_inputs