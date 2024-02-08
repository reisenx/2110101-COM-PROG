# Input integer n
n = int(input())

# Input coordinates (x,y)
# Calculate a distance between (0,0) to (x,y)
# Distance = sqrt(x^2 + y^2)
X = []
Y = []
distance = []
distance_sort = []
for i in range(0,n):
    data = input().split()
    X.append(float(data[0]))
    Y.append(float(data[1]))
    distance.append(((X[i]**2) + (Y[i]**2))**0.5)
    distance_sort.append(((X[i]**2) + (Y[i]**2))**0.5)

# Sorting a distance
distance_sort.sort()

# Output coordinate (x,y) of the 3rd longest distance from (0,0)
index = distance.index(distance_sort[2])
print("#" + str(index+1) + ": " + "(" + str(X[index]) + ", " + str(Y[index]) + ")")