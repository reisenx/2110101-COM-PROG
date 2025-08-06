<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Gray Codes ★★★ (
      <a href="https://drive.google.com/file/d/1wtcfvhjixQCCNLIbgYGeM6CuGrg597gz/view?usp=drive_link">
        <code>P3_01_Gray</code>
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
# File Name : P3_01_Gray.py
# Problem   : Part-III Gray Codes
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Check if n and k are valid integers
def is_valid(n, k):
    if n < 1 and k < 1:
        print("Invalid n and k")
        return False
    elif n < 1:
        print("Invalid n")
        return False
    elif k < 1:
        print("Invalid k")
        return False
    return True


# Print the number pattern based on n and k
def num_pattern(n, k):
    line = ""
    for num in range(1, k + 1):
        if num == k:
            line += f"{num}{(n - len(str(num))) * '-'}"
        else:
            line += f"{num}{(n - len(str(num)) + 1) * '-'}"
    print(line)


# Generate Gray codes for a given number of bits
def gray_codes(bits):
    # Initialize the list with the first two Gray codes
    half = 1
    codes = ["0", "1"]
    # Generate Gray codes
    for _ in range(bits - 1):
        # Append the reverse of the current codes
        codes += codes[::-1]
        half *= 2
        # Prefix '0' to the first half and '1' to the second half
        for i in range(half):
            codes[i] = "0" + codes[i]
            codes[half + i] = "1" + codes[half + i]
    return codes


# Input n and k
n = int(input())
k = int(input())

# Check if n and k are valid
if is_valid(n, k):
    # Print the number pattern
    num_pattern(n, k)
    # Generate and print Gray codes in groups of k
    codes = gray_codes(n)
    idx = 0
    while idx < len(codes):
        print(",".join(codes[idx : idx + k]))
        idx += k
```
