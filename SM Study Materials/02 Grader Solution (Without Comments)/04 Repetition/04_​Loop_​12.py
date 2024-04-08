N = int(input())
X = []
Y = []
list_01 = []
list_02 = []

for i in range(0,N):
    data = [int(e) for e in input().split()]
    X.append(data[0])
    Y.append(data[1])

for i in range(0,N):
    if(i%2 == 0):
        list_01.append(X[i])
        list_02.append(Y[i])
    elif(i%2 == 1):
        list_01.append(Y[i])
        list_02.append(X[i])

func = str(input())
if(func == "Zig-Zag"):
    print(min(list_01),max(list_02))
elif(func == "Zag-Zig"):
    print(min(list_02),max(list_01))