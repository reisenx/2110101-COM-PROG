<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    File Min-Max-Average ★★ (
      <a href="https://drive.google.com/file/d/1g8qEXc7_TKpAVXmD9HZSHeysBDMZwiv4/view?usp=drive_link">
        <code>07_StrFile_23</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเตรียมปีที่ต้องการ**](#การเตรียมปีที่ต้องการ)
-   [**การอ่านและคัดเลือกคะแนน**](#การอ่านและคัดเลือกคะแนน)
-   [**การคำนวณผลลัพธ์**](#การคำนวณผลลัพธ์)
-   [**รูปแบบผลลัพธ์**](#รูปแบบผลลัพธ์)
-   [**Solution**](#solution)

---

## การเตรียมปีที่ต้องการ

ข้อมูลนำเข้าหนึ่งบรรทัดประกอบด้วยชื่อแฟ้มและปี พ.ศ. ที่นิสิตเริ่มเข้าศึกษา
คั่นด้วยช่องว่าง โปรแกรมจึงแยกข้อมูลทั้งสองส่วนด้วย `split()`

```python
filename, year = input().strip().split()
```

เลขประจำตัวนิสิตในแฟ้มเก็บปีที่เริ่มเข้าศึกษาไว้ในตัวเลขสองหลักแรก
แต่ปีที่รับมาอยู่ในรูป พ.ศ. เช่น `2562` โปรแกรมจึงเลือกสองหลักสุดท้ายด้วย
slice `year[-2:]`

```python
year = year[-2:]
```

ดังนั้น `"2562"[-2:]` ได้ `"62"` ซึ่งพร้อมนำไปเปรียบเทียบกับ
`student_id[:2]` เช่น เลขประจำตัว `6230012121` มีสองหลักแรกเป็น `"62"`
จึงเป็นข้อมูลของนิสิตที่เริ่มศึกษาในปี พ.ศ. 2562

## การอ่านและคัดเลือกคะแนน

คำสั่ง `with open(filename) as file:` เปิดแฟ้มตามชื่อที่รับมา และช่วยปิดแฟ้มให้
โดยอัตโนมัติเมื่ออ่านเสร็จ โปรแกรมอ่านข้อมูลทีละบรรทัด โดยแต่ละบรรทัดมี
เลขประจำตัวนิสิตและคะแนน

```python
student_id, score = line.strip().split()
```

คะแนนจากแฟ้มยังเป็นข้อความ โปรแกรมจะคัดเลือกเฉพาะบรรทัดที่สองหลักแรกของ
เลขประจำตัวตรงกับปีที่ต้องการ แล้วแปลงคะแนนเป็น `float` ก่อนเก็บในลิสต์
`scores`

```python
if student_id[:2] == year:
    scores.append(float(score))
```

ตัวอย่างเช่น เมื่อเลือกปี `2562` จากข้อมูลในโจทย์ ลิสต์ `scores` จะเป็น
`[90.0, 80.0, 70.0, 60.0, 50.0]` ส่วนคะแนนของปีอื่นจะไม่ถูกเพิ่มเข้ามา

## การคำนวณผลลัพธ์

ก่อนคำนวณ โปรแกรมตรวจว่า `scores` มีข้อมูลอย่างน้อยหนึ่งค่าด้วย
`len(scores) > 0` เพราะ `min()` และ `max()` ใช้กับลิสต์ว่างไม่ได้
และการหาค่าเฉลี่ยของลิสต์ว่างจะทำให้เกิดการหารด้วยศูนย์

ถ้ามีข้อมูล คะแนนน้อยสุดและมากสุดหาได้ด้วย `min(scores)` และ `max(scores)`
ส่วนคะแนนเฉลี่ยคำนวณจากสูตร

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

ซึ่งเขียนในภาษา Python ได้เป็น

```python
avg_score = sum(scores) / len(scores)
```

สำหรับคะแนนของปี `2562` จะได้คะแนนน้อยสุด `50.0` คะแนนมากสุด `90.0`
และคะแนนเฉลี่ย

$$
\frac{90.0 + 80.0 + 70.0 + 60.0 + 50.0}{5} = 70.0
$$

## รูปแบบผลลัพธ์

เมื่อมีข้อมูล โปรแกรมแสดงผลตามลำดับ **คะแนนน้อยสุด คะแนนมากสุด
และคะแนนเฉลี่ย** ในบรรทัดเดียว

```python
print(min_score, max_score, avg_score)
```

`print()` จะแทรกช่องว่างหนึ่งช่องระหว่างค่าทั้งสาม โปรแกรมไม่ได้ปัดเศษหรือ
กำหนดจำนวนตำแหน่งทศนิยมเพิ่มเติม แต่แสดงค่าชนิด `float` ตามรูปแบบปกติของ
Python ดังนั้นผลจากการคำนวณบางชุดอาจมีรายละเอียดของเลขทศนิยมแบบ
floating-point ปรากฏออกมา

ถ้าไม่มีเลขประจำตัวของปีที่ต้องการ ลิสต์ `scores` จะว่างและโปรแกรมแสดง
`No data` โดยต้องใช้ตัวพิมพ์ใหญ่-เล็กและช่องว่างตามนี้ให้ตรงกับโจทย์

---

# Solution

```python
# --------------------------------------------------
# File Name : 07_StrFile_23.py
# Problem   : File Min Max Average
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input filename and year (extract last two digits)
filename, year = input().strip().split()
year = year[-2:]

# Initialize lists to store scores
scores = []

# Read the file and extract scores for the specified year
with open(filename) as file:
    for line in file:
        student_id, score = line.strip().split()
        if student_id[:2] == year:
            scores.append(float(score))

if len(scores) > 0:
    # Calculate min, max, and average
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)

    # Print the results
    print(min_score, max_score, avg_score)
else:
    print("No data")
```
