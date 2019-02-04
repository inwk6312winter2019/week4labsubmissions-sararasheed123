import string

def fre(readfile, s_line=1):
    a = []
    fin = open("words.txt",'r')
    lines = fin.readlines()
    lines = lines[s_line - 1:]

    for line in lines:
        stripped_line = line.strip().lower().translate(string.maketrans("",""), string.punctuation).split()
        a += stripped_line

    wordcount = {}
    for word in a:
        wordcount[word] = wordcount.get(word, 0) + 1

    sortedcount = sorted([(v, k) for k, v in wordcount.iteritems()], reverse=True)
    t = sortedcount[:20]

    for item, word in t:
        print( word + " : " + str(item))
