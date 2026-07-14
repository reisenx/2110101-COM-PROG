<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Duration (Function) ★★ (
      <a href="https://drive.google.com/file/d/1ZgwtK1C-FFU7v2BkYiNgJ_vXWWGgA-EP/view?usp=drive_link">
        <code>01_Expr_09</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลเวลา**](#รูปแบบข้อมูลเวลา)
-   [**การแปลงข้อความและเวลา**](#การแปลงข้อความและเวลา)
-   [**การแปลงระหว่างเวลาและวินาที**](#การแปลงระหว่างเวลาและวินาที)
-   [**การหาช่วงเวลา**](#การหาช่วงเวลา)
-   [**การทำงานของ `main`**](#การทำงานของ-main)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลเวลา

โจทย์ใช้เวลาในรูปแบบ `HH:MM:SS` เช่น `10:03:29` หมายถึง 10 ชั่วโมง
3 นาที 29 วินาที แนวคิดของโปรแกรมคือแปลงข้อมูลไปตามลำดับ

`"10:03:29"` → `(10, 3, 29)` → `36209` วินาที

เมื่อหาผลต่างเสร็จแล้วจึงแปลงย้อนกลับจากจำนวนวินาทีเป็น tuple และข้อความ
`HH:MM:SS` สำหรับแสดงผล ค่าคงที่ `60`, `3600` และ `86400` แทนจำนวนวินาที
ในหนึ่งนาที หนึ่งชั่วโมง และหนึ่งวันตามลำดับ

---

## การแปลงข้อความและเวลา

ฟังก์ชัน `str2hms(hms_str)` ใช้ `hms_str.split(":")` แยกข้อความตรง
เครื่องหมาย `:` แล้วกระจายสมาชิกสามตัวให้ `h`, `m` และ `s` ค่าที่ได้จาก
`split` ยังเป็น string จึงต้องแปลงด้วย `int()` ก่อนคืน tuple

```python
h, m, s = "10:03:29".split(":")
# h, m, s คือ "10", "03", "29"
```

ผลของ `str2hms("10:03:29")` จึงเป็น `(10, 3, 29)`

ฟังก์ชัน `hms2str(h, m, s)` ทำงานย้อนกลับ โดยเติม `0` ด้านหน้าแต่ละค่า
ด้วย f-string แล้วเลือกสองตัวท้ายด้วย `[-2:]`

-   `f"0{3}"[-2:]` ได้ `"03"`
-   `f"0{10}"[-2:]` ได้ `"10"`

จากนั้น `f"{h_str}:{m_str}:{s_str}"` เชื่อมทั้งสามส่วนเป็น `HH:MM:SS`

> [!NOTE]
>
> `hms2str` และวิธี `f"0{h}"[-2:]` ตั้งใจใช้กับ `h`, `m` และ `s`
> ที่ต้องแสดงสองหลักเท่านั้น หากส่งค่าที่เกินสองหลัก เช่น `123` จะเหลือเพียง
> `"23"`

---

## การแปลงระหว่างเวลาและวินาที

การเปรียบเทียบเวลาทำได้ง่ายเมื่อแปลงทุกค่าเป็นจำนวนวินาทีตั้งแต่เที่ยงคืน
ฟังก์ชัน `to_sec(h, m, s)` ใช้สูตร

$$
t=3600h+60m+s
$$

ซึ่งตรงกับ Python expression
`(h * SECONDS_IN_HOUR) + (m * SECONDS_IN_MIN) + s` ตัวอย่างเช่น
`to_sec(10, 3, 29)` ได้ `36209`

ส่วน `to_hms(s)` ใช้การหารเอาส่วน (`//`) และหาเศษ (`%`) เพื่อแยกวินาที
ทั้งหมดกลับเป็นแต่ละหน่วย ถ้าให้จำนวนวินาทีเริ่มต้นเป็น $T$

$$
h=\left\lfloor\frac{T}{3600}\right\rfloor,
\qquad r=T\bmod 3600
$$

$$
m=\left\lfloor\frac{r}{60}\right\rfloor,
\qquad s=r\bmod 60
$$

คำสั่ง Python ที่ทำงานตรงกับสูตรคือ

```python
h = s // SECONDS_IN_HOUR
s %= SECONDS_IN_HOUR
m = s // SECONDS_IN_MIN
s %= SECONDS_IN_MIN
```

ตัวแปร `s` ถูกเปลี่ยนให้เก็บเศษที่เหลือในแต่ละขั้น ดังนั้น
`to_hms(36209)` จะคืน `(10, 3, 29)`

---

## การหาช่วงเวลา

ฟังก์ชัน `diff` แปลงเวลาเริ่มต้นและเวลาสิ้นสุดเป็น `t1` และ `t2` ก่อน
แล้วหาช่วงเวลาเป็นวินาทีด้วย

$$
dt=(86400+t_2-t_1)\bmod 86400
$$

ซึ่งตรงกับ `(SECONDS_IN_DAY + t2 - t1) % SECONDS_IN_DAY`
จากนั้น `to_hms(dt)` จะแปลงผลต่างกลับเป็นชั่วโมง นาที และวินาที

PDF รับประกันว่าเวลาเริ่มต้นไม่เกินเวลาสิ้นสุด จึงมองได้ว่า $dt=t_2-t_1$
โดยตรง อย่างไรก็ตาม การบวกหนึ่งวันแล้วใช้ `%` ทำให้โค้ดรองรับกรณีข้ามเที่ยงคืน
หนึ่งครั้งด้วย เช่น ช่วงจาก `23:50:50` ถึง `02:01:01` จะได้ `02:10:11`

---

## การทำงานของ `main`

`main()` อ่านเวลาเริ่มต้นและเวลาสิ้นสุดอย่างละหนึ่งบรรทัด แล้วทำงานตามลำดับ

1. ใช้ `str2hms` แปลงข้อความทั้งสองเป็นตัวเลข
2. ใช้ `diff` หาช่วงเวลา
3. ใช้ `hms2str` จัดรูปแบบผลลัพธ์เป็น `HH:MM:SS`
4. แสดงผลด้วย `print`

บรรทัด `exec(input())` มีไว้ให้ grader ส่งคำสั่ง Python ที่ต้องการทดสอบ
เช่น ถ้าส่งข้อมูลดังนี้

```text
main()
10:57:57
12:00:00
```

`exec(input())` จะอ่านและเรียก `main()` จากบรรทัดแรก จากนั้น `main()`
อ่านเวลาอีกสองบรรทัดและแสดง `01:02:03`

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ได้ จึงควรคงบรรทัดนี้ไว้สำหรับ grader
> และใช้เฉพาะกับคำสั่งที่เชื่อถือได้ ไม่ควรนำ `exec(input())` ไปใช้รับข้อมูล
> จากผู้ใช้ทั่วไป

---

# Solution

```python
# --------------------------------------------------
# File Name : 01_Expr_09.py
# Problem   : Duration (Function)
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# Constants
SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400


# Convert a string in the format HH:MM:SS to 3 integers h, m, s
def str2hms(hms_str):
    h, m, s = hms_str.split(":")
    return int(h), int(m), int(s)


# Convert 3 integers h, m, s to a string in the format HH:MM:SS
def hms2str(h, m, s):
    h_str = f"0{h}"[-2:]  # Add hours with leading zero if needed
    m_str = f"0{m}"[-2:]  # Add minutes with leading zero if needed
    s_str = f"0{s}"[-2:]  # Add seconds with leading zero if needed
    return f"{h_str}:{m_str}:{s_str}"


# Calculate total seconds from hours, minutes, and seconds
def to_sec(h, m, s):
    return (h * SECONDS_IN_HOUR) + (m * SECONDS_IN_MIN) + s


# Convert total seconds to hours, minutes, and seconds
def to_hms(s):
    h = s // SECONDS_IN_HOUR
    s %= SECONDS_IN_HOUR
    m = s // SECONDS_IN_MIN
    s %= SECONDS_IN_MIN
    return h, m, s


# Calculate the difference between two times given in hours, minutes, and seconds
def diff(h1, m1, s1, h2, m2, s2):
    # Convert both times to total seconds
    t1 = to_sec(h1, m1, s1)
    t2 = to_sec(h2, m2, s2)

    # Calculate the difference in seconds
    dt = (SECONDS_IN_DAY + t2 - t1) % SECONDS_IN_DAY

    # Convert the difference back to hours, minutes, and seconds
    return to_hms(dt)


# Main function to read input times, calculate the difference, and print the result
def main():
    # Read input times in the format HH:MM:SS
    hms_start = input()
    hms_end = input()

    # Convert input strings to hours, minutes, and seconds
    h1, m1, s1 = str2hms(hms_start)
    h2, m2, s2 = str2hms(hms_end)

    # Calculate the difference and convert it to a string
    dh, dm, ds = diff(h1, m1, s1, h2, m2, s2)

    # Convert the difference to a string in the format HH:MM:SS
    time = hms2str(dh, dm, ds)
    print(time)


# Execute the input string as code
exec(input())
```
