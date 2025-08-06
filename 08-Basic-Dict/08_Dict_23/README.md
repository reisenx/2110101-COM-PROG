<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Telephone Dictionary ★★ (
      <a href="https://drive.google.com/file/d/1tFaiW-9R_dVhyP72g_SaPjIFcmkQfcXa/view?usp=drive_link">
        <code>08_Dict_23</code>
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
# File Name : 08_Dict_23.py
# Problem   : Telephone Directory
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the telephone directory
name_to_telephone = {}
telephone_to_name = {}

# Input the entries in the directory
n = int(input())
for _ in range(n):
    first_name, last_name, telephone = input().strip().split()
    name = f"{first_name} {last_name}"
    name_to_telephone[name] = telephone
    telephone_to_name[telephone] = name

# Search queries in the directory
n = int(input())
for _ in range(n):
    query = input().strip()
    if query in name_to_telephone:
        print(f"{query} --> {name_to_telephone[query]}")

    elif query in telephone_to_name:
        print(f"{query} --> {telephone_to_name[query]}")

    else:
        print(f"{query} --> Not found")
```
