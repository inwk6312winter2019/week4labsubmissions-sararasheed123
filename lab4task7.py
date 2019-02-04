import os

def s(a, b, fin, fout):
    
    x = open(fin)

    
    y = open(fout, 'w+')

    
    for line in x:
        if a in line:
            print ('pattern found')
            
            
            newLine = line.replace(a,b)
            y.write(newLine)
        else:
            y.write(line)

if __name__ == '__main__':
    print (os.getcwd())
    a = 'oy'
    b = 'it'
    fin = ("/home/matt/projects/Skools_Kool/Chapter_14/Exercise2_Test.txt")
    fout = ("/home/matt/projects/Skools_Kool/Chapter_14/Exercise2_Out.txt")
    s(a, b, fin, fout)
