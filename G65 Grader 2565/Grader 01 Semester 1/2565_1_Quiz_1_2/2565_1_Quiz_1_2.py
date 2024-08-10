# Not guarantee 100/100 points on this code

# 'f1' function returns minimum value of a,b,c (Consider only positive number)
def f1(a,b,c):
    # Find a positive number in a,b,c and put it in the list
    positive = []
    if(a > 0):
        positive.append(a)
    if(b > 0):
        positive.append(b)
    if(c > 0):
        positive.append(c)
    # Return a minimum value among positive numbers
    return min(positive)

# 'f2' function returns maximum value of a,b,c (Consider only negative number)
def f2(a,b,c):
    # Find a negative number in a,b,c and put it in the list
    negative = []
    if(a < 0):
        negative.append(a)
    if(b < 0):
        negative.append(b)
    if(c < 0):
        negative.append(c)
    # Return a maximum value among negative numbers
    return max(negative)

# 'f3' function returns the leftmost digit of a+b+c (Ignore negative symbol)
def f3(a,b,c):
    # Find sum then remove negative symbol using absolute
    sum = abs(a+b+c)
    # Convert a sum into a string a return the leftmost digit
    return str(sum)[0]

# 'f4' function returns the rightmost digit of a+b+c (Ignore negative symbol)
def f4(a,b,c):
    # Find sum then remove negative symbol using absolute
    sum = abs(a+b+c)
    # Convert a sum into a string a return the rightmost digit
    return str(sum)[-1]

# Get s1,s2,a,b,c value from keyboard
# - If s1=0, s2=0, print(f1(a,b,c))
# - If s1=0, s2=1, print(f2(a,b,c))
# - If s1=1, s2=0, print(f3(a,b,c))
# - If s1=1, s2=1, print(f4(a,b,c))
# - If s1 or s2 is not 0 or 1, print("Error")
def main():
    s1,s2,a,b,c = [int(e) for e in input().split()]
    if(s1 == 0 and s2 == 0):
        print(f1(a,b,c))
    elif(s1 == 0 and s2 == 1):
        print(f2(a,b,c))
    elif(s1 == 1 and s2 == 0):
        print(f3(a,b,c))
    elif(s1 == 1 and s2 == 1):
        print(f4(a,b,c))
    else:
        print("Error")

# Execute an input string
exec(input().strip())