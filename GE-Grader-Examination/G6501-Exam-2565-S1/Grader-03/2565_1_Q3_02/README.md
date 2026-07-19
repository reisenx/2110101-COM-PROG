<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Graduation Ceremony ★★★ (
      <a href="https://drive.google.com/file/d/1WBB8TOkW_fw3vlitH2TXXcxpklcce0la/view?usp=sharing">
        <code>2565_1_Q3_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเชื่อมข้อมูลบัณฑิต แขก และคณะ**](#การเชื่อมข้อมูลบัณฑิต-แขก-และคณะ)
-   [**การหาคณะที่แขกทุกคนต้องไป**](#การหาคณะที่แขกทุกคนต้องไป)
-   [**การเรียงและแสดงผล**](#การเรียงและแสดงผล)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวังเรื่องการแก้ไข Set เดิม**](#ข้อควรระวังเรื่องการแก้ไข-set-เดิม)
-   [**Solution**](#solution)

---

## การเชื่อมข้อมูลบัณฑิต แขก และคณะ

ข้อมูลของโจทย์มีความสัมพันธ์อยู่ 2 ชั้น

1. บัณฑิตแต่ละคนสังกัดคณะใด
2. แขกแต่ละคนจะไปแสดงความยินดีกับบัณฑิตคนใดบ้าง

บรรทัดแรกมีจำนวนเต็ม `N M K` โดย

-   `N` คือจำนวนบัณฑิต
-   `M` คือจำนวนแขก
-   `K` คือจำนวนกลุ่มแขกที่ต้องหาคำตอบ

ตัวแปรในโปรแกรมจึงรับค่าตามลำดับดังนี้

```python
student_count, guest_count, testcases = [int(amt) for amt in input().split()]
```

> [!NOTE]
>
> comment ใน Solution เขียนว่าค่าทั้งสามเป็นจำนวน students, faculties และ
> testcases แต่ค่าที่สองตามโจทย์และตัวแปร `guest_count` คือ **จำนวนแขก**
> ไม่ใช่จำนวนคณะ

### จากบัณฑิตไปยังคณะ

ใช้ dictionary `students_faculty` เก็บชื่อบัณฑิตเป็น key และชื่อคณะเป็น value

```python
students_faculty[student] = faculty
```

เช่น ถ้า `Nami` อยู่ `faculty_a` ค่า
`students_faculty["Nami"]` จะเป็น `"faculty_a"`

### จากแขกไปยังเซตของคณะ

แขกหนึ่งคนอาจไปหาบัณฑิตหลายคน และบัณฑิตเหล่านั้นอาจอยู่คณะเดียวกัน
จึงใช้ `set` เก็บคณะที่แขกต้องไป เพื่อให้ชื่อคณะแต่ละชื่อปรากฏเพียงครั้งเดียว

ให้ `V(g)` เป็นกลุ่มบัณฑิตที่แขก `g` ไปหา และให้ `S(s)` เป็นคณะของบัณฑิต
`s` เซตคณะที่แขกต้องไปคือ

$$
F(g) = \{S(s) \mid s \in V(g)\}
$$

โค้ดอ่านชื่อแรกเป็นชื่อแขก และชื่อที่เหลือเป็นรายชื่อบัณฑิต

```python
people = input().split()
guest = people[0]
students = people[1:]
```

จากนั้นค้นหาคณะของบัณฑิตทีละคน แล้วเก็บเซตไว้ใน `guest_faculties`

```python
faculties = set()
for student in students:
    faculties.add(students_faculty[student])
guest_faculties[guest] = faculties
```

ตามข้อกำหนด แขกแต่ละคนจะมีชื่อบัณฑิตตามหลังอย่างน้อย 1 คน

---

## การหาคณะที่แขกทุกคนต้องไป

ในแต่ละ testcase โจทย์ให้รายชื่อแขกอย่างน้อย 2 คน
เราต้องหาคณะที่อยู่ในเซตของแขก **ทุกคน** ไม่ใช่คณะที่แขกคนใดคนหนึ่งไป
การทำงานนี้เรียกว่า intersection หรือส่วนร่วมของเซต

ถ้ากลุ่มที่สนใจคือแขก `g_1, g_2, ..., g_k` คำตอบคือ

$$
R = F(g_1) \cap F(g_2) \cap \cdots \cap F(g_k)
$$

โปรแกรมเริ่มจากเซตของแขกคนแรก แล้วใช้ `&=` หาส่วนร่วมกับแขกคนถัดไป
ตามลำดับ

```python
result = guest_faculties[guests[0]]
for guest in guests[1:]:
    result &= guest_faculties[guest]
```

ตัวอย่างเช่น ถ้า

-   `Eren` ต้องไป `{faculty_a, faculty_c}`
-   `Anya` ต้องไป `{faculty_a, faculty_b}`

ส่วนร่วมจะเหลือเพียง `{faculty_a}` เพราะเป็นคณะเดียวที่ทั้งสองคนต้องไป

---

## การเรียงและแสดงผล

สมาชิกของ `set` ไม่มีลำดับที่นำไปใช้เป็นผลลัพธ์ได้โดยตรง
โจทย์กำหนดให้เรียงชื่อคณะตามพจนานุกรม จึงใช้ `sorted(result)`
ก่อนเชื่อมชื่อด้วยช่องว่างหนึ่งช่อง

```python
print(" ".join(sorted(result)))
```

ถ้า `result` เป็นเซตว่าง แสดงข้อความ `None` แทน

```python
if len(result) > 0:
    print(" ".join(sorted(result)))
else:
    print("None")
```

โปรแกรมแสดงทั้งหมด `K` บรรทัด โดยลำดับผลลัพธ์ตรงกับลำดับของ
`K` กลุ่มสุดท้ายในข้อมูลนำเข้า

---

## ลำดับการทำงาน

1. รับจำนวนบัณฑิต `N` จำนวนแขก `M` และจำนวน testcase `K`
2. สร้าง `students_faculty` จากข้อมูลบัณฑิต `N` บรรทัด
3. สำหรับแขกแต่ละคน ค้นหาคณะของบัณฑิตทุกคนที่แขกจะไปหา
4. เก็บเซตคณะของแขกไว้ใน `guest_faculties`
5. รับรายชื่อแขกของ testcase หนึ่งบรรทัด
6. หาส่วนร่วมของเซตคณะของแขกทุกคนในบรรทัด
7. ถ้ามีคำตอบ ให้เรียงชื่อคณะแล้วแสดงโดยคั่นด้วยช่องว่าง
8. ถ้าไม่มีคณะร่วมกัน ให้แสดง `None`
9. ทำข้อ 5–8 ให้ครบ `K` testcase

---

## ตัวอย่างการทำงาน

จากตัวอย่างในโจทย์

-   `Eren` ไปหา `Nami`, `Chopper` และ `Brook` จึงต้องไป
    `{faculty_a, faculty_c}`
-   `Anya` ไปหา `Sanji` และ `Luffy` จึงต้องไป
    `{faculty_a, faculty_b}`
-   `Yaiba` ไปหา `Franky` จึงต้องไป `{faculty_b}`

กลุ่ม `Eren Anya` มีส่วนร่วมเป็น `{faculty_a}` ส่วนกลุ่ม
`Anya Eren Yaiba` ไม่มีคณะที่ทุกคนต้องไปเหมือนกัน จึงได้ผลลัพธ์

```text
faculty_a
None
```

---

## ข้อควรระวังเรื่องการแก้ไข Set เดิม

> [!WARNING]
>
> คำสั่ง `result = guest_faculties[guests[0]]` ทำให้ `result`
> อ้างถึง set ก้อนเดียวกับที่เก็บอยู่ใน dictionary ไม่ได้สร้าง set ก้อนใหม่
> เมื่อใช้ `result &= guest_faculties[guest]` โปรแกรมจึงแก้ไขเซตของแขกคนแรก
> ใน `guest_faculties` ไปพร้อมกัน
>
> ผลข้างเคียงนี้ทำให้ testcase หลังจากนั้นอาจใช้ข้อมูลคณะของแขกคนแรกที่ถูกลดรูป
> ไปแล้ว แทนข้อมูลเดิมจากอินพุต ตัวอย่างเช่น ถ้า `g1` มี `{a, b}` และ testcase
> แรกหาส่วนร่วมของ `g1` กับแขกที่มี `{a}` ค่า `g1` จะเหลือ `{a}` ใน
> dictionary ด้วย ดังนั้นควรอ่านคำอธิบายการทำงานของ Solution โดยคำนึงถึง
> การเปลี่ยนแปลงนี้ระหว่าง testcase

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_1_Q3_02.py
# Problem   : Graduation Ceremony
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input number of students, faculties, and testcases
student_count, guest_count, testcases = [int(amt) for amt in input().split()]

# Create a dictionary to map students to their faculty
students_faculty = {}
for _ in range(student_count):
    student, faculty = input().split()
    students_faculty[student] = faculty

# Create a dictionary to map each guest to the set of faculties of their students
guest_faculties = {}
for _ in range(guest_count):
    # Read the guest name and their visited students
    people = input().split()
    guest = people[0]
    students = people[1:]

    # Create a set of faculties for the visited students of each guest
    faculties = set()
    for student in students:
        faculties.add(students_faculty[student])
    # Store the faculties in the guest_faculties dictionary
    guest_faculties[guest] = faculties

# Process each testcase to find the common faculties among the guests
for _ in range(testcases):
    # Read the guests for this testcase
    guests = input().split()

    # Find the common faculties among the guests
    result = guest_faculties[guests[0]]
    for guest in guests[1:]:
        result &= guest_faculties[guest]

    # Output the common faculties alphabetically
    if len(result) > 0:
        print(" ".join(sorted(result)))
    else:
        print("None")
```
