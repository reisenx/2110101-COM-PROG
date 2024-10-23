# Input data
C,n = input().strip().split()
C,n = float(C), int(n)

# Given A contains a sequence a0, a1, a2, ... of a finite simple continued fraction of C
A = []

# Loop n times
for i in range(n):
    # Separate integer part and decimal part of C
    # Example: 3.14159 = 3 + 0.14159
    intPart = int(C)
    decPart = C - int(C)
    # Append integer part to list A
    A.append(intPart)
    
    # If decimal part < 10^(-10), then end the process
    if(decPart < 10**(-10)):
        break
    # Change the value of C to 1/decPart
    C = 1/decPart

# Output all item in list A
# To use join() function, we need to convert all item in list from int to str
A = [str(item) for item in A]
print(", ".join(A))