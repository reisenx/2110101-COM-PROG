<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Odd Odd Functions ★★ (
      <a href="https://drive.google.com/file/d/1fysZG6sj3HcgmMIxE94B25Qk0fBw_b2x/view?usp=drive_link">
        <code>P2_01_Func1</code>
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
# File Name : P2_01_Func1.py
# Problem   : Part-II Odd Odd Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Check if a number is odd
def is_odd(number):
    return number % 2 == 1


# Check if there are any odd numbers in the data
def has_odds(numbers):
    for number in numbers:
        if is_odd(number):
            return True
    return False


# Check if all numbers in the data are odd
def all_odds(numbers):
    for number in numbers:
        if not is_odd(number):
            return False
    return True


# Check if there are no odd numbers in the data
def no_odds(numbers):
    return not has_odds(numbers)


# Get a list of all odd numbers from the data
def get_odds(numbers):
    result = []
    for number in numbers:
        if is_odd(number):
            result.append(number)
    return result


# Zip two lists of odd numbers together, alternating between the two lists
def zip_odds(a, b):
    # Get the odd numbers from both lists
    odds_a = get_odds(a)
    odds_b = get_odds(b)
    # Create a new list to hold the zipped result
    result = []
    # Zip the two lists of odd numbers together
    for idx in range(max(len(odds_a), len(odds_b))):
        if idx < len(odds_a):
            result.append(odds_a[idx])

        if idx < len(odds_b):
            result.append(odds_b[idx])
    # Return the zipped list of odd numbers
    return result


# Execute the input string as code
exec(input().strip())
```
