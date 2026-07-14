<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Search Engine ★★ (
      <a href="https://drive.google.com/file/d/1QUqzKH_17u-sY_sTCGyMRoe2W_uh2dC9/view?usp=drive_link">
        <code>P3_07_Search</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**คะแนนความเกี่ยวข้อง**](#คะแนนความเกี่ยวข้อง)
-   [**การเก็บคะแนนของแต่ละเอกสาร**](#การเก็บคะแนนของแต่ละเอกสาร)
-   [**การรับข้อมูลเอกสาร**](#การรับข้อมูลเอกสาร)
-   [**การค้นหาเอกสารที่ดีที่สุด**](#การค้นหาเอกสารที่ดีที่สุด)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**Solution**](#solution)

---

## คะแนนความเกี่ยวข้อง

โจทย์ไม่ได้เลือกเอกสารจากจำนวนครั้งที่พบคำเพียงอย่างเดียว
แต่พิจารณาทั้ง **ความถี่ของคำ** และ **ความจำเพาะของคำในเอกสาร**

ให้

-   `c(w)` เป็นจำนวนครั้งที่คำ `w` ปรากฏในเอกสาร
-   `T` เป็นจำนวนคำทั้งหมดในเอกสาร
-   `U` เป็นจำนวนคำที่ไม่ซ้ำกันในเอกสาร

คะแนนความเกี่ยวข้องของคำ `w` คือ

$$
S(w) = \frac{c(w)}{T} \times \frac{1}{U}
$$

ซึ่งตรงกับนิพจน์ภาษา Python ดังนี้

```python
(count / total_words) * (1 / total_unique_words)
```

ตัวอย่างเช่น เอกสาร `PPAP` มีคำ `APPLE` จำนวน `1` ครั้ง จากคำทั้งหมด
`11` คำ และมีคำไม่ซ้ำ `8` คำ จึงได้คะแนน

$$
\frac{1}{11} \times \frac{1}{8} \approx 0.0113636
$$

ส่วนเอกสาร `MYAPPLE` มี `APPLE` จำนวน `2` ครั้ง จากคำทั้งหมด `7` คำ
และมีคำไม่ซ้ำ `6` คำ จึงได้คะแนน

$$
\frac{2}{7} \times \frac{1}{6} \approx 0.047619
$$

ดังนั้น เมื่อค้นหา `APPLE` โปรแกรมจึงเลือก `MYAPPLE`
คะแนนเหล่านี้ใช้เปรียบเทียบภายในโปรแกรมเท่านั้น ไม่ต้องปัดเศษหรือแสดงออกทางหน้าจอ

> [!NOTE]
>
> โปรแกรมแบ่งข้อความด้วย `split()` แล้วเปรียบเทียบคำทั้งคำ
> ดังนั้น `APPLE` กับ `PINEAPPLE` เป็นคนละคำ แม้ `PINEAPPLE`
> จะมีตัวอักษร `APPLE` อยู่ข้างในก็ตาม

---

## การเก็บคะแนนของแต่ละเอกสาร

ฟังก์ชัน `calculate_relatable_scores()` เริ่มจากนับจำนวนครั้งของทุกคำด้วย
dictionary ชื่อ `word_counts` โดย key คือคำ และ value คือจำนวนครั้งที่พบนั้น

```python
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
```

เมื่อสร้าง dictionary เสร็จแล้ว

-   `len(words)` คือจำนวนคำทั้งหมด `T`
-   `len(word_counts)` คือจำนวนคำที่ไม่ซ้ำกัน `U`

จากนั้นโปรแกรมคำนวณคะแนนของคำแต่ละคำเพียงครั้งเดียว
แล้วเก็บไว้ใน `relatable_scores`
การเตรียมคะแนนล่วงหน้าทำให้ตอนค้นหาไม่ต้องนับคำในเอกสารใหม่ทุกครั้ง

---

## การรับข้อมูลเอกสาร

บรรทัดแรกเป็นจำนวนเอกสาร `n` แล้วแต่ละเอกสารใช้ข้อมูลสองบรรทัดตามลำดับ

1. ชื่อเอกสาร
2. คำทั้งหมดในเอกสาร

โปรแกรมเก็บข้อมูลใน dictionary `documents` โดยมีโครงสร้างดังนี้

```text
ชื่อเอกสาร -> {คำ -> คะแนนความเกี่ยวข้อง}
```

คำสั่งสำคัญคือ

```python
documents[name] = calculate_relatable_scores(words)
```

ข้อมูลภาษาอังกฤษตามโจทย์เป็นตัวพิมพ์ใหญ่ทั้งหมด
โค้ดจึงเปรียบเทียบข้อความแบบตรงตัวโดยไม่ต้องแปลงตัวพิมพ์

เนื่องจากชื่อเอกสารถูกใช้เป็น key หากชื่อซ้ำ ข้อมูลเดิมจะถูกแทนที่
ส่วนบรรทัดเอกสารว่างซึ่งอยู่นอกข้อมูลตามโจทย์จะทำให้ `words` เป็นลิสต์ว่าง
ลูปคำนวณคะแนนจึงไม่ทำงานและคืน dictionary ว่าง โดยไม่เกิดการหารด้วยศูนย์
เอกสารนั้นจะไม่ถูกเลือกจากคำค้นหาใด

---

## การค้นหาเอกสารที่ดีที่สุด

โปรแกรมรับคำค้นหาทีละบรรทัดภายในลูป `while True`
ถ้าพบ `-1` จะหยุดทำงานทันที มิฉะนั้นจะตรวจเอกสารทุกฉบับ

ในการค้นหาแต่ละครั้ง `max_score` เริ่มที่ `0` และ `best_document`
เริ่มเป็นข้อความว่าง โปรแกรมจะอัปเดตคำตอบเมื่อ

```python
query in scores and scores[query] > max_score
```

เงื่อนไขแรกป้องกันการอ่าน key ที่ไม่มีอยู่ ส่วนเงื่อนไขที่สองเก็บเฉพาะเอกสาร
ที่มีคะแนนสูงกว่าคะแนนที่ดีที่สุดก่อนหน้า

-   ถ้า `max_score > 0` ให้แสดงชื่อ `best_document`
-   ถ้าคำค้นหาไม่อยู่ในเอกสารใดเลย คะแนนสูงสุดยังเป็น `0`
    จึงแสดง `NOT FOUND`

โจทย์รับประกันว่าไม่มีกรณีคะแนนสูงสุดเท่ากัน
หากเกิดคะแนนเท่ากันนอกเหนือจากกรณีทดสอบ
การใช้เครื่องหมาย `>` จะคงเอกสารที่รับเข้ามาก่อนไว้

โปรแกรมแสดงคำตอบทันทีหลังรับคำค้นหาแต่ละคำ
ดังนั้นลำดับผลลัพธ์จึงตรงกับลำดับคำค้นหา

---

## ลำดับการทำงาน

1. รับจำนวนเอกสาร
2. รับชื่อและข้อความของแต่ละเอกสาร แล้วคำนวณคะแนนของทุกคำ
3. รับคำค้นหาหนึ่งคำ
4. เปรียบเทียบคะแนนของคำนั้นในเอกสารทุกฉบับ
5. แสดงชื่อเอกสารที่คะแนนสูงสุด หรือ `NOT FOUND`
6. กลับไปรับคำถัดไปจนพบ `-1`

สำหรับตัวอย่างในโจทย์ คำค้นหา `PEN`, `GOOGLE`, `APPLE`, `I` และ `AKB`
ให้ผลลัพธ์ตามลำดับดังนี้

```text
PPAP
GOOGLE
MYAPPLE
PPAP
NOT FOUND
```

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_07_Search.py
# Problem   : Part-III Search Engine
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Calculate relatable scores for a list of words.
def calculate_relatable_scores(words):
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    total_words = len(words)
    total_unique_words = len(word_counts)

    relatable_scores = {}
    for word, count in word_counts.items():
        relatable_scores[word] = (count / total_words) * (1 / total_unique_words)
    return relatable_scores


# Initialize a list of documents.
documents = {}

# Input amount of documents and calculate relatable scores for each document.
n = int(input())
for _ in range(n):
    name = input().strip()
    words = input().strip().split()
    documents[name] = calculate_relatable_scores(words)

# Query for a word and find the most relatable document.
while True:
    query = input().strip()
    if query == "-1":
        break

    max_score = 0
    best_document = ""

    for name, scores in documents.items():
        if query in scores and scores[query] > max_score:
            max_score = scores[query]
            best_document = name

    if max_score > 0:
        print(best_document)
    else:
        print("NOT FOUND")
```
