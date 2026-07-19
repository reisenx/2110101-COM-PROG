<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    USA Election ★★★ (
      <a href="https://drive.google.com/file/d/14jrcYfblgTZ9jnNMSjJzeXOevwjzyZ8J/view?usp=sharing">
        <code>2567_1_Q3_C1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ภาพรวมของการนับคะแนน**](#ภาพรวมของการนับคะแนน)
-   [**การจัดเก็บรัฐและเขตเลือกตั้ง**](#การจัดเก็บรัฐและเขตเลือกตั้ง)
-   [**การตรวจสอบและรวมคะแนนประชาชน**](#การตรวจสอบและรวมคะแนนประชาชน)
-   [**การให้คะแนน Electoral votes**](#การให้คะแนน-electoral-votes)
-   [**รูปแบบผลลัพธ์**](#รูปแบบผลลัพธ์)
-   [**Solution**](#solution)

---

## ภาพรวมของการนับคะแนน

โจทย์มีการรวมคะแนนสองระดับ

1. รวมคะแนนประชาชนจากทุก `county` ที่ถูกต้อง เพื่อหาคะแนน Republican และ
   Democrat ของแต่ละ `state`
2. พรรคที่มีคะแนนประชาชนมากกว่าในรัฐนั้นจะได้ Electoral votes ของรัฐ
   **ทั้งหมด** แล้วจึงรวม Electoral votes จากทุกรัฐ

ดังนั้นห้ามนำคะแนนประชาชนของคนละรัฐมารวมกันโดยตรง และห้ามแบ่ง Electoral votes
ตามสัดส่วนคะแนนประชาชน

ข้อมูลเข้ามีสามกลุ่ม แต่ละกลุ่มขึ้นต้นด้วยจำนวนรายการ `n`

-   รายชื่อรัฐในรูป `state,electoral votes`
-   รายชื่อเขตในรูป `county,state`
-   ผลลงคะแนนในรูป `county,state,republican votes,democrat votes`

---

## การจัดเก็บรัฐและเขตเลือกตั้ง

โปรแกรมใช้ dictionary หลายชุดเพื่อค้นข้อมูลจากชื่อได้โดยตรง

| ตัวแปร | key | value | หน้าที่ |
|:---|:---|:---|:---|
| `state_electoral_votes` | ชื่อรัฐ | จำนวน Electoral votes | เก็บคะแนนผู้แทนของแต่ละรัฐ |
| `state_counties` | ชื่อรัฐ | รายการชื่อ county | ใช้ตรวจว่าคู่ `county,state` มีอยู่จริง |
| `state_party_votes` | ชื่อรัฐ | คะแนนของสองพรรค | สะสมคะแนนประชาชนที่ผ่านการตรวจสอบ |
| `total_electoral` | ชื่อพรรค | Electoral votes รวม | เก็บผลรวมสุดท้าย |

เมื่ออ่าน `county,state` โปรแกรมสร้างรายการของรัฐนั้นเมื่อพบครั้งแรก
แล้วใช้ `append()` เพิ่มชื่อ county ทำให้ county ชื่อเดียวกันในคนละรัฐ
ยังแยกออกจากกันได้

---

## การตรวจสอบและรวมคะแนนประชาชน

ผลลงคะแนนแต่ละบรรทัดถูกแยกด้วย `split(",")` แล้วแปลงคะแนนของทั้งสองพรรค
เป็น `int` ก่อนนำไปใช้ โปรแกรมตรวจตามลำดับดังนี้

1. ถ้า `state` ไม่อยู่ใน `state_electoral_votes` ให้ใช้ `continue`
   ข้ามผลบรรทัดนั้น
2. ถ้า `county` ไม่อยู่ในรายการ `state_counties[state]` ให้ข้ามเช่นกัน
3. เมื่อคู่ `county,state` ถูกต้อง จึงเพิ่มคะแนนเข้า `state_party_votes[state]`

การเพิ่มคะแนนใช้ `+=` ดังนั้นถ้าคู่ county และรัฐเดียวกันปรากฏในผลลงคะแนน
หลายครั้ง โปรแกรมจะนำคะแนนทุกครั้งมาบวกกันตามข้อกำหนด เช่น

$$
R_s = \sum R_{county}, \qquad D_s = \sum D_{county}
$$

ซึ่งใน Python คือการสะสมด้วย
`state_party_votes[state]["republican"] += republican_votes` และคำสั่งแบบเดียวกัน
สำหรับ Democrat

> [!NOTE]
>
> โค้ดเข้าถึง `state_counties[state]` หลังตรวจชื่อรัฐแล้ว ข้อมูลตามเงื่อนไขโจทย์
> จึงต้องมีรายการ county ของรัฐที่ถูกอ้างถึงในผลลงคะแนนอย่างน้อยหนึ่งรายการ
> ส่วนคู่ county กับรัฐที่ไม่ตรงกับรายชื่อจะถูกละทิ้ง

---

## การให้คะแนน Electoral votes

เมื่อรวมคะแนนประชาชนเสร็จ โปรแกรมวนเฉพาะรัฐที่มีผลลงคะแนนที่ถูกต้อง

-   ถ้า `votes["republican"] > votes["democrat"]` ให้เพิ่ม Electoral votes
    ทั้งหมดของรัฐนั้นแก่ Republican
-   ถ้าคะแนน Republican น้อยกว่า ให้ Electoral votes ทั้งหมดแก่ Democrat

ตัวอย่างเช่น ถ้ารัฐหนึ่งมีคะแนนรวม `7000:9000` และมี Electoral votes `40`
Democrat จะได้เพิ่ม `40` คะแนน ไม่ใช่ `9000` คะแนน

โจทย์รับประกันว่าคะแนนประชาชนภายในแต่ละรัฐไม่เสมอกัน อย่างไรก็ตาม
ถ้ามีคะแนนเสมอกันจริง โค้ดจะไม่เข้าเงื่อนไข `if` หรือ `elif`
จึงไม่มีพรรคใดได้ Electoral votes ของรัฐนั้น

รัฐที่ไม่มีผลลงคะแนนที่ผ่านการตรวจสอบจะไม่อยู่ใน `state_party_votes`
และไม่เพิ่ม Electoral votes ให้พรรคใดเช่นกัน

---

## รูปแบบผลลัพธ์

โปรแกรมแสดงผลสองบรรทัดตามลำดับ

1. Electoral votes รวมของ Republican และ Democrat ในรูป `R:D`
   โดยไม่มีช่องว่างรอบ `:`
2. เปรียบเทียบผลรวมแล้วแสดงข้อความใดข้อความหนึ่ง
    -   `Republican wins`
    -   `Democrat wins`
    -   `Undecided` เมื่อ Electoral votes รวมเท่ากัน

การตัดสิน `Undecided` ใช้ผลรวม Electoral votes ของทั้งประเทศ
ซึ่งต่างจากการเสมอกันของคะแนนประชาชนภายในรัฐ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_C1.py
# Problem   : USA Election
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initialize dictionaries to store state, county, and votes
state_electoral_votes = {}
state_counties = {}
state_party_votes = {}
total_electoral = {"republican": 0, "democrat": 0}

# Input states and their electoral votes
n = int(input())
for _ in range(n):
    state, votes = input().strip().split(",")
    state_electoral_votes[state] = int(votes)

# Input counties and their states
n = int(input())
for _ in range(n):
    county, state = input().strip().split(",")
    if state not in state_counties:
        state_counties[state] = []
    state_counties[state].append(county)

# Calculate votes for each party in each state
n = int(input())
for _ in range(n):
    # Extract county, state, and votes from input
    data = input().strip().split(",")
    county = data[0].strip()
    state = data[1].strip()
    republican_votes = int(data[2].strip())
    democrat_votes = int(data[3].strip())

    # Validate state
    if state not in state_electoral_votes:
        continue

    # Validate county
    if county not in state_counties[state]:
        continue

    # Update party votes for the state
    if state not in state_party_votes:
        state_party_votes[state] = {"republican": 0, "democrat": 0}
    state_party_votes[state]["republican"] += republican_votes
    state_party_votes[state]["democrat"] += democrat_votes

# Calculate total electoral votes based on party votes on each state
for state, votes in state_party_votes.items():
    # Republican wins on the state and gains electoral votes
    if votes["republican"] > votes["democrat"]:
        total_electoral["republican"] += state_electoral_votes[state]

    # Democrat wins on the state and gains electoral votes
    elif votes["republican"] < votes["democrat"]:
        total_electoral["democrat"] += state_electoral_votes[state]

# Output the total electoral votes of each party
print(f"{total_electoral['republican']}:{total_electoral['democrat']}")

# Republican wins if they have more electoral votes
if total_electoral["republican"] > total_electoral["democrat"]:
    print("Republican wins")

# Democrat wins if they have more electoral votes
elif total_electoral["republican"] < total_electoral["democrat"]:
    print("Democrat wins")

# Both parties have equal electoral votes
else:
    print("Undecided")
```
