<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    BNK48 ★★★☆ (
      <a href="https://drive.google.com/file/d/1bTrlKl6DU7X-fDITSiY6FWAyg8p-iCY0/view?usp=drive_link">
        <code>P3_09_BNK48</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**เกณฑ์การจัดอันดับ**](#เกณฑ์การจัดอันดับ)
-   [**การออกแบบโครงสร้างข้อมูล**](#การออกแบบโครงสร้างข้อมูล)
-   [**การสะสมคะแนนโหวต**](#การสะสมคะแนนโหวต)
-   [**การหาคามิโอชิ**](#การหาคามิโอชิ)
-   [**การจัดอันดับสามคนแรก**](#การจัดอันดับสามคนแรก)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**Solution**](#solution)

---

## เกณฑ์การจัดอันดับ

โปรแกรมรับข้อมูลการโหวตทีละบรรทัดในรูปแบบ

```text
ชื่อโอตะ ชื่อไอดอล คะแนนโหวต
```

เมื่อพบบรรทัดที่มีตัวเลข `1`, `2` หรือ `3` เพียงค่าเดียว
ให้หยุดรับคะแนนและแสดงไอดอลสามอันดับแรกตามเกณฑ์ที่เลือก

| คำสั่ง | เกณฑ์เรียงจากมากไปน้อย | ค่าที่โค้ดใช้ |
|---|---|---|
| `1` | คะแนนโหวตรวมของไอดอล | `details["total_score"]` |
| `2` | จำนวนโอตะที่ต่างกันซึ่งเคยโหวตให้ | `len(details["otakus"])` |
| `3` | จำนวนโอตะที่เลือกไอดอลนั้นเป็นคามิโอชิ | `details["kamioshi_count"]` |

ชื่อทั้งหมดเป็นภาษาอังกฤษตัวพิมพ์ใหญ่
และโจทย์รับประกันว่ามีไอดอลที่ได้รับคะแนนอย่างน้อยสามคน

ผลลัพธ์ต้องมีชื่อสามชื่อคั่นด้วยเครื่องหมาย comma และเว้นวรรคหนึ่งช่อง เช่น

```text
CHERPRANG, JENNIS, JANE
```

คะแนนและจำนวนทุกค่าเป็นจำนวนเต็ม จึงไม่มีการปัดเศษ

---

## การออกแบบโครงสร้างข้อมูล

เราต้องเก็บทั้งมุมมองของโอตะแต่ละคนและมุมมองของไอดอลแต่ละคน
โค้ดจึงใช้ dictionary สองชุด

`otakus` เก็บคะแนนที่โอตะแต่ละคนให้ไอดอล และเก็บชื่อคามิโอชิหลังคำนวณเสร็จ

```text
ชื่อโอตะ -> {
    "vote": {ชื่อไอดอล -> คะแนนสะสม},
    "kamioshi": ชื่อคามิโอชิ
}
```

ส่วน `idols` เก็บข้อมูลที่ใช้กับเกณฑ์ทั้งสาม

```text
ชื่อไอดอล -> {
    "total_score": คะแนนรวม,
    "otakus": set ของชื่อโอตะ,
    "kamioshi_count": จำนวนครั้งที่เป็นคามิโอชิ
}
```

การใช้ `set` สำคัญต่อเกณฑ์ที่ `2` เพราะชื่อเดียวกันจะอยู่ใน set ได้เพียงครั้งเดียว
แม้โอตะคนนั้นจะโหวตไอดอลคนเดิมหลายบรรทัด

---

## การสะสมคะแนนโหวต

เมื่อรับคะแนน `s` จากโอตะ `o` ให้ไอดอล `i`
มีค่าที่ต้องอัปเดตสองชนิด

$$
V_{o,i} \leftarrow V_{o,i} + s
$$

คือคะแนนสะสมที่โอตะคนนั้นให้ไอดอล และ

$$
T_i \leftarrow T_i + s
$$

คือคะแนนรวมที่ไอดอลได้รับจากทุกคน

ในภาษา Python ตรงกับคำสั่ง

```python
otakus[otaku]["vote"][idol] += score
idols[idol]["total_score"] += score
```

พร้อมกันนั้น โปรแกรมบันทึกว่าโอตะคนนี้เคยโหวตให้ไอดอลด้วย

```python
idols[idol]["otakus"].add(otaku)
```

ตัวอย่างเช่น `SOMCHAI` โหวตให้ `CHERPRANG` `10` คะแนน
แล้วโหวตเพิ่มอีก `4` คะแนน
คะแนนของคู่นี้และคะแนนรวมของ `CHERPRANG` จะเพิ่มรวม `14`
แต่ `SOMCHAI` ถูกนับเป็นโอตะของ `CHERPRANG` เพียงหนึ่งคน

> [!NOTE]
>
> **คะแนนโหวต** จากหลายบรรทัดต้องนำมาบวกกัน
> แต่ **จำนวนโอตะ** ต้องนับชื่อเดิมเพียงครั้งเดียว
> dictionary ช่วยสะสมคะแนน ส่วน `set` ช่วยตัดชื่อซ้ำ

---

## การหาคามิโอชิ

คามิโอชิของโอตะหนึ่งคนคือไอดอลที่ได้รับคะแนนสะสมจากคนนั้นมากที่สุด
หากคะแนนเท่ากัน ให้เลือกชื่อไอดอลที่มาก่อนตามลำดับตัวอักษร

ฟังก์ชัน `get_kamioshi()` สร้างข้อมูลสำหรับเรียงลำดับเป็น

```python
[-score, idol]
```

เมื่อเรียงจากน้อยไปมาก

1. `-score` ทำให้คะแนนมากมาก่อน
2. `idol` ทำให้ชื่อที่มาก่อนตามตัวอักษรมาก่อนเมื่อคะแนนเท่ากัน

เช่น `PITI` ให้ `JENNIS` และ `JANE` อย่างละ `1` คะแนน
ชื่อ `JANE` มาก่อน `JENNIS` จึงเป็นคามิโอชิของ `PITI`

หลังรับคะแนนครบ `update_all_kamioshi()` จะหาคามิโอชิของโอตะทุกคน
แล้วเพิ่ม

```python
idols[kamioshi]["kamioshi_count"] += 1
```

โอตะแต่ละคนจึงเพิ่มจำนวนคามิโอชิให้ไอดอลเพียงคนเดียว

---

## การจัดอันดับสามคนแรก

ฟังก์ชันจัดอันดับทั้งสามแบบใช้แนวคิดเดียวกัน
คือสร้าง list ที่สมาชิกแต่ละตัวมีรูปแบบ

```python
[-ค่าที่ใช้จัดอันดับ, idol]
```

จากนั้นเรียง list แล้วเลือกเพียงสามตัวแรกด้วย `[:3]`
เครื่องหมายลบทำให้ค่ามากอยู่ข้างหน้า
ส่วนชื่อไอดอลทำให้ผลลัพธ์แน่นอนเมื่อค่าหลักเท่ากัน

โจทย์รับประกันว่าค่าที่ใช้จัดอันดับในสามอันดับแรกไม่เท่ากับอันดับอื่น
จึงไม่จำเป็นต้องกำหนดกติกาสำหรับคะแนนรวมที่เสมอกัน
อย่างไรก็ตาม canonical solution จะเลือกชื่อตามลำดับตัวอักษรหากเกิดกรณีดังกล่าว

สุดท้าย

```python
", ".join(results[cmd])
```

จะเชื่อมชื่อด้วย `, ` ตามรูปแบบที่โจทย์กำหนด

ตัวอย่างชุดคะแนนใน PDF ให้ผลดังนี้

| คำสั่ง | ผลลัพธ์ |
|---|---|
| `1` | `CHERPRANG, JENNIS, JANE` |
| `2` | `TURTLE, CHERPRANG, JENNIS` |
| `3` | `TURTLE, CHERPRANG, JANE` |

---

## ลำดับการทำงาน

1. รับข้อมูลสามส่วนและสะสมคะแนนไปเรื่อย ๆ
2. เมื่อพบบรรทัดคำสั่งหนึ่งค่า แปลง `1`–`3` เป็น index `0`–`2`
3. หาคามิโอชิของโอตะทุกคน แล้วนับจำนวนของไอดอล
4. สร้างผลการจัดอันดับทั้งสามแบบ
5. เลือกผลตามคำสั่ง และแสดงชื่อสามอันดับด้วย comma และช่องว่าง

การหยุดเมื่อ `len(data) == 1` สอดคล้องกับรูปแบบข้อมูลใน PDF
ซึ่งกำหนดให้บรรทัดสุดท้ายเป็นตัวเลข `1`, `2` หรือ `3`

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_09_BNK48.py
# Problem   : Part-III BNK48
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# Initialize dictionaries to store otaku and idol data
otakus = {}
idols = {}


# Function to handle voting by otakus for idols
def vote(otaku, idol, score):
    # If the otaku or idol does not exist, initialize them
    if otaku not in otakus:
        otakus[otaku] = {"vote": {}, "kamioshi": ""}
    if idol not in idols:
        idols[idol] = {"total_score": 0, "otakus": set(), "kamioshi_count": 0}

    # Update the otaku's vote for the idol and idol's total score
    if idol not in otakus[otaku]["vote"]:
        otakus[otaku]["vote"][idol] = 0
    otakus[otaku]["vote"][idol] += score
    idols[idol]["total_score"] += score
    idols[idol]["otakus"].add(otaku)


# Function to determine the kamioshi (favorite idol) for an otaku
def get_kamioshi(otaku):
    # Sort the votes of the otaku by score (descending) and idol name (ascending)
    idol_ranks = []
    for idol, score in otakus[otaku]["vote"].items():
        idol_ranks.append([-score, idol])
    idol_ranks.sort()

    # Return the idol with the highest score (kamioshi)
    return idol_ranks[0][1]


# Function to update all otakus' kamioshi and idols' kamioshi counts
def update_all_kamioshi():
    # Iterate through each otaku and determine their kamioshi
    for otaku, details in otakus.items():
        # Get the kamioshi for the otaku
        kamioshi = get_kamioshi(otaku)

        # Update the otaku's kamioshi
        details["kamioshi"] = kamioshi
        idols[kamioshi]["kamioshi_count"] += 1


# Function to get the top 3 idols based on total votes
def get_top_total_votes():
    # Sort idols by total score (descending) and idol name (ascending)
    idol_ranks = []
    for idol, details in idols.items():
        idol_ranks.append([-details["total_score"], idol])
    idol_ranks.sort()

    # Return the top 3 idols
    results = []
    for _, idol in idol_ranks[:3]:
        results.append(idol)
    return results


# Function to get the top 3 idols based on the number of otakus
def get_top_otaku_count():
    # Sort idols by the number of otakus (descending) and idol name (ascending)
    idol_ranks = []
    for idol, details in idols.items():
        idol_ranks.append([-len(details["otakus"]), idol])
    idol_ranks.sort()

    # Return the top 3 idols
    results = []
    for _, idol in idol_ranks[:3]:
        results.append(idol)
    return results


# Function to get the top 3 idols based on kamioshi counts
def get_top_kamioshi_count():
    # Sort idols by kamioshi count (descending) and idol name (ascending)
    idol_ranks = []
    for idol, details in idols.items():
        idol_ranks.append([-details["kamioshi_count"], idol])
    idol_ranks.sort()

    # Return the top 3 idols
    results = []
    for _, idol in idol_ranks[:3]:
        results.append(idol)
    return results


# Main function
def main():
    # Read votes from otakus to idols
    while True:
        data = input().strip().split()
        # Stop if the input is a command
        if len(data) == 1:
            cmd = int(data[0]) - 1
            break
        # Update the vote for the idol by the otaku
        otaku, idol, score = data[0], data[1], int(data[2])
        vote(otaku, idol, score)

    # Update kamioshi for all otakus and kamioshi counts for idols
    update_all_kamioshi()

    # Output the results based on the command
    results = [get_top_total_votes(), get_top_otaku_count(), get_top_kamioshi_count()]
    print(", ".join(results[cmd]))


# Call the main function to start the program
main()
```
