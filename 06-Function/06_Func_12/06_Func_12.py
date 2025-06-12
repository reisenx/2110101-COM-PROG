# --------------------------------------------------
# File Name : 06_Func_12.py
# Problem   : Next Prime
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


# Find the next prime number after N
def next_prime(N):
    N += 1
    while not is_prime(N):
        N += 1
    return N


# Find the next twin prime pair after N
# Twin primes are pairs of prime numbers that differ by 2
def next_twin_prime(N):
    prime01 = next_prime(N)
    prime02 = next_prime(prime01)
    while prime02 - prime01 != 2:
        prime01 = prime02
        prime02 = next_prime(prime01)
    return prime01, prime02


# Execute a input string as code
exec(input().strip())
