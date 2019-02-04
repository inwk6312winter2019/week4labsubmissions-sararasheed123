def duplicate(alllist):
    import os
    d=dict()
    for x in alllist:
        import string
        x=x.replace(' ','\ ')
        for i in "(){}[]&,';":
            x=x.replace(i,"\\"+i)
        f=os.popen('md5sum '+x)
        hashed=f.read()
        d[hashed[:32]]=d.get(hashed[:32],[])+[x]
        f.close()
        print (x)
    return d  
