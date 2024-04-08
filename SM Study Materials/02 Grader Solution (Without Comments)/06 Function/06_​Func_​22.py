def distance1(x1, y1, x2, y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distance

def distance2(p1, p2):
    return distance1(p1[0], p1[1], p2[0], p2[1])

def distance3(c1, c2):
    distance = distance1(c1[0], c1[1], c2[0], c2[1])
    if(c1[2] + c2[2] >= distance):
        return distance, True
    else:
        return distance, False

def perimeter(points):
    perimeter = 0
    for i in range(1,len(points)):
        perimeter += distance2(points[i-1], points[i])
    perimeter += distance2(points[-1], points[0])
    return perimeter

exec(input().strip())