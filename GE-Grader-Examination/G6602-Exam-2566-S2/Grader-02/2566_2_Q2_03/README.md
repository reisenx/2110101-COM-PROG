<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Text Formatter ★★★ (
      <a href="https://drive.google.com/file/d/1ftesAF-xHat6QuRv99XYFy8gNnVN-qKJ/view?usp=sharing">
        <code>2566_2_Q2_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โจทย์ต้องการอะไร**](#โจทย์ต้องการอะไร)
-   [**แนวคิดในการแก้ปัญหา**](#แนวคิดในการแก้ปัญหา)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

# โจทย์ต้องการอะไร

โปรแกรมรับชื่อแฟ้มข้อความ 1 บรรทัด ภายในแฟ้มมีคำที่ประกอบด้วยตัวอักษรอังกฤษและตัวเลข โดยใช้ `_` คั่นคำ อาจมีหลายบรรทัดและมีบรรทัดว่างได้ แต่ไม่มีคำใดถูกแบ่งข้ามบรรทัดและแต่ละคำยาวไม่เกิน 50 ตัวอักษร

งานของเราคือรวมคำจากทุกบรรทัดให้เป็นลำดับเดียวโดยรักษาลำดับเดิม แล้วจัดบรรทัดใหม่ให้แต่ละบรรทัดมีคำต่อเนื่องมากที่สุดเท่าที่ใส่ได้ โดยมีอักขระรวมไม่เกิน 50 ตัว คำในผลลัพธ์ยังคั่นด้วย `_` และต้องไม่มี `_` ที่ต้นหรือท้ายบรรทัด

ก่อนแสดงข้อความ โปรแกรมต้องพิมพ์ `-` ติดกัน 50 ตัวเป็นบรรทัดแรกเสมอ

# แนวคิดในการแก้ปัญหา

## 1. อ่านแฟ้มและรวมคำเป็นลิสต์เดียว

คำสั่ง `with open(filename) as file:` เปิดแฟ้มให้อ่าน และช่วยปิดแฟ้มให้อัตโนมัติเมื่อออกจากบล็อก `with` โปรแกรมอ่านทีละบรรทัด ข้ามบรรทัดว่าง แล้วแยกคำด้วย `_`

```python
if line.strip() != "":
    words += line.strip().split("_")
```

`.strip()` นำรหัสขึ้นบรรทัดใหม่ออก ส่วน `.split("_")` คืนลิสต์คำ การต่อเข้ากับ `words` ตามลำดับทำให้เส้นแบ่งบรรทัดเดิมหายไป แต่ลำดับของทุกคำยังเหมือนเดิม

## 2. นับความยาวรวมทั้งเครื่องหมายคั่นคำ

ถ้าบรรทัดหนึ่งมีคำ $k$ คำ ความยาวบรรทัดคือ

$$
\sum_{i=1}^{k}\operatorname{len}(w_i) + (k-1)
$$

พจน์ $(k-1)$ คือจำนวน `_` ระหว่างคำ ในโค้ดจึงเริ่ม `length` ด้วยความยาวของคำแรก แล้วทุกครั้งที่ทดลองเพิ่มคำถัดไปจะบวก

```python
length += len(words[end_idx]) + 1
```

ค่า `+ 1` คือ `_` ที่ต้องวางก่อนคำใหม่ หากความยาวใหม่มากกว่า `LENGTH_LIMIT` หรือ 50 จะหยุดและย้ายคำนั้นไปเริ่มบรรทัดถัดไป แต่ถ้าความยาวเท่ากับ 50 พอดียังใส่ได้

## 3. ใช้ดัชนีแบ่งช่วงคำของแต่ละบรรทัด

- `start_idx` ชี้คำแรกของบรรทัดปัจจุบัน
- `end_idx` ชี้ตำแหน่งถัดจากคำสุดท้ายที่ใส่ได้

ลูปด้านในเลื่อน `end_idx` ไปเรื่อย ๆ ขณะที่คำถัดไปยังใส่ได้ เมื่อตัดสินช่วงเสร็จแล้ว

```python
line = "_".join(words[start_idx:end_idx])
```

จะเชื่อมเฉพาะคำในช่วงนั้นด้วย `_` จึงไม่มีเครื่องหมายเกินมาที่ต้นหรือท้ายบรรทัด หลังพิมพ์แล้วกำหนด `start_idx = end_idx` เพื่อเริ่มบรรทัดใหม่จากคำที่ยังไม่ได้ใช้

# ลำดับการทำงาน

1. อ่านชื่อแฟ้มและเปิดแฟ้มด้วย `with open(...)`
2. อ่านทุกบรรทัด ข้ามบรรทัดว่าง และสะสมคำทั้งหมดไว้ใน `words`
3. พิมพ์ `"-" * LENGTH_LIMIT` เป็นเส้นยาว 50 ตัว
4. เริ่มบรรทัดที่คำตำแหน่ง `start_idx`
5. ทดลองเพิ่มคำถัดไปพร้อมนับ `_` จนคำต่อไปจะทำให้ยาวเกิน 50
6. ใช้ `"_".join(...)` สร้างและพิมพ์บรรทัดนั้น
7. เลื่อน `start_idx` แล้วทำซ้ำจนใช้คำครบ

# ตัวอย่างการทำงาน

สมมติแฟ้มมีข้อความ

```text
Mary_had_a_little_lamb
little_lamb_little_lamb
Mary_had_a_little_lamb
its_fleece_was_white
as_snow
```

หลังรวมคำแล้ว โปรแกรมเติมคำจากซ้ายไปขวาให้เต็มที่สุดโดยไม่เกิน 50 ตัว จึงได้

```text
--------------------------------------------------
Mary_had_a_little_lamb_little_lamb_little_lamb
Mary_had_a_little_lamb_its_fleece_was_white_as
snow
```

คำ `snow` ไม่สามารถต่อท้ายบรรทัดก่อนหน้าโดยยังอยู่ในขีดจำกัด จึงต้องขึ้นบรรทัดใหม่ ส่วนคำที่ยาว 50 ตัวพอดีสามารถอยู่ลำพังหนึ่งบรรทัดได้

# ข้อควรระวัง

> [!NOTE]
> ต้องนับ `_` ระหว่างคำด้วย เงื่อนไขรับได้เมื่อความยาว **ไม่เกิน** 50 ดังนั้นความยาวเท่ากับ 50 พอดียังอยู่ในบรรทัดเดิม แต่ 51 ต้องขึ้นบรรทัดใหม่

- บรรทัดว่างในแฟ้มถูกข้ามและไม่สร้างบรรทัดว่างในผลลัพธ์
- โจทย์รับประกันว่าคำเดี่ยวยาวไม่เกิน 50 ตัว หากมีคำยาว 50 ตัว คำนั้นจะถูกพิมพ์ได้หนึ่งบรรทัดพอดี
- หากแฟ้มมีแต่บรรทัดว่าง พฤติกรรมของโค้ดคือพิมพ์เฉพาะเส้น `-` 50 ตัว
- โปรแกรมสมมติว่าชื่อแฟ้มถูกต้องและเปิดอ่านได้ตามข้อมูลของระบบตรวจคำตอบ
- การจัดบรรทัดเกี่ยวกับจำนวนอักขระเท่านั้น ไม่มีการคำนวณหรือปัดเศษตัวเลข

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_2_Q2_03.py
# Problem   : Text Formatter
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize the length limit
LENGTH_LIMIT = 50
# Read the filename
filename = input().strip()

# Extract words from the file and store them in a list
words = []
with open(filename) as file:
    for line in file:
        if line.strip() != "":
            words += line.strip().split("_")

# Print the header
print("-" * LENGTH_LIMIT)
# Initialize the start index for the first word
start_idx = 0
# Output the words in lines not exceeding the length limit
while start_idx < len(words):
    # Initialize the end index and current line length
    end_idx = start_idx + 1
    length = len(words[start_idx])
    # Calculate the end index for the current line
    while end_idx < len(words):
        # Calculate the length of the current line if the next word is added
        length += len(words[end_idx]) + 1
        # If the length exceeds the limit, break the loop
        if length > LENGTH_LIMIT:
            break
        # Otherwise, include the next word
        end_idx += 1

    # Output the current line
    line = "_".join(words[start_idx:end_idx])
    print(line)
    # Update the start index for the next iteration
    start_idx = end_idx
```
