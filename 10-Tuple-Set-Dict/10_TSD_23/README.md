<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Genre Total Playtime ★★ (
      <a href="https://drive.google.com/file/d/1IkcX66v3vl9U20yYVMldH4gmyXqXDxpI/view?usp=drive_link">
        <code>10_TSD_23</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของโจทย์**](#แนวคิดของโจทย์)
-   [**การแปลงเวลา**](#การแปลงเวลา)
-   [**การสะสมและจัดอันดับ**](#การสะสมและจัดอันดับ)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

## แนวคิดของโจทย์

ข้อมูลเพลงแต่ละบรรทัดประกอบด้วยชื่อเพลง ชื่อนักร้อง ประเภทเพลง และเวลา
โดยคั่นแต่ละส่วนด้วย `", "` โจทย์ต้องการรวมเวลาของเพลงที่มีประเภทเดียวกัน
แล้วแสดงไม่เกิน 3 ประเภทที่มีเวลารวมมากที่สุด

โครงสร้างข้อมูลที่เหมาะกับการสะสมผลรวมคือ dictionary โดยกำหนดให้

-   key คือชื่อประเภทเพลง เช่น `"Rock"`
-   value คือเวลารวมของประเภทนั้นในหน่วยวินาที

ตัวอย่างเช่น dictionary

```python
genre_playtime = {"Rock": 924, "Pop": 885}
```

หมายความว่าเพลง Rock มีเวลารวม `924` วินาที และเพลง Pop มีเวลารวม `885`
วินาที การเก็บเวลาเป็นจำนวนเต็มหน่วยวินาทีทำให้บวกและเปรียบเทียบเวลาได้โดยตรง
โดยไม่ต้องจัดการข้อความรูปแบบ `นาที:วินาที` ระหว่างคำนวณ

## การแปลงเวลา

### จากนาทีและวินาทีเป็นวินาทีทั้งหมด

ถ้าเวลาอยู่ในรูป `m:s` เวลารวมเป็นวินาทีคำนวณได้จาก

$$
\text{วินาทีทั้งหมด} = (60 \times m) + s
$$

ซึ่งตรงกับนิพจน์ Python `m * SECONDS_IN_MIN + s` ในฟังก์ชัน
`to_seconds()`

```python
def to_seconds(time):
    m, s = [int(num) for num in time.split(":")]
    return (m * SECONDS_IN_MIN) + s
```

เช่น `"6:30"` ถูกแยกเป็น `m = 6` และ `s = 30` จึงได้
`6 * 60 + 30 = 390` วินาที

### จากวินาทีทั้งหมดกลับเป็นนาทีและวินาที

เมื่อต้องแสดงผล เราแปลงวินาทีทั้งหมดกลับด้วย

$$
m = \text{seconds} \mathbin{//} 60
\qquad\text{และ}\qquad
s = \text{seconds} \bmod 60
$$

ใน Python ใช้ `seconds // SECONDS_IN_MIN` หาจำนวนนาที และใช้
`seconds % SECONDS_IN_MIN` หาวินาทีส่วนที่เหลือ ฟังก์ชัน `to_time()` เติม `0`
ด้านหน้าส่วนวินาทีแล้วเลือกสองตัวท้าย จึงแสดง `5` วินาทีเป็น `05` เช่น
`725` วินาทีจะแสดงเป็น `12:05` ส่วนจำนวนนาทีไม่ถูกเติมศูนย์ด้านหน้า

## การสะสมและจัดอันดับ

โปรแกรมวนรับข้อมูลเพลง `n` บรรทัด แต่ละบรรทัดถูกแยกด้วย
`split(", ")` แล้วเลือกสองช่องท้ายเสมอ

```python
data = input().strip().split(", ")
genre = data[-2]
time = to_seconds(data[-1])
```

ดังนั้น `data[-2]` คือประเภทเพลง และ `data[-1]` คือเวลา จากนั้นถ้ายังไม่มี
ประเภทเพลงนั้นใน `genre_playtime` โปรแกรมสร้างค่าเริ่มต้นเป็น `0`
แล้วบวกเวลาของเพลงปัจจุบันเข้าไป

การเรียงต้องการเวลาจากมากไปน้อย แต่ `list.sort()` เรียงตัวเลขจากน้อยไปมาก
โดยปริยาย โค้ดจึงเก็บ tuple `(-total_time, genre)` กล่าวคือเปลี่ยนเวลารวมให้เป็น
จำนวนลบก่อนเรียง เวลาที่มากกว่าจะกลายเป็นจำนวนลบที่น้อยกว่าและอยู่ด้านหน้า

```python
sorted_genre_playtime.append((-total_time, genre))
sorted_genre_playtime.sort()
```

เมื่อจะแสดงผลจึงใช้ `-total_time` เปลี่ยนค่ากลับเป็นบวก แล้วเลือกเพียง
`sorted_genre_playtime[:DISPLAY_LIMIT]` ซึ่งมีได้มากที่สุด 3 รายการ

> [!NOTE]
>
> โจทย์รับประกันว่าเวลารวมของแต่ละประเภทไม่เท่ากัน จึงตัดสินอันดับจากเวลาได้
> แน่นอน หากทดลองด้วยข้อมูลนอกเงื่อนไขที่เวลารวมเท่ากัน tuple จะใช้ชื่อประเภท
> เพลงเป็นเกณฑ์รองและเรียงตามลำดับพจนานุกรม

## ตัวอย่างการทำงาน

เพลง Rock ในตัวอย่างมีเวลา `6:30`, `2:59` และ `5:55` โปรแกรมจะแปลงเป็น

```text
6:30  -> 390 วินาที
2:59  -> 179 วินาที
5:55  -> 355 วินาที
```

จึงได้เวลารวม `390 + 179 + 355 = 924` วินาที และแปลงกลับเป็น
`924 // 60 = 15` นาที กับ `924 % 60 = 24` วินาที ผลลัพธ์ของประเภทนี้คือ

```text
Rock --> 15:24
```

หลังทำแบบเดียวกันครบทุกประเภท โปรแกรมจะเรียงได้ Rock, Pop และ Country
เป็นสามอันดับแรกตามเวลารวม

## ข้อควรระวัง

-   รูปแบบข้อมูลใช้เครื่องหมายจุลภาคตามด้วยช่องว่างหนึ่งช่อง เพราะโค้ดแยกด้วย
    `split(", ")`
-   ไม่มีการปัดเศษเวลา การคำนวณทั้งหมดใช้จำนวนเต็มหน่วยวินาที
-   ถ้ามีประเภทเพลงเพียง 1 หรือ 2 ประเภท การ slice `[:3]` จะคืนเท่าที่มี
    โปรแกรมจึงไม่พิมพ์บรรทัดเกินจริง
-   เพลงประเภทเดียวกันกี่เพลงก็สะสมอยู่ใน key เดียว จึงไม่เกิดประเภทซ้ำในผลลัพธ์

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_23.py
# Problem   : Genre Total Playtime
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

SECONDS_IN_MIN = 60
DISPLAY_LIMIT = 3


# Convert time string in MM:SS format to total seconds.
def to_seconds(time):
    m, s = [int(num) for num in time.split(":")]
    return (m * SECONDS_IN_MIN) + s


# Convert total seconds to time string in MM:SS format.
def to_time(seconds):
    m = str(seconds // SECONDS_IN_MIN)
    s = f"0{str(seconds % SECONDS_IN_MIN)}"[-2:]
    return f"{m}:{s}"


# Initialize a dictionary to store total playtime for each genre.
genre_playtime = {}

# Input number of entries.
n = int(input())

# Process each entry.
for _ in range(n):
    data = input().strip().split(", ")
    genre = data[-2]
    time = to_seconds(data[-1])

    # Add the playtime to the corresponding genre.
    if genre not in genre_playtime:
        genre_playtime[genre] = 0
    genre_playtime[genre] += time

# Sort genres by total playtime in descending order.
sorted_genre_playtime = []
for genre, total_time in genre_playtime.items():
    sorted_genre_playtime.append((-total_time, genre))
sorted_genre_playtime.sort()

# Output the top 3 genres with the longest total playtime.
for total_time, genre in sorted_genre_playtime[:DISPLAY_LIMIT]:
    print(f"{genre} --> {to_time(-total_time)}")
```
