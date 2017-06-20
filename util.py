import numpy as np
import nltk

def read_data(filename):
    data = []
    with open(filename, encoding="ISO-8859-1") as f:
        for line in f:
            tokens = line.split()
            label = float(tokens[7])
            text = tokenize(' '.join(tokens[8:]))
            data.append((text, label))
    return data


def tokenize(text):
    return nltk.tokenize.casual.casual_tokenize(text)


def get_vocab(data):
    vocab = {}
    for instance in data:
        text = instance[0]
        for word in text:
            if word not in vocab:
                vocab[word] = len(vocab)
    return vocab


def get_features(data, vocab):
    feat_matrix = np.zeros((len(data), len(vocab)))
    for i, instance in enumerate(data):
        for word in instance[0]:
            if word in vocab:
                feat_matrix[i][vocab[word]] += 1
    return feat_matrix


def get_labels(data):
    labels = []
    for instance in data:
        labels.append(instance[1])
    return np.array(labels)


if __name__ == "__main__":
    import sys
    data = read_data(sys.argv[1])
    print(data)
    vocab = get_vocab(data)
    print(get_features(data, vocab))
    print(get_labels(data))
