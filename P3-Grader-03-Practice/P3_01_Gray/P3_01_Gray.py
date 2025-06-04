import math

# Check if n,k is valid (n < 1 and k < 1) or not
# If not valid, output a string then return False
# If valid, return True
def check_valid(n,k):
    if(n < 1 and k < 1):
        print("Invalid n and k")
        return False
    elif(n < 1):
        print("Invalid n")
        return False
    elif(k < 1):
        print("Invalid k")
        return False
    else:
        return True

# This function can output a string in the first line of the output
# Example: num_pattern(5,11) = "1-----2-----3-----4-----5-----6-----7-----8-----9-----10----11---"
def num_pattern(n,k):
    line = ""
    for num in range(1,k+1):
        if(num == k):
            line += str(num) + (n - len(str(num)))*"-"
        else:
            line += str(num) + ((n+1) - len(str(num)))*"-"
    print(line)

# This function can return all n-bit gray code as a list
# Gray code is the code in the pattern
# 1-Bit Code: ['0','1']
# 2-Bit Code: ['0','1','1','0'] --> ['00','01','11','10']
# 3-Bit Code: ['00','01','11','10','10','11','01','00'] --> ['000','001','011','010','110','111','101','100']
# and so on...
def gray_codes(n):
    # Setup initial code as 1-Bit Code
    codes = ['0','1']
    for i in range(1,n):
        # Reconstruct the code list by adding revesed list at the end
        # Example: ['0','1'] --> ['0','1','1','0']
        codes = codes + codes[::-1]
        # Add '0' at the first half of a list
        for j in range(0, len(codes)//2):
            codes[j] = '0' + codes[j]
        # Add '1' at the second half of a list
        for j in range(len(codes)//2, len(codes)):
            codes[j] = '1' + codes[j]
    # Returns as a list of n-bits gray codes
    return codes

# Input n and k
n = int(input())
k = int(input())

# Check if n,k is valid
if(check_valid(n,k)):
    # Output the first line
    num_pattern(n,k)
    # Output Gray codes k number in each line
    codes = gray_codes(n)
    nrows = math.ceil(len(codes)/k)
    start = 0
    end = k
    for i in range(nrows):
        print(",".join(codes[start:end]))
        start += k
        end += k