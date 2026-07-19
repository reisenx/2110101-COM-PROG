<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![12-class.png](/Z99-OTHERS/12-class/01-class.png)

# Contents

- [Section 1: Classes and Objects](#section-1-classes-and-objects)
    - [1.1. From Existing Types to New Types](#11-from-existing-types-to-new-types)
    - [1.2. Defining a Class](#12-defining-a-class)
    - [1.3. Creating Objects with `__init__`](#13-creating-objects-with-__init__)
    - [1.4. Objects Have Separate Attributes](#14-objects-have-separate-attributes)
- [Section 2: Object Attributes](#section-2-object-attributes)
    - [2.1. Reading and Updating Attributes](#21-reading-and-updating-attributes)
    - [2.2. Objects as Attributes](#22-objects-as-attributes)
    - [2.3. Collections of Objects](#23-collections-of-objects)
- [Section 3: Methods](#section-3-methods)
    - [3.1. From Functions to Methods](#31-from-functions-to-methods)
    - [3.2. The Meaning of `self`](#32-the-meaning-of-self)
    - [3.3. Methods That Change Object State](#33-methods-that-change-object-state)
    - [3.4. Calling Methods from Methods](#34-calling-methods-from-methods)
    - [3.5. Calling a Helper Through the Class](#35-calling-a-helper-through-the-class)
- [Section 4: Special Methods](#section-4-special-methods)
    - [4.1. Arithmetic and Conversion](#41-arithmetic-and-conversion)
    - [4.2. Object Comparison with `__lt__`](#42-object-comparison-with-__lt__)
    - [4.3. Text Representation with `__str__`](#43-text-representation-with-__str__)
    - [4.4. Sorting Objects](#44-sorting-objects)

---

# Section 1: Classes and Objects

ที่ผ่านมา เราใช้ประเภทข้อมูลที่ Python มีให้ เช่น `int`, `float`, `str`,
`bool`, `list`, `tuple` และ `dict` แต่ข้อมูลบางอย่างประกอบด้วยรายละเอียดหลายค่า
ที่สัมพันธ์กัน เช่น หนังสือหนึ่งเล่มมีชื่อ หมายเลข ISBN และราคา

**Class (คลาส)** ช่วยให้เราสร้างประเภทข้อมูลใหม่ที่เหมาะกับสิ่งที่ต้องการแทน
ส่วน **Object (อ็อบเจกต์)** คือข้อมูลแต่ละตัวที่สร้างจาก class นั้น

## 1.1. From Existing Types to New Types

หากใช้ `tuple` เก็บหนังสือ ตำแหน่งของสมาชิกแต่ละตำแหน่งจะมีความหมายเฉพาะ

```python
book = ("Data Science", "149190142X", 28.79)
title = book[0]
isbn = book[1]
price = book[2]
```

วิธีนี้สั้น แต่ผู้อ่านต้องจำว่า `book[2]` หมายถึงราคา หากใช้ `dict`
ชื่อของแต่ละรายละเอียดจะชัดขึ้น

```python
book = {
    "title": "Data Science",
    "isbn": "149190142X",
    "price": 28.79,
}
price = book["price"]
```

Class เป็นอีกทางเลือกหนึ่ง โดยรวมโครงสร้างของข้อมูลและบริการที่เกี่ยวข้องไว้ด้วยกัน
เมื่อสร้าง class `Book` แล้ว เราจะเขียน `book.price` เพื่อเข้าถึงราคาได้

| คำศัพท์ | ความหมาย | ตัวอย่าง |
| :-- | :-- | :-- |
| Class | ประเภทข้อมูลที่เรากำหนดขึ้น | `Book` |
| Object / Instance | ข้อมูลหนึ่งตัวที่สร้างจาก class | `book` |
| Attribute | ตัวแปรที่เป็นรายละเอียดของ object | `book.price` |
| Method | ฟังก์ชันที่เรียกใช้กับ object | `book.discount(10)` |

> [!IMPORTANT]
>
> Class เป็นประเภทข้อมูล ส่วน object เป็นค่าข้อมูลจริง เช่นเดียวกับที่ `int`
> เป็นประเภทข้อมูล และ `10` เป็นค่าหนึ่งของประเภท `int`

## 1.2. Defining a Class

ใช้คำสั่ง `class` ตามด้วยชื่อ class และเครื่องหมาย `:` โดยนิยมตั้งชื่อ class
แบบขึ้นต้นแต่ละคำด้วยตัวพิมพ์ใหญ่ เช่น `Book`, `BankAccount` และ `Rectangle`

Class ที่ยังไม่มีรายละเอียดสามารถเขียนด้วย `pass` ได้

```python
class Book:
    pass
```

เมื่อ Python ทำคำสั่งนี้ ชื่อ `Book` จะอ้างถึงประเภทข้อมูลใหม่ แต่ยังไม่มี object
ใดถูกสร้างขึ้น

```python
class Book:
    pass


book = Book()
print(type(book))
```

ผลลัพธ์คือ

```
<class '__main__.Book'>
```

คำสั่ง `Book()` สร้าง object ใหม่จาก class `Book` แล้วให้ตัวแปร `book`
อ้างถึง object นั้น

## 1.3. Creating Objects with `__init__`

โดยทั่วไป object ต้องมีข้อมูลตั้งแต่ตอนสร้าง จึงกำหนด **special method**
ชื่อ `__init__` ไว้ภายใน class เมธอดนี้ทำงานโดยอัตโนมัติหลังจาก Python
สร้าง object ใหม่

```python
class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price


book = Book("Data Science", "149190142X", 28.79)
print(book.title)
print(book.price)
```

ผลลัพธ์คือ

```
Data Science
28.79
```

เมื่อเรียก `Book("Data Science", "149190142X", 28.79)` จะเกิดขั้นตอนสำคัญดังนี้

1. Python สร้าง object ใหม่จาก `Book`
2. Python เรียก `__init__` โดยส่ง object ใหม่นั้นให้พารามิเตอร์ `self`
3. อาร์กิวเมนต์ที่เหลือถูกส่งให้ `title`, `isbn` และ `price` ตามลำดับ
4. คำสั่ง `self.title = title` และบรรทัดถัด ๆ ไปสร้าง attributes ใน object

ชื่อทางซ้ายและขวาของ `=` ไม่จำเป็นต้องเหมือนกัน แต่การใช้ชื่อเดียวกันช่วยให้
เห็นความสัมพันธ์ได้ชัดเจน เช่น ใน `self.price = price` นั้น `self.price`
คือ attribute ส่วน `price` คือ parameter

> [!WARNING]
>
> ชื่อ method ต้องเป็น `__init__` ซึ่งมีขีดเส้นใต้สองตัวทั้งด้านหน้าและด้านหลัง
> หากสะกดผิด Python จะไม่เรียก method นี้ขณะสร้าง object

## 1.4. Objects Have Separate Attributes

Object แต่ละตัวมี attributes ของตัวเอง แม้สร้างจาก class เดียวกัน

```python
class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price


book1 = Book("Data Science", "149190142X", 28.79)
book2 = Book("Learning Python", "1449355730", 37.06)
book3 = Book("Data Analysis", "1449319793", 27.68)

print(book1.title, book1.price)
print(book2.title, book2.price)
print(book3.title, book3.price)
```

ผลลัพธ์คือ

```
Data Science 28.79
Learning Python 37.06
Data Analysis 27.68
```

มองความสัมพันธ์ระหว่างตัวแปรกับ object ได้ดังนี้

```text
book1 ──> Book object: title="Data Science",   price=28.79
book2 ──> Book object: title="Learning Python", price=37.06
book3 ──> Book object: title="Data Analysis",  price=27.68
```

การแก้ `book1.price` จึงไม่ทำให้ `book2.price` หรือ `book3.price` เปลี่ยนตาม

---

# Section 2: Object Attributes

Attribute คือตัวแปรที่อยู่ใน object การเขียนจุด (`.`) หลัง object
เป็นการเลือก attribute ที่ต้องการ เช่น `book.title` และ `book.price`

## 2.1. Reading and Updating Attributes

เราสามารถอ่าน attribute นำไปคำนวณ กำหนดค่าใหม่ หรือปรับค่าเดิมได้

```python
class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price


book = Book("Data Science", "149190142X", 28.79)
print(book.title)

book.price *= 0.80
print(round(book.price, 2))
```

ผลลัพธ์คือ

```
Data Science
23.03
```

ในตัวอย่างนี้ `book.price *= 0.80` มีความหมายเดียวกับ
`book.price = book.price * 0.80` และแก้ attribute ของ object `book` โดยตรง

> [!WARNING]
>
> หากอ่าน attribute ที่ object ไม่มี เช่น `book.author` จะเกิด
> `AttributeError` ดังนั้นควรกำหนด attributes ที่ object ทุกตัวจำเป็นต้องมีใน
> `__init__`

## 2.2. Objects as Attributes

Attribute ไม่จำเป็นต้องเป็นตัวเลขหรือข้อความเท่านั้น แต่สามารถอ้างถึง object
อีกตัวหนึ่งได้ด้วย ตัวอย่างเช่น วงกลมมีจุดศูนย์กลางซึ่งเป็น `Point`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


circle = Circle(Point(20, 30), 100)
print(circle.center.x, circle.center.y)

circle.radius = 200
circle.center = Point(2, 4)
circle.center.x = 3
print(circle.center.x, circle.center.y, circle.radius)
```

ผลลัพธ์คือ

```
20 30
3 4 200
```

นิพจน์ `circle.center.x` อ่านจากซ้ายไปขวา

1. `circle.center` ได้ object `Point` ซึ่งเป็นจุดศูนย์กลาง
2. `.x` เลือก attribute `x` ของ `Point` object นั้น

```text
circle ──> Circle object
             ├─ radius: 200
             └─ center ──> Point object
                              ├─ x: 3
                              └─ y: 4
```

## 2.3. Collections of Objects

Object สามารถเป็นสมาชิกของ `list` ได้เหมือนข้อมูลประเภทอื่น ทำให้ประมวลผล
ข้อมูลหลาย object ด้วย loop หรือ list comprehension ได้

```python
class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price


def total_price(books):
    total = 0
    for book in books:
        total += book.price
    return total


books = [
    Book("Data Science", "149190142X", 28.79),
    Book("Learning Python", "1449355730", 37.06),
    Book("Data Analysis", "1449319793", 27.68),
]

print(round(total_price(books), 2))
print(min(book.price for book in books))
```

ผลลัพธ์คือ

```
93.53
27.68
```

ฟังก์ชันยังสามารถค้นหาแล้วคืน object ที่พบ หรือคืน `None` เมื่อไม่พบ

```python
class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price


def find_by_isbn(books, isbn):
    for book in books:
        if book.isbn == isbn:
            return book
    return None


books = [
    Book("Data Science", "149190142X", 28.79),
    Book("Data Analysis", "1449319793", 27.68),
]
found = find_by_isbn(books, "1449319793")
print(found.title if found is not None else "Not found")
```

ผลลัพธ์คือ

```
Data Analysis
```

---

# Section 3: Methods

**Method (เมธอด)** คือฟังก์ชันที่กำหนดอยู่ภายใน class และเรียกใช้ผ่าน object
ด้วยรูป `object.method(...)` วิธีนี้ทำให้บริการที่เกี่ยวกับข้อมูลอยู่รวมกับ
ประเภทข้อมูลนั้น

## 3.1. From Functions to Methods

สมมติว่าต้องการหาระยะห่างระหว่างจุดสองจุด เราอาจเริ่มจากฟังก์ชันทั่วไป

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2):
    dx = point1.x - point2.x
    dy = point1.y - point2.y
    return (dx ** 2 + dy ** 2) ** 0.5


point1 = Point(2, 4)
point2 = Point(5, 8)
print(distance(point1, point2))
```

ผลลัพธ์คือ

```
5.0
```

เมื่อย้ายฟังก์ชันเข้าไปใน `Point` และเปลี่ยน object ตัวแรกเป็น `self`
ฟังก์ชันนั้นจะเป็น method

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5


point1 = Point(2, 4)
point2 = Point(5, 8)
print(point1.distance(point2))
```

ผลลัพธ์คือ

```
5.0
```

รูปแบบการเรียกเปลี่ยนจาก `distance(point1, point2)` เป็น
`point1.distance(point2)` แต่ยังใช้ object สองตัวเหมือนเดิม

## 3.2. The Meaning of `self`

`self` คือพารามิเตอร์ที่อ้างถึง object ซึ่งอยู่หน้าจุดตอนเรียก method
Python ส่ง object นี้เข้าไปให้อัตโนมัติ

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5


point1 = Point(10, 20)
point2 = Point(13, 16)
result = point1.distance(point2)
print(result)
```

ผลลัพธ์คือ

```
5.0
```

ขณะทำงานใน `distance`

- `self` อ้างถึง object เดียวกับ `point1`
- `other` อ้างถึง object เดียวกับ `point2`
- `self.x` จึงเป็น `10` และ `other.x` เป็น `13`

การเรียก `point2.distance(point1)` จะสลับกัน คือ `self` อ้างถึง `point2`
และ `other` อ้างถึง `point1`

> [!IMPORTANT]
>
> โดยธรรมเนียม พารามิเตอร์แรกของ instance method ใช้ชื่อ `self`
> และไม่ต้องส่งค่าให้พารามิเตอร์นี้เองเมื่อเรียกผ่าน object

## 3.3. Methods That Change Object State

Method สามารถอ่านและแก้ attributes ของ `self` ได้ ตัวอย่าง `BankAccount`
มี method สำหรับฝากและถอนเงิน

```python
class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount


account = BankAccount("1-034-567-892", "Pranee", 500)
account.deposit(1000)
account.withdraw(150)
print(account.account_number, account.balance)
```

ผลลัพธ์คือ

```
1-034-567-892 1350
```

เงื่อนไขใน method รักษากติกาของ object: ฝากได้เฉพาะจำนวนบวก และถอนได้เฉพาะ
จำนวนบวกที่ไม่เกินยอดเงินปัจจุบัน หากเงื่อนไขไม่ผ่าน method จะไม่แก้ `balance`

## 3.4. Calling Methods from Methods

Method หนึ่งสามารถเรียก method อื่นผ่าน `self` หรือ object ที่ได้รับมาได้
ตัวอย่างการโอนเงินจากบัญชีปัจจุบันไปยังอีกบัญชีหนึ่ง

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def transfer_to(self, other, amount):
        if 0 < amount <= self.balance:
            self.withdraw(amount)
            other.deposit(amount)


source = BankAccount("A-001", 500)
destination = BankAccount("B-002", 100)
source.transfer_to(destination, 150)
print(source.balance, destination.balance)
```

ผลลัพธ์คือ

```
350 250
```

ใน `transfer_to`

- `self.withdraw(amount)` เรียก `withdraw` ของบัญชีต้นทาง
- `other.deposit(amount)` เรียก `deposit` ของบัญชีปลายทาง

## 3.5. Calling a Helper Through the Class

ฟังก์ชันช่วยที่อยู่ใน class แต่ไม่ต้องใช้ object ใด สามารถไม่มีพารามิเตอร์
`self` และเรียกผ่านชื่อ class ได้ ตัวอย่าง `Rational._gcd` หาตัวหารร่วมมาก
เพื่อย่อเศษส่วนขณะสร้าง object

```python
class Rational:
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __init__(self, numerator, denominator):
        divisor = Rational._gcd(numerator, denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor


number = Rational(4, 8)
print(number.numerator, number.denominator)
```

ผลลัพธ์คือ

```
1 2
```

การเขียน `Rational._gcd(...)` ทำให้ชัดว่าเลือกฟังก์ชัน `_gcd` จาก class
และไม่ส่ง object เข้าไปโดยอัตโนมัติ

> [!WARNING]
>
> ฟังก์ชัน `_gcd` ตัวอย่างนี้ไม่มีพารามิเตอร์ `self` จึงต้องเรียกผ่านชื่อ class
> ตามที่เขียนไว้ หากเรียก `number._gcd(...)` Python จะส่ง `number` เพิ่มเป็น
> อาร์กิวเมนต์แรกและทำให้จำนวนอาร์กิวเมนต์ไม่ตรงกัน

---

# Section 4: Special Methods

**Special methods** เป็น method ชื่อพิเศษที่ขึ้นต้นและลงท้ายด้วยขีดเส้นใต้
สองตัว Python จะเรียก method เหล่านี้เมื่อเราใช้ syntax หรือฟังก์ชันที่ตรงกัน
เช่น `a + b`, `a < b`, `float(a)` และ `str(a)`

## 4.1. Arithmetic and Conversion

Class `Rational` สามารถกำหนดการบวก การคูณ และการแปลงเป็น `float` ด้วย
`__add__`, `__mul__` และ `__float__` ตามลำดับ

```python
class Rational:
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __init__(self, numerator, denominator):
        divisor = Rational._gcd(numerator, denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __add__(self, other):
        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __float__(self):
        return self.numerator / self.denominator


half = Rational(1, 2)
quarter = Rational(1, 4)
total = half + quarter
product = half * quarter
print(total.numerator, total.denominator, float(total))
print(product.numerator, product.denominator, float(product))
```

ผลลัพธ์คือ

```
3 4 0.75
1 8 0.125
```

การทำงานที่เกิดขึ้นสรุปได้ดังนี้

| Syntax ที่ใช้ | Method ที่ Python เรียก | ค่าที่ควรคืน |
| :-- | :-- | :-- |
| `left + right` | `left.__add__(right)` | object ผลบวก |
| `left * right` | `left.__mul__(right)` | object ผลคูณ |
| `float(value)` | `value.__float__()` | ค่า `float` |

`__add__` และ `__mul__` ในตัวอย่างสร้าง `Rational` object ใหม่ โดยไม่แก้
attributes ของ object เดิม

## 4.2. Object Comparison with `__lt__`

Special method `__lt__` กำหนดความหมายของเครื่องหมาย `<` ชื่อ `lt` ย่อจาก
**less than** โดยรับ object ด้านขวาเป็นอาร์กิวเมนต์

```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, other):
        left = (self.year, self.month, self.day)
        right = (other.year, other.month, other.day)
        return left < right


date1 = Date(20, 1, 1990)
date2 = Date(9, 12, 1990)
print(date1 < date2)
print(date2 < date1)
```

ผลลัพธ์คือ

```
True
False
```

Tuple เปรียบเทียบสมาชิกจากซ้ายไปขวา จึงเรียง `(year, month, day)` เพื่อให้ปี
มีความสำคัญก่อนเดือนและวัน

สำหรับ `Rational` อาจเปรียบเทียบค่าที่แปลงเป็น `float` ตามแนวคิดในสไลด์

```python
class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __float__(self):
        return self.numerator / self.denominator

    def __lt__(self, other):
        return float(self) < float(other)


print(Rational(1, 4) < Rational(1, 2))
```

ผลลัพธ์คือ

```
True
```

## 4.3. Text Representation with `__str__`

Special method `__str__` คืนข้อความที่ใช้แทน object เมื่อเรียก `str(object)`
หรือส่ง object ให้ `print()`

```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


date = Date(20, 1, 1990)
print(str(date))
print(date)
```

ผลลัพธ์คือ

```
20/1/1990
20/1/1990
```

ทั้งสองบรรทัดเหมือนกัน เพราะ `print(date)` ขอข้อความจาก `date.__str__()`
โดยอัตโนมัติ

> [!IMPORTANT]
>
> `__str__` ต้องคืนค่าเป็น `str` หากคืนตัวเลขหรือข้อมูลประเภทอื่น Python 3.11
> จะเกิด `TypeError`

## 4.4. Sorting Objects

`list.sort()` และ `sorted()` สามารถใช้ `__lt__` เปรียบเทียบ object ขณะเรียง
ลำดับได้ ตัวอย่างต่อไปนี้กำหนดให้อาหารที่ราคาน้อยกว่าอยู่ก่อน

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __str__(self):
        return f"{self.name}:{self.price}"


menu = [
    Item("Fried rice", 45),
    Item("Phat thai", 50),
    Item("Congee", 30),
    Item("Papaya salad", 40),
]
menu.sort()

for item in menu:
    print(item)
```

ผลลัพธ์คือ

```
Congee:30
Papaya salad:40
Fried rice:45
Phat thai:50
```

การทำงานร่วมกันของ special methods มีสองส่วน

- `menu.sort()` เรียก `__lt__` เพื่อเปรียบเทียบราคาและจัดลำดับ object
- `print(item)` เรียก `__str__` เพื่อแสดงชื่อและราคาของแต่ละ object

ดังนั้น class ไม่ได้เป็นเพียงกลุ่ม attributes แต่ยังระบุได้ด้วยว่า object
ของประเภทใหม่นี้ควรคำนวณ เปรียบเทียบ แสดงผล และทำงานร่วมกับ object อื่นอย่างไร
