<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Body Surface Area (Function) ★ (
      <a href="https://drive.google.com/file/d/1Y5w8Sg8FVCjdQD4DcAN8ckEvMk85V06Y/view?usp=drive_link">
        <code>01_Expr_07</code>
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
# File Name : 01_Expr_07.py
# Problem   : Body Surface Area (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math


# Calculate the body surface area using the Mosteller formula
def mosteller(w, h):
    return math.sqrt((w * h) / 3600)


# Calculate the body surface area using the Du Bois formula
def du_bois(w, h):
    return 0.007184 * (w**0.425) * (h**0.725)


# Calculate the body surface area using the Fujimoto formula
def fujimoto(w, h):
    return 0.008883 * (w**0.444) * (h**0.663)


# Main function to read input and display results
def main():
    # Read weight and height from input
    w = float(input())
    h = float(input())

    # Calculate body surface areas using different formulas
    mosteller_area = mosteller(w, h)
    du_bois_area = du_bois(w, h)
    fujimoto_area = fujimoto(w, h)

    # Print the results formatted to 2 decimal places
    print("Mosteller =", round(mosteller_area, 5))
    print("Du Bois =", round(du_bois_area, 5))
    print("Fujimoto =", round(fujimoto_area, 5))


# Execute the input string as code
exec(input())
```
