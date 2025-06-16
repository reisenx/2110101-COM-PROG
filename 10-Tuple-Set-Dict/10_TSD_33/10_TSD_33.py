# --------------------------------------------------
# File Name : 10_TSD_33.py
# Problem   : Polynomial
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


def add_poly(p1: list, p2: list) -> list:
    # Initialize variables to hold the result of the addition
    result_dict = {}
    result = []

    # Add terms from the first polynomial
    for coefficient, exponent in p1:
        result_dict[exponent] = coefficient
    # Add terms from the second polynomial
    for coefficient, exponent in p2:
        if exponent in result_dict:
            result_dict[exponent] += coefficient
        else:
            result_dict[exponent] = coefficient

    # Convert the dictionary back to a sorted list of tuples
    # Sort the terms by exponent in descending order
    for exponent, coefficient in sorted(result_dict.items())[::-1]:
        if coefficient != 0:
            result.append((coefficient, exponent))
    # Return the result polynomial
    return result


# Multiplies two polynomials represented as lists of tuples.
def mult_poly(p1: list, p2: list) -> list:
    total_result = []
    # Expand each term in the first polynomial with every term in the second polynomial.
    for coefficient01, exponent01 in p1:
        result = []
        for coefficient02, exponent02 in p2:
            # Multiply coefficients and add exponents
            new_coefficient = coefficient01 * coefficient02
            new_exponent = exponent01 + exponent02
            # Append the new term to the result
            result.append((new_coefficient, new_exponent))
        # Add the result of this multiplication to the total result
        total_result = add_poly(total_result, result)
    # Return the final polynomial after all multiplications
    return total_result


for _ in range(3):
    exec(input().strip())
