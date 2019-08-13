from Graph import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:  # for each word...
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:  # if bucket already exists
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # add vertices and edges for words in the same bucket
    for bucket in d.keys():  # same as for bucket in d?
        for word1 in d[bucket]:  # iterates thru each bucket twice
            for word2 in d[bucket]:
                if word1 != word2:  # make sure a word doesn't connect to itself
                    g.addEdge(word1,word2)
    print(d)  # FM, for understanding
    return g

def main(): 
    mygraph = buildGraph('input.txt')

    # FM, for understanding
    testdict = {'_ops': ['pops'], 'p_ps': ['pops'], 'po_s': ['pops'], 'pop_': ['pops', 'pope', 'popa'], '_ope': ['pope'], 'p_pe': ['pope'], 'po_e': ['pope', 'pose'], '_opa': ['popa'], 'p_pa': ['popa'], 'po_a': ['popa'], '_ose': ['pose'], 'p_se': ['pose'], 'pos_': ['pose']}    
    for bucket in testdict:
        # print(bucket)
        for word1 in testdict[bucket]: 
            print(word1, 1)
            for word2 in testdict[bucket]: 
                print(word2, 2)
                if word1 != word2: 
                    print(word1, word2)


if __name__ == '__main__':
    main()