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
        return "("+str(self.x)+","+str(self.y)+")"

class Rect:
    # __init__ method
    # Create 'Rect' object by given
    # - 'p1' is lower left 'Point' object of a reactangle
    # - 'p2' is upper right 'Point' object of a rectangle
    def __init__(self, p1, p2): 
        self.lowerleft = p1
        self.upperright = p2
    
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
    
    # contains method
    # This method can check if the Point object 'p' is in the rectangle or not
    def contains(self, p):
        # Assign the value to a variable
        p1 = self.lowerleft
        p2 = self.upperright
        a,b = p1.x, p1.y
        c,d = p2.x, p2.y
        x,y = p.x, p.y

        # Check if 'p' is in the rectangle or not
        if((a <= x <= c) and (b <= y <= d)):
            return True
        else:
            return False

# Input coordinates and Create 'Point' object
x1,y1,x2,y2 = [int(e) for e in input().split()] 
lowerleft = Point(x1,y1) 
upperright = Point(x2,y2) 

# Create 'Rect' object
rect = Rect(lowerleft, upperright) 

# Output the area of a rectangle
print(rect.area())

# Input number of points needed to check
m = int(input())

# Output True if the point is in the rectangle
# Output False if the point in not in the rectangle
for i in range(m): 
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p))