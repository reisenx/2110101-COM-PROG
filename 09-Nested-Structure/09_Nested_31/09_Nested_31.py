# --------------------------------------------------
# File Name : 09_Nested_31.py
# Problem   : Pythagorean Triple
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Calculate the greatest common divisor (GCD) of two numbers
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Check if three numbers are coprime (their GCD is 1)
def is_coprime(a: int, b: int, c: int) -> bool:
    return gcd(gcd(a, b), c) == 1


# Generate all primitive Pythagorean triples with a, b, c <= max_len
# Three numbers a, b, c must satisfy a^2 + b^2 = c^2 and gcd(a, b, c) = 1
def primitive_Pythagorean_triples(max_len: int) -> list:
    triples = []
    for a in range(1, max_len + 1):
        for b in range(a + 1, max_len + 1):
            c = (a**2 + b**2) ** (0.5)
            if c <= max_len and c == int(c) and is_coprime(a, b, c):
                triples.append([int(c), a, b])
    triples.sort()

    sorted_triples = []
    for c, a, b in triples:
        sorted_triples.append([a, b, c])
    return sorted_triples


# Execute an input string
exec(input().strip())
