import os
def walk_through(mydir123):
    for root, dirs, files in os.walk(mydir123):
        for name in files:
            print (os.path.join(root, mydir123))
        for name in dirs:
            print (os.path.join(root, mydir123))

