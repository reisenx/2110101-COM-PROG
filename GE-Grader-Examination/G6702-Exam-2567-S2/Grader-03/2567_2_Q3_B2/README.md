<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Plate Extractor ★★ (
      <a href="https://drive.google.com/file/d/1JQPTF4RkH_XMh0RffyJAe--oFt2vvAsJ/view?usp=sharing">
        <code>2567_2_Q3_B2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบทะเบียนและจุดแบ่ง**](#รูปแบบทะเบียนและจุดแบ่ง)
-   [**แทรกช่องว่างเพื่อแยกทะเบียน**](#แทรกช่องว่างเพื่อแยกทะเบียน)
-   [**อ่านไฟล์และรวมผลลัพธ์**](#อ่านไฟล์และรวมผลลัพธ์)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**Solution**](#solution)

---

## รูปแบบทะเบียนและจุดแบ่ง

ทะเบียนหนึ่งคันมีรูปแบบดังนี้

1. ตัวเลขนำหน้า 1 หลัก
2. อักษรไทย 2 ตัว
3. ตัวเลขท้าย 1 ถึง 4 หลัก

ปัญหาคืออักขระขึ้นบรรทัดใหม่บางตำแหน่งหายไป ทำให้ทะเบียนหลายคันติดกัน เช่น

```text
1กข5092ขค884ขง2
```

ต้องแยกกลับเป็น `1กข509`, `2ขค88` และ `4ขง2` โดยห้ามใช้ regular expression

สังเกตว่าตัวเลขนำหน้าทะเบียนจะตามด้วยอักษรไทย ซึ่งเป็นอักขระที่ไม่ใช่ตัวเลข
แต่ตัวเลขส่วนท้ายทะเบียนจะตามด้วยตัวเลขตัวถัดไปหรือเป็นตัวสุดท้ายของข้อความ
จุดสังเกตนี้ทำให้หาเลขตัวแรกของทะเบียนแต่ละคันได้

---

## แทรกช่องว่างเพื่อแยกทะเบียน

ฟังก์ชัน `get_plates_from_str()` เดินดูอักขระทีละตำแหน่งพร้อมอักขระถัดไป

```python
if raw_data[i].isdigit() and not raw_data[i + 1].isdigit():
    modified_data += " " + raw_data[i]
```

ถ้าอักขระปัจจุบันเป็นตัวเลขและตัวถัดไปไม่ใช่ตัวเลข อักขระปัจจุบันคือเลขนำหน้า
ของทะเบียน จึงเติมช่องว่างไว้ **ก่อน** ตัวเลขนั้น

ตัวอย่างช่วงรอยต่อ `...5092ข...` จะพิจารณาเลข `2` ซึ่งมี `ข` ตามหลัง
แล้วเปลี่ยนเป็น `...509 2ข...` เมื่อทำครบทั้งบรรทัดจะได้ข้อความที่ใช้ช่องว่าง
คั่นทะเบียนแต่ละคัน

ลูปทำงานถึงอักขระรองสุดท้าย เพราะต้องมอง `i + 1` ด้วย หลังจบลูปจึงเติม
`raw_data[-1]` กลับเข้าไป แล้วใช้

```python
modified_data.strip().split()
```

เพื่อตัดช่องว่างหัวท้ายและแยกเป็นลิสต์ทะเบียน ช่องว่างที่ถูกเติมก่อนทะเบียนคันแรก
ไม่ทำให้เกิดข้อมูลว่าง เพราะ `strip()` นำช่องว่างนั้นออกก่อน

---

## อ่านไฟล์และรวมผลลัพธ์

`get_plates_from_file()` เปิดไฟล์ด้วย `encoding="utf-8"` เพื่ออ่านอักษรไทยได้ถูกต้อง
จากนั้นอ่านทีละบรรทัด

```python
for line in file:
    plates += get_plates_from_str(line.strip())
```

`line.strip()` นำอักขระขึ้นบรรทัดใหม่ออก แต่ไม่เปลี่ยนลำดับทะเบียน
ผลจากแต่ละบรรทัดถูกต่อท้ายลิสต์ `plates` ด้วย `+=`
ดังนั้นผลลัพธ์สุดท้ายยังเรียงตามลำดับที่ปรากฏในไฟล์ต้นฉบับ

วิธีนี้ไม่ได้เดาจำนวนหลักด้านท้ายทะเบียนโดยตรง แต่ใช้รูปแบบ
“เลขนำหน้า 1 หลักแล้วตามด้วยอักษร” เป็นจุดเริ่มทะเบียนคันใหม่
จึงรองรับตัวเลขท้ายตั้งแต่ 1 ถึง 4 หลักตามโจทย์

---

## ลำดับการทำงานของโปรแกรม

ฟังก์ชัน `main()` ทำงานเป็นขั้นตอนดังนี้

1. รับชื่อไฟล์ด้วย `input().strip()`
2. เรียก `get_plates_from_file(filename)` เพื่ออ่านและแยกทะเบียนทุกบรรทัด
3. วน `for plate in plates` แล้ว `print(plate)` ทีละคัน

จึงได้ทะเบียนหนึ่งคันต่อหนึ่งบรรทัด และไม่มีการเรียงลำดับใหม่หรือเปลี่ยนข้อความ
ภายในทะเบียน

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q3_B2.py
# Problem   : Plate Extractor
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------


# Function to extract license plates from a string
def get_plates_from_str(raw_data):
    # Initialize an empty string to hold modified data
    modified_data = ""

    # Iterate through the characters in the raw string
    for i in range(len(raw_data) - 1):
        # Check the pattern of one digits followed by a non-digit character
        if raw_data[i].isdigit() and not raw_data[i + 1].isdigit():
            # Add whitespace before the digit for splitting
            modified_data += " " + raw_data[i]
        # The current character does not match the pattern
        else:
            modified_data += raw_data[i]
    # Add the last character to modified_data
    modified_data += raw_data[-1]

    # Split the modified data by whitespace and return the list of plates
    return modified_data.strip().split()


# Function to read a file and extract license plates
def get_plates_from_file(filename):
    # Initialize an empty list to hold the plates
    plates = []

    # Open the file, read each line and extract license plates
    with open(filename, encoding="utf-8") as file:
        for line in file:
            plates += get_plates_from_str(line.strip())

    # Return the list of all license plates in the file
    return plates


# Main function
def main():
    # Input the filename
    filename = input().strip()

    # Extract the license plates from the file
    plates = get_plates_from_file(filename)

    # Output all the license plates
    for plate in plates:
        print(plate)


# Run the main function
main()
```
