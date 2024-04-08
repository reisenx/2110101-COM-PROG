n = int(input())
X = []
Y = []
distance = []
distance_sort = []
for i in range(n):
    x,y = input().split()
    X.append(float(x))
    Y.append(float(y))
    distance.append(((X[i]**2) + (Y[i]**2))**0.5)
distance_sort = sorted(distance)

index = distance.index(distance_sort[2])
print("#" + str(index+1) + ": " + "(" + str(X[index]) + ", " + str(Y[index]) + ")")