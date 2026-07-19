<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Color Splash ★★☆ (
      <a href="https://drive.google.com/file/d/1Y3ZGwib7W2vyC9boj5bUja5Bn7x4YKRV/view?usp=sharing">
        <code>2565_1_Q2_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การอ่านข้อมูลจากไฟล์**](#การอ่านข้อมูลจากไฟล์)
-   [**การค้นหาและใส่แท็กสี**](#การค้นหาและใส่แท็กสี)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวังเรื่องตำแหน่งค้นหาและช่องว่าง**](#ข้อควรระวังเรื่องตำแหน่งค้นหาและช่องว่าง)
-   [**Solution**](#solution)

---

## การอ่านข้อมูลจากไฟล์

โจทย์รับชื่อไฟล์ 2 บรรทัดตามลำดับ บรรทัดแรกเป็นชื่อไฟล์เก็บชื่อสี และ
บรรทัดที่สองเป็นชื่อไฟล์เก็บข้อความ

```python
color_filename = input().strip()
text_filename = input().strip()
```

การใช้ `.strip()` ตัดช่องว่างและอักขระขึ้นบรรทัดใหม่ที่อาจติดอยู่รอบชื่อไฟล์
จากนั้นโปรแกรมเปิดแต่ละไฟล์ด้วย `with open(...) as file:` เมื่อทำงานในบล็อก
`with` เสร็จ Python จะปิดไฟล์ให้อัตโนมัติ

ไฟล์สีอาจมีหลายบรรทัดและแต่ละบรรทัดอาจมีหลายสี โปรแกรมจึงใช้ `.split()`
แยกทุกบรรทัดตามช่องว่าง แล้วเก็บชื่อสีทั้งหมดต่อกันในลิสต์ `colors`

```python
for line in file:
    for color in line.strip().split():
        colors.append(color.lower())
```

ชื่อสีในไฟล์อาจเป็นตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่ การใช้ `color.lower()` ทำให้
ทุกชื่อที่เก็บไว้เป็นตัวพิมพ์เล็ก เช่น `GREEN` จะถูกเก็บเป็น `"green"`
รูปแบบแท็กที่สร้างในภายหลังจึงใช้ชื่อสีตัวพิมพ์เล็กเสมอ

ส่วนไฟล์ข้อความถูกอ่านตามลำดับบรรทัดและต่อเก็บไว้ในสตริง `text`

```python
for line in file:
    text += line.strip() + "\n"
```

การเติม `"\n"` หลังทุกบรรทัดทำให้ลำดับบรรทัดและบรรทัดว่างภายในข้อความ
ยังคงอยู่ ส่วนผลของ `.strip()` ต่อช่องว่างจะอธิบายเพิ่มเติมในหัวข้อท้าย

## การค้นหาและใส่แท็กสี

ฟังก์ชัน `mark_color(text, color)` ทำหน้าที่ค้นหาสีชนิดหนึ่งทุกตำแหน่งใน
ข้อความ แล้วครอบสตริงย่อยที่พบด้วยรูปแบบแท็กของโจทย์

ถ้าพบข้อความเดิม `current_color` ซึ่งเมื่อแปลงเป็นตัวพิมพ์เล็กแล้วเท่ากับ
`color` ผลลัพธ์ที่ต้องสร้างคือ

```text
<color>current_color</>
```

ในภาษา Python เขียนการประกอบข้อความได้เป็น

```python
f"<{color}>{current_color}</>"
```

`color` เป็นตัวพิมพ์เล็กจากขั้นตอนอ่านไฟล์ แต่ `current_color` เป็นชิ้นส่วน
ที่ตัดจากข้อความต้นฉบับ จึงยังรักษารูปแบบตัวพิมพ์เดิมไว้ เช่น `WHITE`
จะเปลี่ยนเป็น `<white>WHITE</>`

การค้นหาใช้คำสั่ง

```python
start_idx = result.lower().find(color, start_find_idx)
```

`result.lower()` ทำให้ค้นหาโดยไม่สนใจตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่ แต่ไม่ได้
เปลี่ยนค่าใน `result` จริง เมื่อตัด `result[start_idx:end_idx]` จึงยังได้
ข้อความที่มีตัวพิมพ์เหมือนเดิม หาก `.find()` คืน `-1` แสดงว่าไม่พบสีนี้แล้ว
และจบการวนซ้ำ

เมื่อพบสี โปรแกรมแบ่งข้อความออกเป็น 3 ส่วน

```python
before_color = result[:start_idx]
current_color = result[start_idx:end_idx]
after_color = result[end_idx:]
```

แล้วนำส่วนก่อนหน้า แท็กพร้อมข้อความสี และส่วนหลังมาต่อกันใหม่ หลังแทรกแท็ก
ความยาวของ `result` จะเพิ่มขึ้น จึงต้องเลื่อนตำแหน่งเริ่มค้นหาครั้งถัดไปให้พ้น
ข้อความที่เพิ่งครอบไว้

```python
start_find_idx = end_idx + len(f"<{color}></>")
```

`f"<{color}></>"` แทนจำนวนอักขระของแท็กเปิดและแท็กปิดที่เพิ่มเข้ามา
การขยับตำแหน่งเช่นนี้ป้องกันไม่ให้ `.find()` กลับไปพบชื่อสีในแท็กเปิด หรือ
พบข้อความสีเดิมซ้ำอีกครั้ง การค้นหาจึงเดินจากซ้ายไปขวาและครอบแต่ละตำแหน่ง
เพียงครั้งเดียว

การค้นหาเป็นแบบ **สตริงย่อย** ไม่ได้ตรวจขอบเขตของคำ เช่น `blue` ใน
`Darkblue` และ `pink` ใน `pinky` ก็ถือว่าเป็นสีที่ต้องครอบแท็ก

## ลำดับการทำงาน

1. รับชื่อไฟล์สีและชื่อไฟล์ข้อความตามลำดับ
2. อ่านชื่อสีทุกคำ แปลงเป็นตัวพิมพ์เล็ก แล้วเก็บใน `colors`
3. อ่านข้อความทุกบรรทัดมาต่อเป็นสตริง `text`
4. วนทีละ `color` และเรียก `mark_color(text, color)`
5. ใน `mark_color()` ค้นหาสีจากซ้ายไปขวา ครอบแท็ก และเลื่อนตำแหน่งค้นหา
6. นำผลจากสีปัจจุบันกลับไปเก็บใน `text` ก่อนเริ่มค้นหาสีถัดไป
7. แสดงข้อความสุดท้ายด้วย `print(text.strip())`

โจทย์รับประกันว่าไม่มีชื่อสีใดเป็นสตริงย่อยของชื่อสีอื่น เงื่อนไขนี้ช่วยให้
การทำงานทีละสีไม่เข้าไปครอบบางส่วนของชื่อสีหรือแท็กที่สร้างจากสีก่อนหน้า

## ตัวอย่างการทำงาน

สมมติว่าส่วนหนึ่งของไฟล์สีมีข้อมูลดังนี้

```
White red
orange pink blue GREEN
Purple yellow
```

และไฟล์ข้อความมีข้อมูลดังนี้

```
Orange, yellow and pinky.
Darkblue, purple and green.

I like WHITE. I like Red.
What's your favorite color?
```

โปรแกรมจะแสดงผล

```
<orange>Orange</>, <yellow>yellow</> and <pink>pink</>y.
Dark<blue>blue</>, <purple>purple</> and <green>green</>.

I like <white>WHITE</>. I like <red>Red</>.
What's your favorite color?
```

จากตัวอย่างจะเห็นว่าเครื่องหมายวรรคตอนยังอยู่ตำแหน่งเดิม `WHITE` และ `Red`
ถูกค้นพบแม้รูปแบบตัวพิมพ์ต่างจากชื่อสี และสีที่เป็นเพียงส่วนหนึ่งของคำก็ถูก
ครอบเฉพาะสตริงย่อยที่ตรงกัน หากข้อความไม่มีสีใดเลย ข้อความจะไม่ถูกเพิ่มแท็ก

## ข้อควรระวังเรื่องตำแหน่งค้นหาและช่องว่าง

แท็ก `<color>ข้อความ</>` เป็นรูปแบบที่โจทย์กำหนด โดยแท็กปิดคือ `</>` ไม่ใช่
แท็กปิด HTML แบบทั่วไป แม้คอมเมนต์ในโค้ดจะเรียกว่า HTML tag ก็ตาม จึงต้อง
สร้างข้อความตามรูปแบบนี้อย่างตรงไปตรงมา

การอ่านและแสดงข้อความของโค้ดนี้มีการใช้ `.strip()` สองระดับ

-   `line.strip()` ตัดช่องว่างหัวบรรทัดและท้ายบรรทัดของทุกบรรทัดก่อนนำมาต่อกัน
-   บรรทัดว่างที่อยู่ระหว่างข้อความยังคงเป็น `"\n"` และรักษาตำแหน่งไว้
-   `text.strip()` ก่อนแสดงผลตัดช่องว่างและบรรทัดว่างที่อยู่ก่อนข้อความแรกหรือ
    หลังข้อความสุดท้าย
-   `print()` เติมอักขระขึ้นบรรทัดใหม่หลังผลลัพธ์สุดท้ายตามปกติ

> [!NOTE]
>
> ดังนั้นโปรแกรมรักษาข้อความและช่องว่างที่อยู่ภายในแต่ละบรรทัด แต่ไม่ได้รักษา
> ช่องว่างที่หัวหรือท้ายบรรทัดแบบ byte-for-byte พฤติกรรมนี้ไม่มีผลต่อตัวอย่าง
> ในเอกสารโจทย์ แต่เป็นพฤติกรรมจริงของโค้ดที่ควรทราบ

โจทย์ข้อนี้ไม่มีการคำนวณตัวเลขหรือการปัดเศษ ผลลัพธ์ทั้งหมดเกิดจากการค้นหา
ตำแหน่ง ตัดสตริง และต่อสตริงกลับเข้าด้วยกัน

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_1_Q2_03.py
# Problem   : Color Splash
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input the color file and text file names
color_filename = input().strip()
text_filename = input().strip()

# Read the colors from the file and store them in a list
colors = []
with open(color_filename) as file:
    for line in file:
        for color in line.strip().split():
            colors.append(color.lower())

# Read the text from the file and store it in a string
text = ""
with open(text_filename) as file:
    for line in file:
        text += line.strip() + "\n"


# Mark HTML tags around the colors in the text
def mark_color(text, color):
    # Initialize the result with the original text
    result = text
    start_find_idx = 0
    while True:
        start_idx = result.lower().find(color, start_find_idx)
        end_idx = start_idx + len(color)
        if start_idx == -1:
            break

        before_color = result[:start_idx]
        current_color = result[start_idx:end_idx]
        after_color = result[end_idx:]
        result = f"{before_color}<{color}>{current_color}</>{after_color}"

        start_find_idx = end_idx + len(f"<{color}></>")
    return result


# Apply the color marking function for every color in the list
for color in colors:
    text = mark_color(text, color)
# Output the modified text with colors marked
print(text.strip())
```
