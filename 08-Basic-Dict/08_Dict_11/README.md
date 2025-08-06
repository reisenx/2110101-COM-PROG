<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Reverse and Keys ★ (
      <a href="https://drive.google.com/file/d/1PLGqq5Xqw2fbWuMnsbC-t3AlIUYLRCoT/view?usp=drive_link">
        <code>08_Dict_11</code>
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
# File Name : 08_Dict_11.py
# Problem   : Reverse and Keys
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Reverses the keys and values of a dictionary
def reverse(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[value] = key
    return new_dict


# Returns a list of keys that have the specified value in the dictionary
def keys(input_dict, v):
    keys = []
    for key, value in input_dict.items():
        if value == v:
            keys.append(key)
    return keys


# Execute the input string
exec(input().strip())
```
