<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Function Call ★★ (
      <a href="https://drive.google.com/file/d/1MF_AAjBOT99rBndyP_Sw9rreKERif-pu/view?usp=drive_link">
        <code>06_Func_21</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ข้อมูลนำเข้าและข้อมูลส่งออก**](#ข้อมูลนำเข้าและข้อมูลส่งออก)
-   [**แบ่งหน้าที่ให้แต่ละฟังก์ชัน**](#แบ่งหน้าที่ให้แต่ละฟังก์ชัน)
-   [**ตรวจคำตอบและคำนวณคะแนน**](#ตรวจคำตอบและคำนวณคะแนน)
-   [**ตัดเกรดตามช่วงคะแนน**](#ตัดเกรดตามช่วงคะแนน)
-   [**เรียงลำดับและแสดงผล**](#เรียงลำดับและแสดงผล)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**Solution**](#solution)

---

## ข้อมูลนำเข้าและข้อมูลส่งออก

โจทย์ข้อนี้ให้ฟังก์ชันสำหรับตรวจข้อสอบไว้แล้ว
หน้าที่ของเราคือเรียกใช้แต่ละฟังก์ชันตามลำดับที่เหมาะสม ตั้งแต่รับคำตอบ
คำนวณคะแนน ตัดเกรด เรียงลำดับ ไปจนถึงแสดงผล

ข้อมูลนำเข้ามีลำดับดังนี้

1. บรรทัดแรกเป็นสตริง `solution` ซึ่งเก็บเฉลยของทุกข้อเรียงต่อกัน
2. บรรทัดที่สองเป็นจำนวนเต็ม `n` แทนจำนวนนักเรียน
3. อีก `n` บรรทัด แต่ละบรรทัดมี `student_id` และ `ans`
   คั่นด้วยช่องว่าง โดย `ans` คือคำตอบของนักเรียนคนนั้น

ผลลัพธ์ของนักเรียนแต่ละคนมี 3 ค่า ได้แก่ เลขประจำตัว คะแนนร้อยละ และเกรด
คั่นด้วยช่องว่าง นักเรียนที่ได้คะแนนมากกว่าจะอยู่ก่อน
หากคะแนนเท่ากันจะเรียงเลขประจำตัวจากมากไปน้อย

---

## แบ่งหน้าที่ให้แต่ละฟังก์ชัน

การแยกงานเป็นฟังก์ชันช่วยให้แต่ละส่วนมีหน้าที่ชัดเจน
และทำให้ฟังก์ชันหนึ่งนำผลจากอีกฟังก์ชันไปใช้ต่อได้

| ฟังก์ชัน | หน้าที่ | ผลลัพธ์หรือผลที่เกิดขึ้น |
| :-- | :-- | :-- |
| `read_answers()` | อ่านจำนวนนักเรียนและคำตอบของนักเรียนทุกคน | คืนลิสต์รูปแบบ `[[student_id, ans], ...]` |
| `marking(answer, solution)` | เปรียบเทียบคำตอบกับเฉลยทีละตำแหน่ง | คืนจำนวนข้อที่ตอบถูก |
| `grading(score)` | เปรียบเทียบคะแนนร้อยละกับเกณฑ์ | คืนเกรดเป็นสตริง เช่น `"A"` |
| `scoring(answers, solution)` | เรียก `marking()` และ `grading()` ให้ครบทุกคน | คืนลิสต์รูปแบบ `[[student_id, score, grade], ...]` |
| `sort(scores)` | เรียงข้อมูลใน `scores` จากน้อยไปมาก | แก้ไขลิสต์เดิมโดยตรงและไม่คืนค่า |
| `report(scores)` | แสดงเลขประจำตัว คะแนน และเกรดทีละคน | พิมพ์ผลลัพธ์คนละหนึ่งบรรทัด |

ตัวอย่างเช่น ในคำสั่ง
`for student_id, ans in answers:` สมาชิกย่อย `[student_id, ans]`
จะถูกแยกเก็บในตัวแปรสองตัวโดยอัตโนมัติ ทำให้ส่ง `ans` ไปตรวจคะแนน
พร้อมเก็บ `student_id` ของเจ้าของคำตอบไว้ได้

---

## ตรวจคำตอบและคำนวณคะแนน

ฟังก์ชัน `marking()` ใช้ดัชนี `i` เดินผ่านตัวอักษรของ `answer`
ถ้าคำตอบและเฉลยที่ตำแหน่งเดียวกันเท่ากัน จะเพิ่ม `score` ขึ้น `1`

```python
if answer[i] == solution[i]:
    score += 1
```

ค่าที่ฟังก์ชันนี้คืนมาจึงเป็น **จำนวนข้อที่ตอบถูก** ไม่ใช่คะแนนร้อยละ
ฟังก์ชัน `scoring()` จะนำค่านี้มาแปลงเป็นร้อยละด้วยสูตร

$$
\text{คะแนนร้อยละ}
= \frac{\text{จำนวนข้อที่ตอบถูก}}{\text{จำนวนข้อทั้งหมด}} \times 100
$$

ซึ่งตรงกับคำสั่ง Python

```python
score = marking(ans, solution) / len(solution) * 100
```

ตัวอย่างเช่น ถ้า `solution` คือ `"ABCD"` และ `ans` คือ `"ABAD"`
นักเรียนตอบถูก 3 จาก 4 ข้อ จึงได้คะแนน
`3 / 4 * 100` เท่ากับ `75.0`

> [!NOTE]
>
> โปรแกรมนี้อาศัยข้อมูลตามเงื่อนไขของโจทย์ คือ `solution` ต้องไม่เป็นสตริงว่าง
> และคำตอบของนักเรียนต้องมีจำนวนตัวอักษรเท่ากับเฉลย เพื่อให้การเข้าถึง
> `solution[i]` และการหารด้วย `len(solution)` ทำงานได้ถูกต้อง

---

## ตัดเกรดตามช่วงคะแนน

ค่าคงที่ `GRADING_CRITERIA` เรียงเกณฑ์จากคะแนนสูงไปต่ำ
ฟังก์ชัน `grading()` ตรวจเกณฑ์ตามลำดับและคืนเกรดทันทีที่พบเกณฑ์แรก
ที่คะแนนถึง

| คะแนนร้อยละ `score` | เกรด |
| :--: | :--: |
| `score >= 80` | `A` |
| `70 <= score < 80` | `B` |
| `60 <= score < 70` | `C` |
| `50 <= score < 60` | `D` |
| `score < 50` | `F` |

ลำดับของเกณฑ์สำคัญ เช่น คะแนน `85.0` ผ่านทั้งเกณฑ์ `80`, `70`, `60`
และ `50` แต่โปรแกรมพบเกณฑ์ `80` ก่อน จึงคืน `"A"`
ส่วนคะแนนที่ไม่ถึง `50` จะไม่เข้าเงื่อนไขใดในลูปและไปคืน `"F"` ตอนท้าย

---

## เรียงลำดับและแสดงผล

ก่อนเรียง ข้อมูลแต่ละคนอยู่ในรูป `[student_id, score, grade]`
แต่โจทย์ต้องการให้ใช้คะแนนเป็นเกณฑ์แรก ฟังก์ชัน `sort()` จึงสร้างข้อมูลชั่วคราว
เป็น `[score, student_id, grade]` แล้วเรียก `sorted_scores.sort()`

เมื่อเรียงลิสต์ย่อย Python จะเปรียบเทียบสมาชิกจากซ้ายไปขวา ดังนี้

1. เรียง `score` จากน้อยไปมาก
2. หากคะแนนเท่ากัน เรียง `student_id` จากน้อยไปมาก
3. จากนั้นฟังก์ชันจึงสลับแต่ละรายการกลับเป็น
   `[student_id, score, grade]` และเขียนทับลงใน `scores`

`student_id` ไม่ได้ถูกแปลงด้วย `int()` จึงยังเป็นสตริง
ทั้งเลขศูนย์ด้านหน้าและการเปรียบเทียบแบบสตริงจึงถูกเก็บไว้ เช่น `"0011"`

ในตอนเรียก `report()` โปรแกรมส่ง `scores[::-1]` เข้าไป
การ slice ด้วย step เท่ากับ `-1` จะสร้างลิสต์ที่มีลำดับย้อนกลับ
ผลจากการเรียงน้อยไปมากจึงกลายเป็น **คะแนนมากไปน้อย**
และเมื่อคะแนนเท่ากันก็กลายเป็น **เลขประจำตัวแบบสตริงจากมากไปน้อย** ตามโจทย์
เช่น ที่คะแนน `80.0` เท่ากัน `"5555"` จะอยู่ก่อน `"2222"`

ฟังก์ชัน `report()` ใช้ `print(student_id, score, grade)`
จึงคั่นทั้งสามค่าด้วยช่องว่างโดยอัตโนมัติ ส่วน `score` เกิดจากเครื่องหมาย `/`
จึงเป็น `float` เช่น `100.0` หรือ `80.0` และโค้ดไม่ได้ใช้ `round()`
หรือกำหนดจำนวนตำแหน่งทศนิยมเพิ่มเติม Python จะแสดงค่า `float` ตามปกติ

---

## ลำดับการทำงานของโปรแกรม

ส่วนหลักของโปรแกรมเชื่อมฟังก์ชันทั้งหมดเข้าด้วยกันตามลำดับนี้

1. `solution = input().strip()` อ่านเฉลยและตัดช่องว่างที่หัวกับท้าย
2. `answers = read_answers()` อ่านเลขประจำตัวและคำตอบของนักเรียนทุกคน
3. `scores = scoring(answers, solution)` ตรวจคำตอบ คำนวณร้อยละ และตัดเกรด
4. `sort(scores)` เรียงลิสต์ `scores` จากน้อยไปมากโดยแก้ไขลิสต์เดิม
5. `report(scores[::-1])` ย้อนลำดับแล้วแสดงรายงานจากมากไปน้อย

จุดสำคัญคือ `sort(scores)` ไม่ได้คืนลิสต์ใหม่ แต่แก้ไข `scores` โดยตรง
ดังนั้นหลังเรียกฟังก์ชัน ข้อมูลที่เรียงแล้วจึงพร้อมนำไปย้อนลำดับและส่งให้
`report()` ได้ทันที

---

# Solution

```python
# --------------------------------------------------
# File Name : 06_Func_21.py
# Problem   : Function Call
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Constants for grading criteria
# - A: 80 and above
# - B: 70 to 79
# - C: 60 to 69
# - D: 50 to 59
# - F: below 50
GRADING_CRITERIA = [[80, "A"], [70, "B"], [60, "C"], [50, "D"]]


# This function reads answers from input
# It returns a list in the format [[sid1, ans1], [sid2, ans2], ...]
def read_answers():
    n = int(input())
    answers = []
    for _ in range(n):
        student_id, ans = input().split()
        answers.append([student_id, ans])
    return answers


# This function can mark a single answer against a its solution
def marking(answer, solution):
    score = 0
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    return score


# This function grades a score based on the grading criteria
def grading(score):
    for required_score, letter in GRADING_CRITERIA:
        if score >= required_score:
            return letter
    return "F"


# This function scores a list of answers against a solution
# "answers" is [[student_id1, ans1], [student_id2, ans2], ...]
# "solution" is a string representing the correct answer
# It returns a [[student_id1, score1, grade1], [student_id2, score2, grade2], ...]
def scoring(answers, solution):
    scores = []
    for student_id, ans in answers:
        score = marking(ans, solution) / len(solution) * 100
        grade = grading(score)
        scores.append([student_id, score, grade])
    return scores


# This function prints the scores in the specified format
def report(scores):
    for student_id, score, grade in scores:
        print(student_id, score, grade)


# This function sorts the scores in ascending order based on score
def sort(scores):
    sorted_scores = []
    for student_id, score, grade in scores:
        sorted_scores.append([score, student_id, grade])
    sorted_scores.sort()

    for i in range(len(scores)):
        score, student_id, grade = sorted_scores[i]
        scores[i] = [student_id, score, grade]


# Input the solution
solution = input().strip()

# Read the answers from input
answers = read_answers()

# Score the answers against the solution
scores = scoring(answers, solution)

# Sort the scores in ascending order
sort(scores)

# Print the report of scores in descending order
report(scores[::-1])
```
