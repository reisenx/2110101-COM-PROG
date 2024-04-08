def make_int_list(x):
    x = [int(e) for e in x.split()]
    return x

def is_odd(e):
    if(e%2 != 0):
        return True
    else:
        return False

def odd_list(alist):
    odd = []
    for item in alist:
        if(is_odd(item)):
            odd.append(item)
    return odd

def sum_square(alist):
    sum = 0
    for item in alist:
        sum += item**2
    return sum

exec(input().strip())