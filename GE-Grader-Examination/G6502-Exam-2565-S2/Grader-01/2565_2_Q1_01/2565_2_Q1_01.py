# rotate_left function
# Example: rotate_left("01234",3)
# "01234" --> "012" + "34" --> "34" + "012" --> "34012"
def rotate_left(s,n):
    return s[n:] + s[:n]

# rotate_right function
# Example: rotate_right("01234",3)
# rotate_right("01234",3) is similar to rotate_left("01234",2)
# So rotate_right(s,n) is rotate_left(s, len(s) - n)
def rotate_right(s,n):
    return rotate_left(s, len(s) - n)

# str_mod function
# Loop each character and modulo with n
def str_mod(s,n):
    result = ""
    for num in s:
        result += str(num % n)
    return result

def main():
    # Input string s
    s = input().strip()
    
    # Check a digit before the last digit
    if(s[-2] == '1'):
        print(rotate_left(s, int(s[-1])))
    elif(s[-2] == '2'):
        print(rotate_right(s, int(s[-1])))
    elif(s[-2] == '3'):
        print(str_mod(s, int(s[-1])))
    else:
        print(s)

