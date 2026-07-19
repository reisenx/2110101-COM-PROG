<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Stock Investment ★★★ (
      <a href="https://drive.google.com/file/d/17qHF6-icxbhkcdWW6TGm4iqUiztbMpTy/view?usp=sharing">
        <code>2565_2_Q3_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การจัดกลุ่มเรตติ้ง**](#การจัดกลุ่มเรตติ้ง)
-   [**การหารหัสบริษัทและรวมเงินลงทุน**](#การหารหัสบริษัทและรวมเงินลงทุน)
-   [**การคำนวณและแสดงผล**](#การคำนวณและแสดงผล)
-   [**Solution**](#solution)

---

## การจัดกลุ่มเรตติ้ง

ข้อมูลนำเข้ามี 2 ชุด โดยแต่ละชุดจบด้วยบรรทัด `END`
ชุดแรกบอกเรตติ้งของแต่ละบริษัท โปรแกรมจึงใช้ dictionary
`company_ratings` เก็บข้อมูลในรูปแบบ `รหัสบริษัท: กลุ่มเรตติ้ง`

เรตติ้งที่ลงท้ายด้วย `+` หรือ `-` ยังอยู่ในกลุ่มเดียวกับเรตติ้งหลัก เช่น `AA+`,
`AA` และ `AA-` อยู่ในกลุ่ม `AA` ทั้งหมด โปรแกรมจึงตัดเครื่องหมายออกก่อนเก็บ

```python
company, rating = data.split()
rating = rating.strip("+-")
company_ratings[company] = rating
```

กลุ่มที่ใช้รวมเงินมีลำดับดังนี้

| กลุ่ม | เรตติ้งที่อยู่ในกลุ่ม |
|---|---|
| `AAA` | `AAA` |
| `AA` | `AA+`, `AA`, `AA-` |
| `A` | `A+`, `A`, `A-` |
| `BBB` | `BBB+`, `BBB`, `BBB-` |
| `BB` | `BB+`, `BB`, `BB-` |
| `B` | `B+`, `B`, `B-` |
| `CCC` | `CCC+`, `CCC` |
| `CC` | `CC` |
| `C` | `C` |
| `D` | `D` |
| `None` | ไม่พบรหัสบริษัทในข้อมูลชุดแรก |

> [!NOTE]
>
> คำสั่ง `strip("+-")` ลบเครื่องหมาย `+` และ `-` ที่อยู่ติดกับ
> **ทั้งด้านซ้ายและด้านขวา** ของข้อความ แม้ comment ในโค้ดจะกล่าวถึงด้านขวาเท่านั้น
> สำหรับข้อมูลเรตติ้งตามโจทย์ เครื่องหมายจะอยู่ด้านขวา จึงได้กลุ่มที่ต้องการ

---

## การหารหัสบริษัทและรวมเงินลงทุน

ข้อมูลชุดที่สองประกอบด้วยรหัสหุ้นกู้และจำนวนเงินลงทุน รหัสหุ้นกู้ขึ้นต้นด้วยรหัสบริษัท
และตามด้วยรหัสการครบกำหนดที่เริ่มด้วยตัวเลข ฟังก์ชัน `get_company_rating()`
จึงวนดูรหัสบริษัทและตรวจว่าพบที่ตำแหน่ง `0` หรือไม่

```python
if stock.find(company) == 0:
    return company_ratings[company]
```

ตัวอย่างเช่น หาก `AYCAL` อยู่ในกลุ่ม `AA` รหัสหุ้นกู้ `AYCAL271A`
ก็จะถูกนับในกลุ่ม `AA` หากไม่มีรหัสบริษัทใดตรงกับส่วนต้นของรหัสหุ้นกู้
ฟังก์ชันจะคืนข้อความ `"None"`

โปรแกรมแปลงจำนวนเงินด้วย `int(money)` แล้วบวกสะสมใน `ratings_money`
ดังนั้นหุ้นกู้หลายรุ่นในกลุ่มเดียวกัน หรือรหัสหุ้นกู้เดิมที่ปรากฏหลายบรรทัด
จะถูกนำเงินมารวมกัน

> [!NOTE]
>
> Dictionary จำลำดับที่เพิ่มข้อมูล ฟังก์ชันนี้จึงคืนเรตติ้งของ
> **รหัสบริษัทตัวแรกที่เป็น prefix** ตามลำดับข้อมูลชุดแรก หากมีรหัสบริษัทหนึ่ง
> เป็นส่วนต้นของอีกรหัสหนึ่ง ลำดับที่รับเข้ามาจะมีผลต่อคำตอบของโค้ดนี้

---

## การคำนวณและแสดงผล

เมื่อรวมเงินครบแล้ว `total_money` คือผลรวมของเงินทุกกลุ่ม สำหรับกลุ่มที่มีเงิน
`money` โปรแกรมคำนวณร้อยละด้วยสูตร

$$
\text{percentage} = \frac{\text{money}}{\text{total\_money}} \times 100
$$

ซึ่งตรงกับนิพจน์ Python
`round((money / total_money) * 100, 2)` โดย `round(..., 2)`
ปัดผลลัพธ์ให้มีทศนิยมไม่เกิน 2 ตำแหน่ง

โปรแกรมวน `ratings_money.items()` ซึ่ง dictionary ถูกสร้างไว้ตามลำดับ
`AAA`, `AA`, `A`, `BBB`, `BB`, `B`, `CCC`, `CC`, `C`, `D`, `None`
จึงแสดงกลุ่มจากเรตติ้งสูงไปต่ำ และแสดง `None` เป็นลำดับสุดท้าย
กลุ่มที่มีเงินเป็น `0` จะไม่ถูกแสดง

แต่ละบรรทัดมีรูปแบบ `กลุ่ม จำนวนเงิน ร้อยละ%` เช่น
`AA 900000 16.36%` จำนวนเงินยังเป็น `int` ตามที่รับเข้ามา

> [!NOTE]
>
> `round(..., 2)` คืนค่าเป็นตัวเลข แต่ไม่ได้บังคับให้พิมพ์ทศนิยมครบ 2 ตำแหน่ง
> ดังนั้นค่าที่ปัดแล้วเป็น `20.0` จะแสดงเป็น `20.0%` ไม่ใช่ `20.00%`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_2_Q3_01.py
# Problem   : Stock Investment
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

# Initialize dictionaries to store company ratings
# and the total money invested in each rating category
company_ratings = {}
ratings_money = {
    "AAA": 0,
    "AA": 0,
    "A": 0,
    "BBB": 0,
    "BB": 0,
    "B": 0,
    "CCC": 0,
    "CC": 0,
    "C": 0,
    "D": 0,
    "None": 0,
}


# Input ratings for each company and store them in a dictionary
def input_ratings():
    while True:
        data = input().strip()
        # Stop when the input is "END"
        if data == "END":
            break
        # Extract the company name and its rating
        company, rating = data.split()
        # Remove "+" or "-" at the end of the rating
        rating = rating.strip("+-")
        # Store the rating in the company_ratings dictionary
        company_ratings[company] = rating


# Get the rating of a stock based on its company name
def get_company_rating(stock):
    # Check if the stock matches any company name in the dictionary
    for company, _ in company_ratings.items():
        # If the stock starts with the company name, return its rating
        if stock.find(company) == 0:
            return company_ratings[company]
    # If no match is found, return "None"
    return "None"


# Input stock investments and update the total money invested in each rating category
def input_stocks():
    while True:
        data = input().strip()
        # Stop when the input is "END"
        if data == "END":
            break
        # Extract the stock name and the amount of money invested
        stock, money = data.split()
        # Get the rating of the stock
        rating = get_company_rating(stock)
        # Add the money to the corresponding rating category
        ratings_money[rating] += int(money)


# Output the total money invested in each rating category
# along with the percentage of the total investment
def print_results():
    # Calculate the total money invested across all ratings
    total_money = sum(ratings_money.values())
    for rating, money in ratings_money.items():
        # Only print ratings with money invested greater than 0
        if money > 0:
            percentage = round((money / total_money) * 100, 2)
            print(f"{rating} {money} {percentage}%")


# Main function
def main():
    input_ratings()
    input_stocks()
    print_results()


# Execute the main function
main()
```
