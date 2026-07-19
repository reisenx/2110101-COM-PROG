<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Bad Words ★★ (
      <a href="https://drive.google.com/file/d/1lgfgUbFPWHh2C0xvCvfsrskLhjylms1b/view?usp=sharing">
        <code>2567_1_Q2_B2-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การซ่อนคำด้วยดอกจัน**](#การซ่อนคำด้วยดอกจัน)
-   [**การค้นหาโดยไม่สนตัวพิมพ์**](#การค้นหาโดยไม่สนตัวพิมพ์)
-   [**การแทนที่ทุกตำแหน่ง**](#การแทนที่ทุกตำแหน่ง)
-   [**ข้อมูลเข้าและผลลัพธ์**](#ข้อมูลเข้าและผลลัพธ์)
-   [**Solution**](#solution)

---

## การซ่อนคำด้วยดอกจัน

โจทย์ให้เก็บตัวอักษรตัวแรกของคำไว้ แล้วเริ่มแทนตัวอักษรด้วย `*`
ตั้งแต่ตัวที่สองแบบตัวเว้นตัว เมื่อมองด้วย index ที่เริ่มจาก `0` จะได้ว่า

-   index คู่ `0, 2, 4, ...` เก็บตัวอักษรเดิม
-   index คี่ `1, 3, 5, ...` เปลี่ยนเป็น `*`

ฟังก์ชัน `hide_word()` จึงตรวจ `i % 2` ขณะเดินทุกตำแหน่ง ตัวอย่างเช่น
`CrAp` เปลี่ยนเป็น `C*A*` โดยตัวอักษรที่ยังมองเห็นคงตัวพิมพ์เดิมไว้

---

## การค้นหาโดยไม่สนตัวพิมพ์

คำเป้าหมายอาจเขียนด้วยตัวพิมพ์เล็กหรือใหญ่ต่างจากข้อความ โปรแกรมจึงค้นหาด้วย

```python
result.lower().find(target.lower(), search_idx)
```

การแปลงเป็นตัวพิมพ์เล็กใช้เฉพาะตอนค้นหา ส่วนข้อความที่นำไปสร้างคำซ่อนมาจาก
`result[start_idx:end_idx]` จึงรักษาตัวพิมพ์ของอักขระที่ไม่ได้ถูกแทนไว้

เมธอด `find()` คืน index เริ่มต้นของคำที่พบ หรือคืน `-1` เมื่อหาไม่พบ
ลูปจึงทำงานไปเรื่อย ๆ จนกระทั่ง `start_idx == -1`

---

## การแทนที่ทุกตำแหน่ง

เมื่อพบคำ โปรแกรมแบ่งข้อความเป็นสามส่วน

```python
before_target = result[:start_idx]
censored_target = hide_word(result[start_idx:end_idx])
after_target = result[end_idx:]
```

แล้วนำทั้งสามส่วนมาต่อกัน การแทนที่มีความยาวเท่าคำเดิม ตำแหน่งของข้อความส่วนหลัง
จึงไม่เลื่อน หลังจากนั้นกำหนด `search_idx = end_idx` เพื่อเริ่มค้นหาหลังคำที่เพิ่งแทน

> [!NOTE]
>
> การขยับไปที่ `end_idx` ทำให้การค้นหาเป็นแบบ **ไม่ซ้อนทับกัน**
> ถ้าคำถัดไปเริ่มตรงตำแหน่งที่คำเดิมจบพอดี จะยังค้นพบได้
> แต่คำที่เริ่มอยู่ภายในช่วงของคำที่แทนไปแล้วจะไม่ถูกนำมาพิจารณาซ้ำ

---

## ข้อมูลเข้าและผลลัพธ์

-   บรรทัดแรกคือคำที่ต้องการซ่อนหนึ่งคำ เก็บใน `offensive_word`
-   บรรทัดที่สองคือข้อความหนึ่งบรรทัด เก็บใน `text`
-   `.strip()` ตัดช่องว่างที่หัวและท้ายของข้อมูลทั้งสองบรรทัดตามพฤติกรรมของโค้ด
-   โปรแกรมแสดงข้อความหลังแทนคำครบทุกตำแหน่งเพียงหนึ่งบรรทัด

การค้นหาไม่สนตัวพิมพ์ แต่ตัวอักษรอื่นทั้งหมด เครื่องหมายวรรคตอน
และตัวพิมพ์ของตัวอักษรที่ไม่ถูกซ่อนยังคงเหมือนข้อความที่รับมา

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q2_B2-S.py
# Problem   : Bad Words
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------


# Function to hide words by alternating characters with asterisks
def hide_word(word):
    result = ""
    for i in range(len(word)):
        if i % 2 == 0:
            result += word[i]
        else:
            result += "*"
    return result


# Censor the text by replacing offensive word with their hidden versions
def censor_text(text, target):
    # Initialize the result with the original text and search index
    result = text
    search_idx = 0

    # Loop to find and replace all occurrences of the target word
    while True:

        # Find the next occurrence of the target word
        start_idx = result.lower().find(target.lower(), search_idx)
        end_idx = start_idx + len(target)

        # If no more occurrences are found, break the loop
        if start_idx == -1:
            break

        # Replace the target word with its vowel-hidden version
        before_target = result[:start_idx]
        censored_target = hide_word(result[start_idx:end_idx])
        after_target = result[end_idx:]

        result = before_target + censored_target + after_target

        # Update the search index to continue searching after the replaced word
        search_idx = end_idx

    # Return the censored text
    return result


# Input offensive word and text
offensive_word = input().strip()
text = input().strip()

# Output the censored text
print(censor_text(text, offensive_word))
```
