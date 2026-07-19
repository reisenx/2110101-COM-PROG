<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Text Replace in File ★★☆ (
      <a href="https://drive.google.com/file/d/1JdGhOynEXVT9aRMdgd9qPwb9SeFidzX5/view?usp=sharing">
        <code>2567_2_Q2_B2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ภาพรวมของโปรแกรม**](#ภาพรวมของโปรแกรม)
-   [**อ่านและรวมข้อความจากไฟล์**](#อ่านและรวมข้อความจากไฟล์)
-   [**แทนข้อความโดยไม่สนใจตัวพิมพ์**](#แทนข้อความโดยไม่สนใจตัวพิมพ์)
-   [**จัดข้อความลงบรรทัด**](#จัดข้อความลงบรรทัด)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## ภาพรวมของโปรแกรม

ข้อมูลนำเข้ามีรูปแบบ `filename,target,replacement` โดยคั่นสามส่วนด้วย `,`
โปรแกรมทำงานตามลำดับดังนี้

1. อ่านทุกบรรทัดในไฟล์และรวมเป็นข้อความบรรทัดเดียว
2. ค้นหา `target` โดยไม่สนใจตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่ แล้วแทนด้วย
   `replacement`
3. หาความยาวบรรทัดที่ยาวที่สุดจากไฟล์ต้นฉบับ
4. แบ่งข้อความที่แก้แล้วกลับเป็นหลายบรรทัด โดยพยายามไม่ให้เกินความยาวนั้น

ค่าความยาวสูงสุดต้องวัดจากไฟล์เดิม ไม่ใช่ข้อความหลังแทนคำ
เพราะคำใหม่อาจสั้นหรือยาวกว่าคำเก่า

---

## อ่านและรวมข้อความจากไฟล์

`get_text_from_file()` วนอ่านไฟล์ทีละบรรทัด ใช้ `line.strip()`
ตัดอักขระขึ้นบรรทัดใหม่และช่องว่างที่หัวหรือท้าย แล้วเติมช่องว่างหนึ่งช่อง
ระหว่างบรรทัด

ตัวอย่างข้อความในไฟล์

```text
We analyzed the "Final
Outcome" carefully
```

จะถูกรวมเป็น

```text
We analyzed the "Final Outcome" carefully
```

จึงค้นหาเป้าหมายที่คร่อมบรรทัดเดิม เช่น `Final Outcome` ได้

ส่วน `get_max_line_length()` อ่านไฟล์เดิมอีกครั้ง แล้วหา

```python
max(max_length, len(line.strip()))
```

จึงไม่นับอักขระขึ้นบรรทัดใหม่ และไม่นับช่องว่างหัวหรือท้ายบรรทัด

---

## แทนข้อความโดยไม่สนใจตัวพิมพ์

`replace_on_text()` แปลงทั้งข้อความและเป้าหมายเป็นตัวพิมพ์เล็กเฉพาะตอนค้นหา

```python
start_idx = result.lower().find(target.lower(), find_idx)
```

เมื่อพบตำแหน่งแล้ว โปรแกรมนำข้อความก่อนตำแหน่งนั้นมาต่อกับ `replacement`
และข้อความหลังเป้าหมาย ดังนั้นคำใหม่จะใช้ตัวพิมพ์ตามที่รับเข้ามาทุกประการ
จากนั้นเลื่อน `find_idx` ไปหลังคำที่เพิ่งแทน เพื่อค้นหาครั้งถัดไป

การค้นหานี้เป็นการหาข้อความย่อย ไม่ได้ตรวจขอบเขตของคำ จึงแทนข้อความที่อยู่
ภายในคำอื่นด้วย ตัวอย่างเช่น target `Ed` และ replacement `Ing`
จะเปลี่ยน `painted` เป็น `paintIng` และ `danced` เป็น `dancIng`

---

## จัดข้อความลงบรรทัด

`display_text_on_limit()` ใช้ `text.split()` แบ่งข้อความตรงช่องว่าง
เครื่องหมายวรรคตอนที่ติดกับคำ เช่น `purchase.` หรือ `"result"`
จึงยังอยู่ใน token เดียวกับคำนั้นและจะไม่ถูกตัดออกจากกัน

โปรแกรมจัดบรรทัดแบบละโมบ โดยเริ่มจากคำแรกของบรรทัด แล้วลองเพิ่มคำถัดไป
พร้อมช่องว่างอีก `1` ตัว

$$
\text{ความยาวใหม่}
= \text{ความยาวปัจจุบัน} + 1 + \text{ความยาวคำถัดไป}
$$

ถ้าความยาวใหม่ไม่เกิน `limit` ก็เก็บคำไว้ในบรรทัดเดิม
แต่ถ้าเกิน จะพิมพ์บรรทัดปัจจุบันและเริ่มบรรทัดใหม่จากคำนั้น
แต่ละบรรทัดจึงไม่มีช่องว่างต่อท้าย

> [!NOTE]
>
> โปรแกรมไม่ตัดคำ หาก token หนึ่งยาวกว่า `limit` ด้วยตัวมันเอง
> token นั้นจะถูกพิมพ์ทั้งคำในบรรทัดเดียว ข้อมูลของโจทย์จึงต้องมีคำที่สามารถ
> วางได้ภายในความยาวสูงสุดของไฟล์เดิม

---

## ตัวอย่างการทำงาน

สำหรับ `file1.txt` บรรทัดเดิมที่ยาวที่สุดมี `23` อักขระ
เมื่อแทน `final outcome` ด้วย `result` แบบไม่สนใจตัวพิมพ์
ข้อความ `"Final Outcome"` จึงกลายเป็น `"result"` แล้วจัดบรรทัดได้เป็น

```text
We analyzed the
"result" carefully
before making a prudent
decision.
```

คำพร้อมเครื่องหมายคำพูดถูกย้ายขึ้นบรรทัดใหม่ทั้งชุด
เพราะ `We analyzed the "result"` ยาว `24` อักขระ ซึ่งเกินขีดจำกัด `23`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q2_B2.py
# Problem   : Text Replace in File
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------


# Read text from a file and return as a single-line string
def get_text_from_file(filename):
    text = ""
    with open(filename) as file:
        for line in file:
            text += line.strip() + " "
    return text.strip()


# Get the maximum line length from the file
def get_max_line_length(filename):
    max_length = 0
    with open(filename) as file:
        for line in file:
            max_length = max(max_length, len(line.strip()))
    return max_length


# Replace occurrences of target with replacement in the text (case-insensitive)
def replace_on_text(text, target, replacement):
    # Initialize the result with the original text
    result = text
    # Initialize the index for finding occurrences
    find_idx = 0

    # Loop to find and replace all occurrences of the target
    while True:
        # Find the next occurrence of the target in a case-insensitive manner
        start_idx = result.lower().find(target.lower(), find_idx)

        # If no more occurrences are found, break the loop
        if start_idx == -1:
            break

        # Calculate the end index of the found target
        end_idx = start_idx + len(target)

        # Replace the found target with the replacement in the result
        result = result[:start_idx] + replacement + result[end_idx:]

        # Update the find index to continue searching after the replaced text
        find_idx = start_idx + len(replacement)

    # Return the modified text
    return result


def display_text_on_limit(text, limit):
    # Split the text into words
    words = text.split()

    # Initialize the start index for the first word
    start_idx = 0

    # Output the words in lines not exceeding the length limit
    while start_idx < len(words):
        # Initialize the end index and current line length
        end_idx = start_idx + 1
        current_length = len(words[start_idx])

        # Calculate the end index for the current line
        while end_idx < len(words):
            # Calculate the length of the current line if the next word is added
            current_length += len(words[end_idx]) + 1

            # If the length exceeds the limit, break the loop
            if current_length > limit:
                break
            # Otherwise, include the next word
            end_idx += 1

        # Output the current line
        print(" ".join(words[start_idx:end_idx]))

        # Update the start index for the next iteration
        start_idx = end_idx


def main():
    # Extract the filename, target, and replacement from input
    filename, target, replacement = input().strip().split(",")

    # Get the text from the file
    text = get_text_from_file(filename)

    # Replace the target with the replacement in the text
    modified_text = replace_on_text(text, target, replacement)

    # Get the maximum line length from the file
    max_length = get_max_line_length(filename)

    # Display the modified text within the length limit
    display_text_on_limit(modified_text, max_length)


# Run the main function
main()
```
