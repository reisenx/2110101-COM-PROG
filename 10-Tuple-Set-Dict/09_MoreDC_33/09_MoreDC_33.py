# Polynomial
# In this problem, we will rewrite polynomial as list with tuples
# Example: 4x^2 + 3x - 1 is [(4,2),(3,1),(-1,0)]

# Expand Polynomial
# Example: 
# expand_poly([(3,4),(-1,1)], 6)
# Returns [(0,6),(0,5),(3,4),(0,3),(0,2),(-1,1),(0,0)]
def expand_poly(polynomial, expand_degree):
    # Find unique degree from polynomial
    unique_degree = []
    for coefficient, degree in polynomial:
        unique_degree.append(degree)
    
    # Expand polynomial
    expand_poly = []
    index = 0
    for degree in range(expand_degree, -1, -1):
        if(degree in unique_degree):
            expand_poly.append(polynomial[index])
            index += 1
        else:
            expand_poly.append((0,degree))
    return expand_poly

# Shrink Polynomial
# Example: shrink_poly([(3,6),(0,5),(5,4),(0,3),(0,2),(0,1),(-1,0)])
# Returns [(3,6),(5,4),(-1,0)]
def shrink_poly(expand_poly):
    polynomial = []
    for monomial in expand_poly:
        if(monomial[0] != 0):
            polynomial.append(monomial)
    return polynomial

# Adding Polynomial
# Example: (3x^6 + 2x^4 + x - 1) + (3x^4 - x) = 3x^6 + 5x^4 - 1
# p1 = [(3,6),(2,4),(1,1),(-1,0)]
# p2 = [(3,4),(-1,1)]
# sum = [(3,6),(5,4),(-1,0)]

# == Algorithm ==
# 1.) Expand 'p1' and 'p2' list to 6th degree
# > p1 = [(3,6),(0,5),(2,4),(0,3),(0,2),(1,1),(-1,0)]
# > p2 = [(0,6),(0,5),(3,4),(0,3),(0,2),(-1,1),(0,0)]
# 2.) Add each tuple in 'p1' and 'p2' list
# > sum = [(3,6),(0,5),(5,4),(0,3),(0,2),(0,1),(-1,0)]
# 3.) Shrink 'sum' list
# > sum = [(3,6),(5,4),(-1,0)]
def add_poly(p1, p2):
    # 1.) Expand 'p1' and 'p2' list
    if(p1 == []):
        degree01 = 0
    else:
        degree01 = p1[0][1]
    if(p2 == []):
        degree02 = 0
    else:
        degree02 = p2[0][1]
    expand_degree = max(degree01, degree02)
    ex_p1 = expand_poly(p1, expand_degree)
    ex_p2 = expand_poly(p2, expand_degree)
    
    # 2.) Add each tuple in 'p1' and 'p2' list
    sum = []
    for i in range(len(ex_p1)):
        sum.append((ex_p1[i][0]+ex_p2[i][0], ex_p1[i][1]))
    
    # 3.) Shrink 'sum' list
    sum = shrink_poly(sum)
    return sum

# Multiplying Monomial with Polynomial
# Example: (3x^6)(x^4 - x^2) = 3x^10 - 3x^8

# == Algorithm ==
# Multiply coefficient and add degree of monomial to the polynomial
# > monomial = (3,6)
# > polynomial = [(1,4),(-1,2)]
# > product = [(1*3,4+6) (-1*3,2+6)]
# > product = [(3,10),(-3,8)]
def mult_mono2poly(monomial, polynomial):
    m_coefficient, m_degree = monomial
    product = []
    for p_coefficient, p_degree in polynomial:
        new_coefficient = m_coefficient * p_coefficient
        new_degree = m_degree + p_degree
        product.append((new_coefficient, new_degree))
    return product

# Multiplying Polynomial
# Example: (3x^6 + 2x^4)(x^4 - x^2) = 3x^10 - x^8 - 2x^6
# p1 =  [(3,6),(2,4)]
# p2 = [(1,4),(-1,2)]
# product = [(3,10),(-1,8),(-1,6)]

# == Concept ==
# (3x^6 + 2x^4)(x^4 - x^2) = (3x^6)(x^4 - x^2) + (2x^4)(x^4 - x^2)

# == Algorithm ==
# 1.) Set 'product' = []
# 2.) Multiply 1st monomial of 'p1' with 'p2' and add to product
# > mult_mono2poly((3,6), [(1,4),(-1,2)]) = [(3,10),(-3,8)]
# > product = add_poly(product, [(3,10),(-3,8)])
# > product = [(3,10),(-3,8)]
# 3.) Multiply 2nd monomial of 'p1' with 'p2'
# > mult_mono2poly((2,4), [(1,4),(-1,2)]) = [(2,8),(-2,6)]
# > product = add_poly(product, [(2,8),(-2,6)])
# > product = [(3,10),(-1,8),(-1,6)]
def mult_poly(p1,p2):
    product = []
    for monomial in p1:
        product = add_poly(product, mult_mono2poly(monomial, p2))
    return product

# Execute input string 3 times
for i in range(3):
    exec(input().strip())