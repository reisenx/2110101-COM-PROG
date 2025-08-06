<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cube Root (Function) ★★ (
      <a href="https://drive.google.com/file/d/1q4SQ2FI5yLt8RGI6L5eDOaKdKPIuf728/view?usp=drive_link">
        <code>01_Expr_08</code>
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
# File Name : 01_Expr_08.py
# Problem   : Cube Root (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


# Calculate the square root of a number n times
def sqrt_n_times(x, n):
    return x ** (1 / (2**n))


# Estimate the cube root of a number y using the sqrt_n_times function
def cube_root(y):
    s1 = sqrt_n_times(y, 2)
    s2 = s1 * sqrt_n_times(s1, 2)
    s3 = s2 * sqrt_n_times(s2, 4)
    s4 = s3 * sqrt_n_times(s3, 8)
    s5 = s4 * sqrt_n_times(s4, 16)
    ans = s5 * sqrt_n_times(s5, 32)
    return ans


# Main function to read input and print the cube root
def main():
    q = float(input())
    print(cube_root(q))


# Execute the input string as code
exec(input())
```
