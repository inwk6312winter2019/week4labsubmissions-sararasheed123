class corner():
     "rner"
c=corner()
c.x = 0
c.y = 0
class Rectangle():
        width = 100
        height = 200
box=Rectangle()
def find_center(rect):
                p1 = (c.x + rect.width)/2.0
                p2 = (c.y + rect.height)/2.0
                return (p1,p2)
"""Write   a   function   namedmove_rectanglethat   takes   a   Rectangle   and   two   numbersnameddxanddy.
 It should change the location of the rectangle by addingdxto thexcoordinateofcornerand addingdyto theycoordinate ofcorner"""
def move(self, dx, dy):
        self.c.x = self.c.x + dx
        self.c.y = self.c.y + dy
