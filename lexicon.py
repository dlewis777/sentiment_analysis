import sys
import scipy.stats
def read_lexicon(filename):

    ldict = {}
    with open(filename,'r') as lexicon:
        for line in lexicon:
            ldict[line.split()[0]] = line.split()[2]

    return ldict

def read_file(filename):

    examples = {}
    
    with open(filename,'r') as data:
        
        for line in data:
            examples[tuple(map(lambda x: x.lower(), line.split()[8:]))] = line.split()[7]

    return examples

def get_counts(data, lex):

    x = []
    y = []
    num = 0
    for example in data:

        counter = 0.
        score = 0
        true = data[example]
        for word in example:
            if word in lex:
                counter += 1
                #print "score:" , lex[word]
                score += float(lex[word])
        #print example        
        score = score / float(counter)
        print "avg score:" , score , true
        score = round((score * 2) + 3)
        data[example] = (score,true)
        x.append(score)
        y.append(float(true))
        num += 1
        print num
    return x,y
if __name__ == "__main__":

    lex = read_lexicon(sys.argv[1])
    data = read_file(sys.argv[2])
    x,y = get_counts(data,lex)
    
    
    #for example in data:
    #    print data[example]

    print scipy.stats.pearsonr(x,y)
