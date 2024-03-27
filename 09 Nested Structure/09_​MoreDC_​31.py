# Find GCD using Euclidean Algorithm
def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

# This function can check if a,b,c are coprime
# If gcd(a,b) = 1, we call a,b as coprime
# So if a,b,c are coprimes, then gcd(a,b,c) = 1
def is_coprime(a,b,c):
    if(gcd(gcd(a,b),c) == 1):
        return True
    else:
        return False

# Primitive Pythagorean triples is the set of (a,b,c) that satisfy these citeria
# 1.) a <= b <= c <= max_len
# 2.) a^2 + b^2 = c^2
# 3.) gcd(a,b,c) = 1
# If we loop a,b,c from 1 to max_len, it would cause a Runtime Exceed (T)
# So we need to find another algorithm

# Euclid's formula for generating Pythagorean triples
# Given integer m,n that 0 < n < m
# From (m^2)^2 + 2(m^2)(n^2) + (n^2)^2 = ((m^2)^2 - 2(m^2)(n^2) + (n^2)^2) + 4(m^2)(n^2)
#      (m^2 + n^2)^2 = (m^2 - n^2)^2 + (2mn)^2
# From the equation above, we can substitute a,b,c as
# 1.) c = m^2 + n^2
# 2.) b = 2mn
# 3.) a = m^2 - n^2
def primitive_Pythagorean_triples(max_len):
    # Create a list to contain Pythagorean triples
    temp = []
    triples = []
    # Set initial value m = 2
    m = 2
    a,b,c = 0,0,0
    # Loop until a,b,c is greater than max_len
    while(a <= max_len or b <= max_len or c <= max_len):
        # Loop n = 1,2,3,...,m-1 (0 < n < m)
        for n in range(1,m):
            c = (m**2) + (n**2)
            b = 2*m*n
            a = (m**2) - (n**2)
            
            # Check if a,b,c is greater than max_len
            if(a > max_len and b > max_len and c > max_len):
                break
            # Make sure than 0 <= a <= b <= c
            if(not (a <= b <= c)):
                a,b,c = sorted([a,b,c])
            # Check if the (a,b,c) is Primitive Pythagorean triple and c <= max_len
            if(is_coprime(a,b,c) and c <= max_len):
                # Append in [c,a,b] format for sorting purpose
                temp.append([c,a,b])
        # Increase m by 1 until a,b,c > max_len
        m += 1
    # Sorting by 'c'. If 'c' is equal, then sorting by 'a'
    temp.sort()
    # Rearrange from [c,a,b] format to [a,b,c] format
    for c,a,b in temp:
        triples.append([a,b,c])
    return triples

# Execute an input string
exec(input().strip())