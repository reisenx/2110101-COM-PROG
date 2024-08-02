class Point: 
    # __init__ method
    # Create 'Point' object that contains coordinate (x,y)
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    
    # __str__ method
    # Convert 'Point' object to a string
    # Example: Point(5,2) --> "(5,2)"
    def __str__(self): 
        return "("+str(self.x) + "," + str(self.y) + ")"

class Rect:
    # __init__ method
    # Create 'Rect' object by given
    # - 'p1' is lower left 'Point' object of a reactangle
    # - 'p2' is upper right 'Point' object of a rectangle
    def __init__(self, p1, p2): 
        self.lowerleft = p1
        self.upperright = p2
    
    # __str__ method
    # Convert 'Rect' object to a string
    # Rect(Point(x1,y1), Point(x2,y2)) --> "(x1,y1)-(x2,y2)"
    def __str__(self): 
        return str(self.lowerleft) + "-" + str(self.upperright)
    
    # == Shape of a rectangle ==
    # Given the coordinate of 'p1' is (a,b) and 'p2' is (c,d)
    #         _______________ p2(c,d)
    #        |               |
    #        |               |
    #        |               |
    #        |_______________|
    # p1(a,b)

    # area method
    # This method can calculate the rectangle area
    # Given that all reactangle sides are parallel to x-axis and y-axis
    def area(self):
        # Assign the value to a variable
        p1 = self.lowerleft
        p2 = self.upperright
        a,b = p1.x, p1.y
        c,d = p2.x, p2.y

        # Calulate and return the area
        area = (c-a) * (d-b)
        return area
    
    # __lt__ method
    # This method can compare area of 2 'Rect' object
    def __lt__(self,other):
        area01 = self.area()
        area02 = other.area()
        return area01 < area02

# Input number of rectangle
n = int(input()) 

# Input coordinates of lowerleft and upperright point of each rectangle
# Create 'Rect' object and put it in the list 'rects'
rects = [] 
for i in range(n): 
    x1,y1,x2,y2 = [int(e) for e in input().split()]
    rects.append(Rect(Point(x1,y1), Point(x2,y2)))

# Sorting 'Rect' object by its area
rects.sort()

# Output
for i in range(n): 
    print(rects[i])