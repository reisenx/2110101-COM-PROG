# This function can factorize the number N
# Given N = (p1^n1)*(p2^n2)*...(pk^nk) --> factor(N) = [[p1,n1],[p2,n2],...,[pk,nk]]
# Example: 200 = (2^3)*(5^2) --> factor(200) = [[2,3],[5,2]]

# Algorithm
# 1.) Given initial 'p' = 2 and increase 'p' by 1 until remain is less than 'p'
# 2.) If 'remain' is divisible by 'p' then loop remain = remain/p and increase n by 1 every loop
#     until it is not divisible then append [p,n] into a 'factor_list'

# Example: factor(200)
# Loop p = 2 (200%2 == 0)
# > remain = 200/2 --> 100/2 --> 50/2 = 25 and n = 3 --> append([2,3])
# Loop p = 3 (25%3 != 0)
# Loop p = 4 (25%4 != 0)
# Loop p = 5 (25%5 == 0):
# > remain = 25/5 = 5/5 = 1 and n = 2 --> append([5,2])
# The loop breaks because remain < p (1 < 6)
def factor(N):
    factor_list = []
    p = 2
    remain = N
    while(remain >= p):
        n = 0
        while(remain%p == 0):
            remain = remain / p
            n += 1
        if(n > 0):
            factor_list.append([p,n])
        p += 1
    return factor_list

# Execute an input string
exec(input().strip())