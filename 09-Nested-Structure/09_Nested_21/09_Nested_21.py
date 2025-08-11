# --------------------------------------------------
# File Name : 09_Nested_21.py
# Problem   : Factorization
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------


# Return the prime factorization of a number as a list.
def factor(number):
    factors = []
    # Find divisors starting from 2
    k = 2
    while k <= number:
        n = 0
        # Find how many times N divisible by k
        while number % k == 0:
            n += 1
            number //= k
        # If k is a factor, append it to the list
        if n > 0:
            factors.append([k, n])
        k += 1
    return factors


# Execute the input string as code
exec(input().strip())
