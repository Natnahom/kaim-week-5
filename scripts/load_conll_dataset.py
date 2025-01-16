
def load_conll_dataset(file_path):
    sentences = []
    labels = []
    current_sentence = []
    current_labels = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                token, label = line.split()
                current_sentence.append(token)
                current_labels.append(label)
            else:
                if current_sentence:
                    sentences.append(current_sentence)
                    labels.append(current_labels)
                    current_sentence = []
                    current_labels = []

    return sentences, labels

# sentences, labels = load_conll_dataset('labeled_data.conll')