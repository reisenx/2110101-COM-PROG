# Input a number of data lines
N = int(input())

# Create an empty list
X = []
Y = []
list_01 = []
list_02 = []

# Input a data, split them and put it into a list
for i in range(0,N):
    data = [int(e) for e in input().split()]
    X.append(data[0])
    Y.append(data[1])

# List 01: X0,Y1,X2,Y3,X4,Y5,... (Index starts at 0)
# List 02: Y0,X1,Y2,X3,Y4,X5,... (Index starts at 0)
for i in range(0,N):
    if(i%2 == 0):
        list_01.append(X[i])
        list_02.append(Y[i])
    elif(i%2 == 1):
        list_01.append(Y[i])
        list_02.append(X[i])

# Output
# Zig-Zag: Minimum of List 01 and Maximum of List 02
# Zag-Zig: Minimum of List 02 and Maximum of List 01
func = str(input())
if(func == "Zig-Zag"):
    print(min(list_01),max(list_02))
elif(func == "Zag-Zig"):
    print(min(list_02),max(list_01))