import math
class Distance():
def __init__(self,point1,point2):
self.point1 = point1
self.point2 =point2
def dist(self):
x1,y1 = self.point1
x2,y2 = self.point2
delta_x = x1-x2
delta_y = y1-y2
dist = math.sqrt(delta_x**2+delta_y**2)
print("the distance b/w points = {}".format(dist)) 
distance = Distance((10,20),(20,30))
print(distance.point1)
print(distance.point2)
distance.dist
