<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    T-Score ★☆ (
      <a href="https://drive.google.com/file/d/1h5utWIzFUcnS0tCOtFIpk-so8qWSDqZ6/view?usp=sharing">
        <code>2567_1_Q4_B1-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐาน**](#ค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐาน)
-   [**การคำนวณคะแนน T-Score**](#การคำนวณคะแนน-t-score)
-   [**การเก็บลำดับและการแสดงผล**](#การเก็บลำดับและการแสดงผล)
-   [**ข้อแตกต่างของชื่อประเภทข้อสอบ**](#ข้อแตกต่างของชื่อประเภทข้อสอบ)
-   [**Solution**](#solution)

---

## ค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐาน

ขั้นแรกต้องสรุปตำแหน่งและการกระจายของคะแนนดิบทั้งหมด

ค่าเฉลี่ยของคะแนน $x_1, x_2, \ldots, x_n$ คือ

$$
\mu = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

ตรงกับ Python ใน `get_mean` ว่า

```python
sum(scores) / len(scores)
```

โจทย์ใช้ส่วนเบี่ยงเบนมาตรฐานของ **ประชากร** จึงหารผลรวมด้วย `n`
ไม่ใช่ `n - 1`

$$
\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2}
$$

ฟังก์ชัน `get_std_dev` สร้าง `(score - mean) ** 2` ของทุกคะแนน
หาค่าเฉลี่ยของผลต่างกำลังสอง แล้วถอดรากด้วย `** 0.5`
โจทย์รับประกันว่าคะแนนไม่ได้เท่ากันทั้งหมด จึงมี `std_dev > 0`
และไม่เกิดการหารด้วยศูนย์

---

## การคำนวณคะแนน T-Score

คะแนนดิบแต่ละตัวถูกแปลงด้วยรูปทั่วไป

$$
t_i = 50 + c\left(\frac{x_i-\mu}{\sigma}\right)
$$

โดยค่าคงที่ `c` ขึ้นกับประเภทข้อสอบ

| ประเภท | `c` ในโค้ด |
|:---|---:|
| `TGAT`, `TPAT` | `8.69031` |
| `A-Level` | `5.21299` |

ส่วน `(score - mean_score) / std_dev` บอกว่าคะแนนนั้นอยู่ห่างจากค่าเฉลี่ย
กี่ส่วนเบี่ยงเบนมาตรฐาน คะแนนเท่าค่าเฉลี่ยจึงได้ T-Score เท่ากับ `50`

---

## การเก็บลำดับและการแสดงผล

โปรแกรมวน `scores` จากซ้ายไปขวา คำนวณและเพิ่มผลลัพธ์เข้า `t_scores`
ในลำดับเดียวกัน จึงไม่ต้องเก็บตำแหน่งแยกต่างหาก

แต่ละค่าถูกปัดด้วย

```python
str(round(t_score, 2))
```

แล้วเชื่อมด้วยช่องว่าง `round(..., 2)` แสดงทศนิยม **อย่างมาก** สองตำแหน่ง
จึงอาจได้ `50.0` แทน `50.00` ซึ่งตรงกับรูปแบบตัวอย่าง

---

## ข้อแตกต่างของชื่อประเภทข้อสอบ

> [!WARNING]
>
> PDF ระบุชื่อประเภทเป็น `A-LEVEL` แต่โค้ดตรวจข้อความ `A-Level`
> แบบตรงตัวและ Python แยกตัวพิมพ์เล็ก–ใหญ่ ถ้าป้อน `A-LEVEL` ตาม PDF
> เงื่อนไขทั้งสองแขนงจะไม่ทำงาน ตัวแปร `t_score` จึงคงเป็น `0`
> และผลลัพธ์ทุกตัวเป็น `0`
>
> Solution ด้านล่างคง spelling และพฤติกรรมของไฟล์ `.py` ไว้ตามเดิม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q4_B1-S.py
# Problem   : T-Score
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize constants
DEFAULT_AVG_SCORE = 50.0
TGAT_TPAT_CONST = 8.69031
A_LEVEL_CONST = 5.21299


# Function to calculate the mean of a list of scores
def get_mean(scores):
    # Check if the list is empty
    if len(scores) == 0:
        return 0.0
    # Return the mean of the scores
    return sum(scores) / len(scores)


# Function to calculate the standard deviation of a list of scores
def get_std_dev(scores, mean):
    # Check if the list is empty
    if len(scores) == 0:
        return 0.0

    # Calculate the squared differences between each score and the mean
    squared_diffs = []
    for score in scores:
        squared_diffs.append((score - mean) ** 2)
    # Return the standard deviation
    return (sum(squared_diffs) / len(scores)) ** 0.5


# Input the scores list and the subject
scores = [int(score) for score in input().split()]
subject = input().strip()

# Calculate the mean and standard deviation of the scores
mean_score = get_mean(scores)
std_dev = get_std_dev(scores, mean_score)

# Initialize the list to hold T-scores
t_scores = []

# Calculate T-scores based on the subject
for score in scores:
    t_score = 0
    # Calculate T-score of subject TGAT, TPAT
    if subject in ["TGAT", "TPAT"]:
        t_score = DEFAULT_AVG_SCORE + TGAT_TPAT_CONST * ((score - mean_score) / std_dev)

    # Calculate T-score of subject A-Level
    elif subject == "A-Level":
        t_score = DEFAULT_AVG_SCORE + A_LEVEL_CONST * ((score - mean_score) / std_dev)

    # Append the calculated T-score rounded to two decimal places to the list
    t_scores.append(str(round(t_score, 2)))

# Output the T-scores
print(" ".join(t_scores))
```
