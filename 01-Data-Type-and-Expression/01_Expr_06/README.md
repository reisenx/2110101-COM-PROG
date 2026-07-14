<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Duration ★★★ (
      <a href="https://drive.google.com/file/d/1RUw-Y2A58UwI3n-oLprnicoxCePYZkbt/view?usp=drive_link">
        <code>01_Expr_06</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ค่าคงที่และการรวมเวลาเป็นวินาที**](#ค่าคงที่และการรวมเวลาเป็นวินาที)
-   [**ระยะเวลาในรอบ 24 ชั่วโมง**](#ระยะเวลาในรอบ-24-ชั่วโมง)
-   [**แยกวินาทีกลับเป็นชั่วโมง นาที วินาที**](#แยกวินาทีกลับเป็นชั่วโมง-นาที-วินาที)
-   [**ตัวอย่างข้ามเที่ยงคืน**](#ตัวอย่างข้ามเที่ยงคืน)
-   [**รูปแบบผลลัพธ์**](#รูปแบบผลลัพธ์)
-   [**Solution**](#solution)

---

## ค่าคงที่และการรวมเวลาเป็นวินาที

การลบเวลาในรูป `ชั่วโมง:นาที:วินาที` โดยตรงทำให้ต้องคอยยืมนาทีหรือชั่วโมง
วิธีที่ง่ายกว่าคือแปลงเวลาทั้งสองจุดให้เป็นหน่วยเดียวกันก่อน นั่นคือ **วินาที**

โปรแกรมรับจำนวนเต็ม 6 บรรทัดตามลำดับ `h1`, `m1`, `s1`, `h2`, `m2`,
`s2` โดยชั่วโมงอยู่ในช่วง `0` ถึง `23` ส่วนนาทีและวินาทีอยู่ในช่วง `0` ถึง
`59`

โปรแกรมตั้งชื่อค่าที่ใช้ซ้ำด้วยตัวพิมพ์ใหญ่ เพื่อสื่อว่าเป็นค่าคงที่

```python
SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400
```

เมื่อเวลาเริ่มต้นคือ $h_1:m_1:s_1$ และเวลาสิ้นสุดคือ $h_2:m_2:s_2$
จำนวนวินาทีที่นับจาก `00:00:00` คือ

$$
t_1 = 3600h_1 + 60m_1 + s_1,
\qquad
t_2 = 3600h_2 + 60m_2 + s_2
$$

ซึ่งตรงกับ Python ดังนี้

```python
t1 = (h1 * SECONDS_IN_HOUR) + (m1 * SECONDS_IN_MIN) + s1
t2 = (h2 * SECONDS_IN_HOUR) + (m2 * SECONDS_IN_MIN) + s2
```

---

## ระยะเวลาในรอบ 24 ชั่วโมง

ถ้าเวลาสิ้นสุดอยู่หลังเวลาเริ่มต้นในวันเดียวกัน ค่า `t2 - t1` จะเป็นบวก
แต่ถ้าช่วงเวลาข้ามเที่ยงคืน ค่านี้จะเป็นลบ จึงคำนวณระยะเวลาในวงรอบหนึ่งวันด้วย

$$
dt = (86400 + t_2 - t_1) \bmod 86400
$$

ใน Python เครื่องหมาย modulo คือ `%`

```python
dt = (SECONDS_IN_DAY + t2 - t1) % SECONDS_IN_DAY
```

การบวกหนึ่งวันก่อนหาเศษทำให้กรณีข้ามเที่ยงคืนกลับมาเป็นระยะเวลาบวก
ส่วน `% 86400` ทำให้คำตอบอยู่ในช่วง `0` ถึง `86399` วินาทีเสมอ

> [!NOTE]
>
> ถ้าเวลาเริ่มต้นและเวลาสิ้นสุดเท่ากัน สูตรนี้ให้ `dt = 0` และแสดงผล
> `0:0:0` ไม่ได้ตีความว่าเวลาผ่านไปครบ 24 ชั่วโมง

---

## แยกวินาทีกลับเป็นชั่วโมง นาที วินาที

ตัวดำเนินการ `//` ให้ผลหารจำนวนเต็ม ส่วน `%` ให้เศษจากการหาร จึงใช้ทั้งคู่
เพื่อแกะ `dt` กลับเป็นสามหน่วยได้

$$
\begin{aligned}
dh &= \left\lfloor \frac{dt}{3600} \right\rfloor,
& r_h &= dt \bmod 3600 \\
dm &= \left\lfloor \frac{r_h}{60} \right\rfloor,
& ds &= r_h \bmod 60
\end{aligned}
$$

ใน solution ใช้ตัวแปร `dt` ซ้ำเพื่อเก็บเศษที่ยังไม่ได้แยก

```python
dh = dt // SECONDS_IN_HOUR
dt %= SECONDS_IN_HOUR
dm = dt // SECONDS_IN_MIN
dt %= SECONDS_IN_MIN
ds = dt
```

หลัง `dt %= SECONDS_IN_HOUR` ตัวแปร `dt` เหลือเฉพาะส่วนที่ไม่ครบชั่วโมง
และหลัง `dt %= SECONDS_IN_MIN` จะเหลือวินาทีสุดท้ายพอดี
คำสั่ง `dt %= value` เป็นรูปย่อของ `dt = dt % value`

---

## ตัวอย่างข้ามเที่ยงคืน

ให้เวลาเริ่มต้นเป็น `19:00:00` และเวลาสิ้นสุดเป็น `18:10:10` ของวันถัดไป

$$
\begin{aligned}
t_1 &= 19(3600) = 68400 \\
t_2 &= 18(3600) + 10(60) + 10 = 65410 \\
dt &= (86400 + 65410 - 68400) \bmod 86400 = 83410
\end{aligned}
$$

และ $83410 = 23(3600) + 10(60) + 10$ ดังนั้นระยะเวลาคือ
`23:10:10`

---

## รูปแบบผลลัพธ์

คำตอบต้องอยู่ในรูป `ชั่วโมง:นาที:วินาที` จึงใช้ f-string เชื่อมตัวเลขด้วย `:`

```python
print(f"{dh}:{dm}:{ds}")
```

โจทย์ไม่ต้องการเติมเลขศูนย์ด้านหน้า เช่น หนึ่งชั่วโมง สองนาที สามวินาที
ต้องแสดงเป็น `1:2:3` ไม่ใช่ `01:02:03`

---

# Solution

```python
# --------------------------------------------------
# File Name : 01_Expr_06.py
# Problem   : Duration
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Constants
SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

# Input the initial time in the format h1 : m1 : s1
h1 = int(input())
m1 = int(input())
s1 = int(input())

# Input the final time in the format h2 : m2 : s2
h2 = int(input())
m2 = int(input())
s2 = int(input())

# Convert the initial time and final time into seconds
t1 = (h1 * SECONDS_IN_HOUR) + (m1 * SECONDS_IN_MIN) + s1
t2 = (h2 * SECONDS_IN_HOUR) + (m2 * SECONDS_IN_MIN) + s2

# Calculate the duration in seconds
# Ensure that the duration is always positive by using modulo operation
dt = (SECONDS_IN_DAY + t2 - t1) % SECONDS_IN_DAY

# Convert the duration in seconds to hours, minutes, and seconds
dh = dt // SECONDS_IN_HOUR
dt %= SECONDS_IN_HOUR
dm = dt // SECONDS_IN_MIN
dt %= SECONDS_IN_MIN
ds = dt

# Output
print(f"{dh}:{dm}:{ds}")
```
