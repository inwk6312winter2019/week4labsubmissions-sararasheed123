def totalfiles(dirf):
    import os 
    alllist=[]
    for x,y,z in os.walk(dirf):
        if len(z)>0:
            for i in z:
                if i[-1]=='3':
                    alllist.append(x+'/'+i)
    return alllist
print(totalfiles(""))  
