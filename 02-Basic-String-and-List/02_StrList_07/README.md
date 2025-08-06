<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Decryption ★★★ (
      <a href="https://drive.google.com/file/d/1ZdCtGOkCj1veisQGNKhYomIU7aK2A6lT/view?usp=drive_link">
        <code>02_StrList_07</code>
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
# File Name : 02_StrList_07.py
# Problem   : Decryption
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input a string of numbers
num = input().strip()

# Step 1: Concatenate the numbers at indices 3, 10, 17, 24, and 31
#         and convert them to an integer.
step1 = int(num[3::7])

# Step 2: Concatenate the numbers at indices 7, 12, 17, 22, and 27
#         and convert them to an integer.
step2 = int(num[7::5])

# Step 3: Add the results from Step 1 and Step 2, then add 10000
#         and convert the result to a string.
step3 = str(step1 + step2 + 10000)

# Step 4: Take the middle three digits from the result of Step 3
step4 = step3[-4:-1]

# Step 5: Calculate the sum of the digits in Step 4,
#         choose the last digit, and add 1.
step5 = int(step4[0]) + int(step4[1]) + int(step4[2])
step5 = (step5 % 10) + 1

# Step 6: Use the result from Step 5 to select a letter from the alphabet
ALPHABET = "ABCDEFGHIJ"
step6 = ALPHABET[step5 - 1]

# Step 7: Output the final result by concatenating Step 4 and Step 6
print(f"{step4}{step6}")
```
