<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Upgrade 2 (Function) ★★ (
      <a href="https://drive.google.com/file/d/1xpFZCr1TpqaLzLu_44UAiL62cVE5i7t-/view?usp=drive_link">
        <code>05_List_F22</code>
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
# File Name : 05_List_F22.py
# Problem   : Upgrade 2 (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of letter grades
GRADES = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]


# Find the index of a student ID in the grades list
def index_of(grades, id):
    idx = 0
    for idx in range(len(grades)):
        student_id = grades[idx][0]
        if student_id == id:
            return idx
    return -1


# Upgrade the grades of students based on their IDs
# After upgrading, sort students by ID in ascending order
def upgrade(grades, student_ids):
    for student_id in student_ids:
        idx = index_of(grades, student_id)

        if idx > -1:
            old_grade = GRADES.index(grades[idx][1])
            new_grade = GRADES[max(0, old_grade - 1)]
            grades[idx][1] = new_grade
    grades.sort()


# Execute the input string as code
exec(input())
exec(input())
exec(input())
```
