# Create a function make_int_list(x)
# This function can convert a string into a list of integers
# Example: "12 34 5" --> [12,34,5]
def make_int_list(x):
    x = [int(e) for e in x.split()]
    return x

# Create a function is_odd(e)
# This function can check if the number is an odd number
def is_odd(e):
    if(e%2 != 0):
        return True
    else:
        return False

# Create a function odd_list(alist)
# This function can return an input list but only with odd number
def odd_list(alist):
    odd = []
    for item in alist:
        if(is_odd(item) == True):
            odd.append(item)
    return odd

# Create a function sum_square(alist)
# This function can return a sum of square of number in a list
# Example: alist = [1, 3, 4]
# 1^2 + 3^2 + 4^2 = 26
# Return 26
def sum_square(alist):
    sum = 0
    for item in alist:
        sum += item**2
    return sum

# Execute a input string
exec(input().strip())