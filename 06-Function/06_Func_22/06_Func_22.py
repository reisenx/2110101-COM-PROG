# Create a function distance1(x1, y1, x2, y2)
# This function can return distance between (x1,y1) and (x2,y2) as a float
# Distance = sqrt((x1-x2)^2 - (y1-y2)^2)
def distance1(x1, y1, x2, y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distance

# Create a function distance2(p1, p2)
# This function can return distance between (x1,y1) and (x2,y2) as a float
# p1 is a list of [x1, y1] and p2 is a list of [x2,y2]
def distance2(p1, p2):
    return distance1(p1[0], p1[1], p2[0], p2[1])

# Create a function distance3(c1, c2)
# This function can return a distance between 2 center points and check if both circle are overlapping
# c1 is a list of [x1, y1, r1] and c2 is a list of [x2, y2, r2]
# "r" is a radius of a circle
# Both circle are overlapping when the sum of both radius 
# is greater than or equal to distance between 2 center points
def distance3(c1, c2):
    distance = distance1(c1[0], c1[1], c2[0], c2[1])
    if(c1[2] + c2[2] >= distance):
        return distance, True
    else:
        return distance, False

# Create a function perimeter(points)
# This function can return a perimeter of a polygon
# "points" is a list [[x1,y1], [x2,y2], [x3,y3], ...]
# To find a perimeter is to find a distance from (x1,y1) to (x2,y2)
# plus a distance from (x2,y2) to (x3,y3) plus a distance from (x3,y3) to (x4,y4) and so on
# and after that plus a distance from (xn,yn) to (x1,y1)
def perimeter(points):
    perimeter = 0
    for i in range(1,len(points)):
        perimeter += distance2(points[i-1], points[i])
    perimeter += distance2(points[-1], points[0])
    return perimeter

# Execute a input string
exec(input().strip())