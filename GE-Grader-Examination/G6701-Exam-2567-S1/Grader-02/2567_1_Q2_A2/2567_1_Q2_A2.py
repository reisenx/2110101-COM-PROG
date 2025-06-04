# Input data
C,n = input().strip().split()
C,n = float(C), int(n)

# Given A contains a sequence a0, a1, a2, ... of a finite simple continued fraction of C
A = []

# Loop n times
for i in range(n):
    # Separate integer part and decimal part of C
    # Example: 3.14159 = 3 + 0.14159
    integer = int(C)
    decimal = C - int(C)
    # Append integer part to list A
    A.append(integer)
    
    # If decimal part < 10^(-10), then end the process
    if(decimal < 10**(-10)):
        break
    # Change the value of C to 1/decimal
    C = 1/decimal

# Output all item in list A
# - Convert list A to string
# - Remove brackets by slicing a string
print(str(A)[1:-1])