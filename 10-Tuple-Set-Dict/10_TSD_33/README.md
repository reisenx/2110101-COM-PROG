<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Polynomial ★★★ (
      <a href="https://drive.google.com/file/d/1NzHodyfvlrIU49Ooqf5xPqe2ys6ujKb7/view?usp=drive_link">
        <code>10_TSD_33</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_33.py
# Problem   : Polynomial
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


def add_poly(polynomial_01, polynomial_02):
    # Initialize variables to hold the result of the addition
    result_dict = {}
    result = []

    # Add terms from the first polynomial
    for coefficient, exponent in polynomial_01:
        result_dict[exponent] = coefficient

    # Add terms from the second polynomial
    for coefficient, exponent in polynomial_02:
        if exponent not in result_dict:
            result_dict[exponent] = 0
        result_dict[exponent] += coefficient

    # Convert the dictionary back to a sorted list of tuples
    # Sort the terms by exponent in descending order
    for exponent, coefficient in sorted(result_dict.items())[::-1]:
        if coefficient != 0:
            result.append((coefficient, exponent))

    # Return the result polynomial
    return result


# Multiplies two polynomials represented as lists of tuples.
def mult_poly(polynomial_01, polynomial_02):
    total_result = []

    # Expand each term in the first polynomial with every term in the second polynomial.
    for coefficient01, exponent01 in polynomial_01:
        result = []
        for coefficient02, exponent02 in polynomial_02:
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
```
