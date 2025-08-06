<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Pythagorean Triple ★★★ (
      <a href="https://drive.google.com/file/d/1SNN6xz6-R4IevIL8uLU9GexVMoLptVhb/view?usp=drive_link">
        <code>09_Nested_31</code>
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
# File Name : 09_Nested_31.py
# Problem   : Pythagorean Triple
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Check if three numbers are coprime (their GCD is 1)
def is_coprime(a, b, c):
    return gcd(gcd(a, b), c) == 1


# Generate all primitive Pythagorean triples with a, b, c <= max_len
# Three numbers a, b, c must satisfy a^2 + b^2 = c^2 and gcd(a, b, c) = 1
def primitive_Pythagorean_triples(max_len):
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
```
