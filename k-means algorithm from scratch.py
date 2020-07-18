from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)


    def __repr__(self):
         return "Point(%d, %d)" % (self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if isinstance(other, int):
            return (other*self.x, other*self.y)
        elif isinstance(other, Point):
            return self.x*other.x + self.y*other.y
        
    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __truediv__(self,other):
        return Point(self.x/other, self.y/other)



class Cluster(object):
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []

    def update(self):
        a=sum(p.x for p in self.points)/len(self.points)
        b=sum(p.y for p in self.points)/len(self.points)
        self.center = Point(a,b)        
           
    def add_point(self, point):
        self.points.append(point)



def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        a = Cluster(a.center.x,a.center.y)
        b = Cluster(b.center.x,b.center.y)  
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
            else:
                b.add_point(point)
                
        if a_old == a.points:
            break
        a_old = a.points
        
        a.update()
        b.update()
    return [(a.center.x, a.center.y), (b.center.x, b.center.y)]

