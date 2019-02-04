import string

def vc(a_file, start_line=1):
    a = []
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]

    for char in lines:
        sl = char.strip().lower().translate(string.maketrans("",""), string.punctuation).split()
        a += sl
        print("words",'r')
        word_count_dict = {}
        for word in a:
          word_count_dict[word] = word_count_dict.get(word, 0) + 1

    g = len(a)
    h = len(word_count_dict.keys())
    v = float(h) / g

    print ("Total number of words: " + str(g) + "\n" + "Number of different words: " + str(h) + "\n" + "Vocab Variance Percent: " + str(v))
