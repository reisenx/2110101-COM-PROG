# --------------------------------------------------
# File Name : 06_Func_12.py
# Problem   : Next Prime
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for k in range(2, int(number**0.5) + 1):
        if number % k == 0:
            return False
    return True


# Find the next prime number after N
def next_prime(number):
    number += 1
    while not is_prime(number):
        number += 1
    return number


# Find the next twin prime pair after N
# Twin primes are pairs of prime numbers that differ by 2
def next_twin_prime(number):
    prime01 = next_prime(number)
    prime02 = next_prime(prime01)
    while prime02 - prime01 != 2:
        prime01 = prime02
        prime02 = next_prime(prime01)
    return prime01, prime02


# Execute a input string as code
exec(input().strip())
