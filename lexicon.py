import sys
import scipy.stats
def read_lexicon(filename):

    ldict = {}
    with open(filename,'r') as lexicon:
        for line in lexicon:
            ldict[line.split()[0]] = line.split()[2]
 
    sdict = {}
    with open(filename,'r') as lexicon:
        for line in lexicon:
            if line.split()[1] == "positive":
                sdict[line.split()[0]] = 1
            else:
                sdict[line.split()[0]] = 0
    return ldict, sdict

def read_file(filename):

    examples = {}
    
    with open(filename,'r') as data:
        
        for line in data:
            examples[tuple(map(lambda x: x.lower(), line.split()[8:]))] = line.split()[7]

    return examples

def get_counts(data, lex):

    x = []
    y = []
    
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
        print score, true
        data[example] = (score,true)
        x.append(score)
        y.append(float(true))
        
    return x,y
if __name__ == "__main__":

    lex1, lex2 = read_lexicon(sys.argv[1])
    data = read_file(sys.argv[2])
    x1,y1 = get_counts(data,lex1)
    x2,y2 = get_counts(data,lex2)
    
    #for example in data:
    #    print data[example]

    print scipy.stats.pearsonr(x2,y2)
    print scipy.stats.pearsonr(x2,y2)
