# Input a number as a string
num = str(input())

# Create a list contains odd or even digits
odd_digit = ['1','3','5','7','9']
even_digit = ['0','2','4','6','8']

# Check if the number is positive, negative or zero
# If zero, the string must be exactly "0"
# If negative, the string must start with '-'
if(num == "0"):
    print("zero")
elif(num[0] == '-'):
    print("negative")
else:
    print("positive")

# Check if the number is even or odd by looking at the last digit
# A number ends with 0,2,4,6,8 must be even
# A number ends with 1,3,5,7,9 must be odd
if(num[-1] in even_digit):
    print("even")
elif(num[-1] in odd_digit):
    print("odd")