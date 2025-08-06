<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Thai Numeral ★★☆ (
      <a href="https://drive.google.com/file/d/1iQh2TR-Gg74CZQyxdJxuCh-4yku5Fx1p/view?usp=drive_link">
        <code>P2_08_Thai</code>
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
# File Name : P2_08_Thai.py
# Problem   : Part-II Thai Numeral
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize the Thai numeral mapping
THAI = {
    0: "soon",
    1: "neung",
    2: "song",
    3: "sam",
    4: "si",
    5: "ha",
    6: "hok",
    7: "chet",
    8: "paet",
    9: "kao",
    10: "sip",
    100: "roi",
    1000: "pun",
}
THAI_EX = {1: "et", 2: "yi"}


# Function to convert an integer to Thai numeral representation
def to_Thai(number):
    # Initialize the result list
    result = []

    # Split into digits
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    # Read the thousands digit
    if thousands > 0:
        result.append(THAI[thousands])
        result.append(THAI[1000])

    # Read the hundreds digits
    if hundreds > 0:
        result.append(THAI[hundreds])
        result.append(THAI[100])

    # Read the tens digits
    if tens > 0:
        if tens == 2:
            result.append(THAI_EX[2])
        elif tens > 1:
            result.append(THAI[tens])
        result.append(THAI[10])

    # Read the ones digits
    if ones > 0:
        if ones == 1 and (tens > 0 or hundreds > 0 or thousands > 0):
            result.append(THAI_EX[1])
        else:
            result.append(THAI[ones])
    if number == 0:
        return THAI[0]

    # Return the result as a string
    return " ".join(result)


# Execute an input string as code
exec(input().strip())
```
