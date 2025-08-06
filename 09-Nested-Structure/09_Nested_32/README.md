<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    First-Fit Best-Fit ★★★ (
      <a href="https://drive.google.com/file/d/1s9ueFIJNywIOl8C9mEoUoqBwR9Ai275I/view?usp=drive_link">
        <code>09_Nested_32</code>
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
# File Name : 09_Nested_32.py
# Problem   : First Fit Best Fit
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# First Fit: Place the number in the first list that its sum does not exceed 100.
#            Otherwise, create a new list.
def first_fit(numbers, num_to_insert):
    # Check if the number can fit into any existing list
    for i in range(len(numbers)):
        if sum(numbers[i]) + num_to_insert <= 100:
            numbers[i].append(num_to_insert)
            return numbers

    # Otherwise, create a new list for the number
    numbers.append([num_to_insert])
    return numbers


# Best Fit: Place the number in the list that has the least remaining value
#           after adding the number, but still does not exceed 100.
def best_fit(numbers, num_to_insert):
    # If there are no existing lists, create the first one
    if len(numbers) == 0:
        numbers.append([num_to_insert])
        return numbers

    # Calculate the remaining value in each list after adding the number
    diffs = [100] * len(numbers)
    for i in range(len(numbers)):
        if sum(numbers[i]) + num_to_insert <= 100:
            diffs[i] = 100 - (sum(numbers[i]) + num_to_insert)

    # Put the number in the list with the least remaining value
    min_diff = min(diffs)
    if min_diff < 100:
        index = diffs.index(min_diff)
        numbers[index].append(num_to_insert)

    # Otherwise, create a new list for the number
    else:
        numbers.append([num_to_insert])
    return numbers


# Partitioning numbers using First Fit algorithms
def partition_FF(numbers):
    result = []
    for num in numbers:
        result = first_fit(result, num)
    return result


# Partitioning numbers using Best Fit algorithms
def partition_BF(numbers):
    result = []
    for num in numbers:
        result = best_fit(result, num)
    return result


# Execute the input string as code
exec(input().strip())
```
