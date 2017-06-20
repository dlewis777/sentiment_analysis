import scikit-learn
import nltk
import sys

def read_lexicon(filename):

    ldict = []
    with open(filename,'r') as lexicon:
        for line in lexicon:
            ldict[line.split()[0]] = line.split()[2]

    return ldict

def read_file(filename):

    examples = []
    
    with open(filename,'r') as data:
        
        for line in data:
            examples[line.split()[8:]] = line.split()[7]

    return examples

def get_counts(data, lex):

    for example in data:
        score = 0
        true = data[example]
        for word in example:
            if word in lex:
                score += lex[word]
        score = score / len(example)
        score = round((score * 2) + 3)
        data[example] = (score,true)

if __name__ == __main__:

    lex = read_lexicon(sys.argv[1])
    data = read_file(sys.argv[2])
    get_counts(data,lex)
    
    for example in data:
        print data[example]

