from string import punctuation, whitespace

origin = 'origin.txt' 


wordf = 'words.txt'
books = [origin]

def w(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def c(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        elif not char.isalpha():
            pass
        else:
            result += char.lower()
    return result

def stats():
    for b in books:
        book_words = set([c(word) for word in w(open(b, 'r'))])
        words_ = set([word for word in open(wordf, 'r')])
        print ("Stats for %s" % open(b, 'r').name)
        print ("  There are %s non-listed words." % len(book_words - words_))
        
stats()



