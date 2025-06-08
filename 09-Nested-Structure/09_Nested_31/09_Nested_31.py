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

# From a^2 + b^2 = c^2 we can know that c = (a^2 + b^2)^0.5
# To check if c is an integer, we can use c == int(c)
def primitive_Pythagorean_triples(max_len):
    temp = []
    triples = []
    for a in range(1, max_len+1):
        for b in range(1, max_len+1):
            c = (a**2 + b**2)**(0.5)
            # Conditions
            # 1.) c <= max_len
            # 2.) a^2 + b^2 = c^2 (c must be an integer)
            # 3.) a,b,c must be coprime
            if(c <= max_len and c == int(c) and is_coprime(a,b,c)):
                # Prevent cases when b < a
                a,b,c = sorted([a,b,int(c)])
                # Append in [c,a,b] format for sorting purpose
                if([c,a,b] not in temp):
                    temp.append([c,a,b])
    temp.sort()
    
    # Convert to [a,b,c] format
    for c,a,b in temp:
        triples.append([a,b,c])
    return triples

# Execute an input string
exec(input().strip())