# --------------------------------------------------
# File Name : 09_Nested_21.py
# Problem   : Factorization
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Return the prime factorization of N as a list.
def factor(N: int) -> list:
    factors = []
    # Find divisors starting from 2
    k = 2
    while k <= N:
        n = 0
        # Find how many times N divisible by k
        while N % k == 0:
            n += 1
            N //= k
        # If k is a factor, append it to the list
        if n > 0:
            factors.append([k, n])
        k += 1
    return factors


# Execute the input string as code
exec(input().strip())
