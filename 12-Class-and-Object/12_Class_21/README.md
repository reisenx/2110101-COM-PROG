<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Complex Number ★★ (
      <a href="https://drive.google.com/file/d/1c-t7FxeJv0xwvdwCdvixSNVJomTEBM_f/view?usp=drive_link">
        <code>12_Class_21</code>
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
# File Name : 12_Class_21.py
# Problem   : Complex Number
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


class Complex:
    # __init__ method
    # Initialize the complex number object
    # a is real part and b is imaginary part
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

    # __str__ method
    # Convert the complex object to a string representation
    def __str__(self):
        # Initialize variables
        a, b = self.real, self.imaginary
        complex_str = ""
        # Format the complex number
        if a == 0 and b == 0:
            return "0"

        if a != 0:
            complex_str += str(a)

        if b != 0:
            if b > 0 and a != 0:
                complex_str += "+"
            if abs(b) != 1:
                complex_str += str(b)
            elif b == -1:
                complex_str += "-"
            complex_str += "i"
        return complex_str

    # __add__ method
    # Calculate the sum of 2 complex numbers
    # 'self' is a+bi and 'rhs' is c+di
    def __add__(self, rhs):
        # Initialize variables
        a, b = self.real, self.imaginary
        c, d = rhs.real, rhs.imaginary
        # Return the sum of complex numbers
        return Complex(a + c, b + d)

    # __mul__ method
    # Calculate the product of 2 complex numbers
    # 'self' is a+bi and 'rhs' is c+di
    def __mul__(self, rhs):
        # Initialize variables
        a, b = self.real, self.imaginary
        c, d = rhs.real, rhs.imaginary
        # Return the product of complex numbers
        real = (a * c) - (b * d)
        imaginary = (a * d) + (b * c)
        return Complex(real, imaginary)

    # __truediv__ method
    # Calculate the quotient of 2 complex numbers
    # 'self' is a+bi and 'rhs' is c+di
    def __truediv__(self, rhs):
        # Initialize variables
        a, b = self.real, self.imaginary
        c, d = rhs.real, rhs.imaginary
        # Return the quotient of complex numbers
        real = ((a * c) + (b * d)) / (c**2 + d**2)
        imaginary = (-(a * d) + (b * c)) / (c**2 + d**2)
        return Complex(real, imaginary)


# Input
t, a, b, c, d = [int(x) for x in input().split()]

# Initialize complex numbers
c1 = Complex(a, b)
c2 = Complex(c, d)

# Output
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1 + c2)
elif t == 4:
    print(c1 * c2)
else:
    print(c1 / c2)
```
