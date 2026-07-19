<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    CUENG Sport 2023 ★★★ (
      <a href="https://drive.google.com/file/d/1t8fcO-p0KzRPTC2RCLjLlpF3ABoSXFk9/view?usp=sharing">
        <code>2565_2_Q3_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บข้อมูลการสมัคร**](#การเก็บข้อมูลการสมัคร)
-   [**การคำนวณจำนวนทีมและตัวสำรอง**](#การคำนวณจำนวนทีมและตัวสำรอง)
-   [**การเรียงและแสดงผล**](#การเรียงและแสดงผล)
-   [**Solution**](#solution)

---

## การเก็บข้อมูลการสมัคร

ข้อมูลนำเข้ามี 2 ชุด โดยแต่ละชุดจบด้วยบรรทัด `END` ชุดแรกระบุชื่อกีฬา
และจำนวนผู้เล่นต่อทีม โปรแกรมเก็บไว้ใน dictionary `person_per_team`
เพื่อให้ค้นหาจำนวนผู้เล่นจากชื่อกีฬาได้โดยตรง

ก่อนรับข้อมูลชุดที่สอง โปรแกรมสร้าง dictionary ว่างให้กีฬาทุกชนิด
โครงสร้างของ `sport_registration` จึงมีลักษณะดังนี้

```text
{
    sport: {
        department: {name_1, name_2, ...}
    }
}
```

ข้อมูลการสมัครแต่ละบรรทัดมี `name`, `department` และรายชื่อกีฬา
หากสมัครหลายชนิดกีฬา ชื่อกีฬาจะคั่นด้วย `,` โปรแกรมจึงใช้
`sports.split(",")` แล้วเพิ่มชื่อผู้สมัครเข้าไปในกีฬาแต่ละชนิด

ชื่อผู้สมัครถูกเก็บใน `set` เพราะสมาชิกใน set ไม่ซ้ำกัน ผู้สมัครคนเดิมจึงสมัครเพิ่ม
ในบรรทัดถัดไปได้ และถ้าระบุกีฬาเดิมซ้ำก็ยังถูกนับเพียงคนเดียวในกีฬานั้น
ส่วนการสมัครหลายชนิดกีฬาจะถูกนับแยกกันตามปกติ

---

## การคำนวณจำนวนทีมและตัวสำรอง

สำหรับแต่ละคู่ของกีฬาและภาควิชา จำนวนผู้สมัครที่ไม่ซ้ำกันหาได้จาก
`members = len(members_set)` หากกีฬาชนิดนั้นต้องใช้ผู้เล่นทีมละ `size` คน
จำนวนทีมและผู้เล่นสำรองคำนวณจาก

$$
\text{teams} = \left\lfloor \frac{\text{members}}{\text{size}} \right\rfloor,
\qquad
\text{subs} = \text{members} \bmod \text{size}
$$

ในโค้ด `size` คือ `person_per_team[sport]` จึงเขียนเป็น Python ได้ว่า

```python
teams = members // person_per_team[sport]
subs = members % person_per_team[sport]
```

ตัวดำเนินการ `//` ให้จำนวนทีมเต็มที่จัดได้ และ `%` ให้จำนวนคนที่เหลือเป็นตัวสำรอง
เช่น มีผู้สมัคร `7` คนและใช้ทีมละ `3` คน จะได้ `2` ทีมและตัวสำรอง `1` คน

โปรแกรมเก็บผลเฉพาะเมื่อ `teams > 0` ภาควิชาที่มีผู้สมัครแต่ยังไม่ครบหนึ่งทีม
จึงไม่ปรากฏหลังชื่อกีฬา อย่างไรก็ตาม ชื่อกีฬายังคงอยู่ใน `sport_teams`
แม้ไม่มีผู้สมัครหรือไม่มีภาคใดจัดทีมได้ครบ

---

## การเรียงและแสดงผล

การวน `sorted(sport_teams.items())` ทำให้ชื่อกีฬาเรียงตามตัวอักษร
และ `sorted(departments.items())` ทำให้รหัสภาควิชาภายในกีฬาเดียวกัน
เรียงตามตัวอักษรเช่นกัน ดังนั้นลำดับข้อมูลนำเข้าจึงไม่กระทบลำดับผลลัพธ์

แต่ละบรรทัดเริ่มด้วย `ชื่อกีฬา:` แล้วต่อข้อมูลแต่ละภาคในรูปแบบ
`รหัสภาค(จำนวนทีม,จำนวนผู้เล่นสำรอง)` โดยไม่มีช่องว่างคั่น เช่น
`Badminton:CE(2,1)CP(1,0)`

กีฬาที่ไม่มีภาควิชาใดจัดทีมได้ครบยังถูกแสดงเป็น `ชื่อกีฬา:`
เช่น `Volleyball:` เพราะโปรแกรมสร้างรายการสำหรับกีฬาทุกชนิดไว้ตั้งแต่ต้น

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_2_Q3_03.py
# Problem   : CUENG Sport 2023
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

# Initialize dictionaries to store person per team of each sport,
# sport registration details, and sport teams details
person_per_team = {}
sport_registration = {}
sport_teams = {}


# Input the number of persons per team for each sport and store it in a dictionary
def input_person_per_team():
    while True:
        # Read input line until it is "END"
        line = input().strip()
        if line == "END":
            break
        # Extract sport and person per team and store them in the dictionary
        sport, person = line.split()
        person_per_team[sport] = int(person)


# Participants register for sports
def register_sport():
    # Initialize dictionary for every sport
    for sport, _ in person_per_team.items():
        sport_registration[sport] = {}

    while True:
        # Read input line until it is "END"
        line = input().strip()
        if line == "END":
            break

        # Extract name, department, and sports from the line
        name, department, sports = line.split()
        # Register the participant in each sport they are interested in
        for sport in sports.split(","):
            # If the sport is not already registered, initialize it
            if department not in sport_registration[sport]:
                sport_registration[sport][department] = set()
            # Add the participant's name to the set of department members for that sport
            sport_registration[sport][department].add(name)


# Calculate the number of department teams and substitutes for each sport
def calculate_sport_teams():
    for sport, departments in sport_registration.items():
        # Initialize the sport in the sport_teams dictionary
        if sport not in sport_teams:
            sport_teams[sport] = {}

        for department, members_set in departments.items():
            # Calculate the number of teams and substitutes for each department
            members = len(members_set)
            teams = members // person_per_team[sport]
            subs = members % person_per_team[sport]
            # If there are teams, store the count in the sport_teams dictionary
            if teams > 0:
                sport_teams[sport][department] = [teams, subs]


# Output the sport teams in the required format
def print_sport_teams():
    # Sort the sport_teams dictionary by sport alphabetically
    for sport, departments in sorted(sport_teams.items()):
        # Initialize the output line with the sport name
        line = f"{sport}:"
        # Sort the departments by its name alphabetically
        for department, [teams, subs] in sorted(departments.items()):
            # Add the department and its teams/substitutes to the output line
            line += f"{department}({teams},{subs})"
        # Print the formatted line
        print(line)


# Main function
def main():
    input_person_per_team()
    register_sport()
    calculate_sport_teams()
    print_sport_teams()


# Execute the main function
main()
```
