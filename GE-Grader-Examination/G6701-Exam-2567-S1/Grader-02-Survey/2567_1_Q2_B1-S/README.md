<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Median of Median of K ★★ (
      <a href="https://drive.google.com/file/d/1Vx9cJXyPUt1ZQ8ffg9O-ZhJ8uTnrOsWl/view?usp=sharing">
        <code>2567_1_Q2_B1-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การหามัธยฐาน**](#การหามัธยฐาน)
-   [**การแบ่งข้อมูลเป็นกลุ่ม**](#การแบ่งข้อมูลเป็นกลุ่ม)
-   [**การหามัธยฐานของมัธยฐาน**](#การหามัธยฐานของมัธยฐาน)
-   [**กรณีขอบและการแสดงผล**](#กรณีขอบและการแสดงผล)
-   [**Solution**](#solution)

---

## การหามัธยฐาน

มัธยฐานคือค่ากึ่งกลางของข้อมูล **หลังเรียงจากน้อยไปมาก** โปรแกรมแยกงานนี้ไว้ใน
ฟังก์ชัน `get_median()` โดยใช้ `sorted()` สร้างลิสต์ที่เรียงแล้วขึ้นมาใหม่
จึงไม่เปลี่ยนลำดับของลิสต์ที่ส่งเข้าฟังก์ชัน

ให้ `n` เป็นจำนวนข้อมูล และ `mid = n // 2`

-   ถ้า `n` เป็นจำนวนคี่ ค่ากลางอยู่ที่ `nums[mid]`
-   ถ้า `n` เป็นจำนวนคู่ ต้องเฉลี่ยสองค่ากลาง คือ
    $(\text{nums[mid-1]}+\text{nums[mid]})/2$

โค้ดเขียนสองกรณีนี้ว่า

```python
if n % 2 == 0:
    return (nums[mid - 1] + nums[mid]) / 2
return float(nums[mid])
```

การหารด้วย `/` และการแปลงด้วย `float()` ทำให้ฟังก์ชันคืนมัธยฐานเป็น
`float` ทั้งกรณีจำนวนข้อมูลคู่และคี่ เช่น อาจแสดง `3.0` แทน `3`

---

## การแบ่งข้อมูลเป็นกลุ่ม

อินพุตบรรทัดแรกคือจำนวนเต็มบวก `k` ส่วนบรรทัดที่สองคือรายการจำนวนเต็ม
โปรแกรมเดินตำแหน่งเริ่มกลุ่มด้วย

```python
for idx in range(0, len(nums), k):
```

จึงได้ `idx` เป็น `0, k, 2*k, ...` และตัดแต่ละกลุ่มด้วย
`nums[idx : idx + k]` ซึ่งมีสมาชิกที่อยู่ติดกันไม่เกิน `k` ตัว

ถ้าจำนวนข้อมูลหารด้วย `k` ไม่ลงตัว slice ของกลุ่มสุดท้ายจะหยุดที่ท้ายลิสต์เอง
กลุ่มสุดท้ายจึงมีน้อยกว่า `k` ตัวได้ และต้องนำกลุ่มสั้นนี้ไปหามัธยฐานด้วย

---

## การหามัธยฐานของมัธยฐาน

โปรแกรมหามัธยฐานของแต่ละกลุ่มแล้วเก็บไว้ใน `medians`
จากนั้นเรียก `get_median(medians)` อีกครั้งเพื่อหาคำตอบสุดท้าย

ตัวอย่าง `k = 3` และข้อมูล `4 1 7 2 9`

1. แบ่งได้ `[4, 1, 7]` และ `[2, 9]`
2. มัธยฐานของสองกลุ่มคือ `4.0` และ `5.5`
3. มัธยฐานของ `[4.0, 5.5]` คือ $(4.0+5.5)/2=4.75$

ดังนั้นโปรแกรมแสดง `4.75`

---

## กรณีขอบและการแสดงผล

-   ถ้า `k = 1` แต่ละกลุ่มมีหนึ่งตัว แล้วคำตอบคือมัธยฐานของข้อมูลทั้งหมด
-   ถ้า `k` มากกว่าหรือเท่ากับจำนวนข้อมูล จะมีเพียงกลุ่มเดียว
    คำตอบจึงเป็นมัธยฐานของกลุ่มนั้น
-   ทั้งกลุ่มย่อยและลิสต์ `medians` อาจมีจำนวนสมาชิกเป็นคู่
    จึงต้องใช้สูตรเฉลี่ยสองค่ากลางให้ถูกต้องทั้งสองรอบ
-   โปรแกรมแสดงคำตอบจาก `get_median()` โดยตรง ไม่มีการปัดเศษหรือกำหนด
    จำนวนตำแหน่งทศนิยมเพิ่มเติม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q2_B1-S.py
# Problem   : Median of Median of K
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------


# Function to calculate the median of a unsorted list
def get_median(unsorted_nums):
    # Sort the list in ascending order
    nums = sorted(unsorted_nums)

    # Get the length of the list and middle index
    n = len(nums)
    mid = n // 2

    # Return the median value of the even length list
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2

    # Return the median value of the odd length list
    return float(nums[mid])


# Input k and the list of integers
k = int(input())
nums = [int(num) for num in input().split()]

# Initialize a list to store medians of each k-sized segment
medians = []

# Calculate the median for each segment of size k
for idx in range(0, len(nums), k):
    medians.append(get_median(nums[idx : idx + k]))

# Calculate and print the median of the medians
print(get_median(medians))
```
