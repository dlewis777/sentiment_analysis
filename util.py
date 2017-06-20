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

if __name__ == "__main__":
    import sys
    print(read_data(sys.argv[1]))
