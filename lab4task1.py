import string
 
punctuations = [mark for mark in string.punctuation]
whitespaces = [char for char in string.whitespace]
 

def wordsp():
    y = open('words.txt', 'r')
    main = []
    for line in y:
        for item in line.split():
            main.append(item)
    return main
    y.close()
print(wordsp())  
 

def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuations) or (char in whitespaces)):
            pass
        else:
            cleansed += char.lower()
            print(char)      
    return cleansed
         
print ("The book has %s 'word'" ,([clean(word) for word in wordsp()]))
