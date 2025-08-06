<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Student Info ★★★ (
      <a href="https://drive.google.com/file/d/15menRq_5rcVxJTHJ2-CBhOH0zxlM_o3W/view?usp=drive_link">
        <code>10_TSD_35</code>
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
# File Name : 10_TSD_35.py
# Problem   : Student Info
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of groups and departments
GROUPS = (
    "A",
    "B",
    "C",
    "Dog",
    "E",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
)
DEPARTMENTS = (
    "CE",
    "EE",
    "ME",
    "AE",
    "IE",
    "CHE",
    "PE",
    "GE",
    "ENV",
    "SV",
    "MT",
    "CP",
    "NT",
    "CEDT",
    "ICE",
    "NANO",
    "ADME",
    "CHPE",
    "AI",
    "AERO",
    "SEMI",
)

# Input student information
n = int(input())
students = []
for _ in range(n):
    data = input().strip().split()
    students.append(data)

# Input query as a set
query = set(input().strip().split())

# Search for students matching the query
results = []
for student in students:
    name, group, generation, department = student
    if (
        query.issubset(set(student))
        and (name not in GROUPS)
        and (name not in DEPARTMENTS)
    ):
        results.append(student)

# Output
if len(results) == 0:
    print("Not Found")
else:
    results.sort()
    for name, group, generation, department in results:
        print(name, group, generation, department)
```
