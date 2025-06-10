<div align="center">
  <h1> Developer Notes </h1>  
  <b>Author:</b> Worralop Srichainont
</div>

# Contents

-   [**Project Structure**](#project-structure)
-   [**Naming Conventions**](#naming-conventions)
-   [**Coding Conventions**](#coding-conventions)
-   [**Problems Database**](#problem-database)

---

# Project Structure

This describes the project structure of this repository.

```
2110101-COM-PROG/
├── Grader Exercises (Unit 00 - 12)
│   ├── Problem Folder
│   │   ├── Problem Description (.pdf)
│   │   ├── Code Solution (.py)
│   │   └── README.md
│   ├── Lecture Summary
│   └── Problem List
├── Grader Exercises (Unit P1 - P3)
│   ├── Problem Folder
│   │   ├── Problem Description (.pdf)
│   │   ├── Code Solution (.py)
│   │   └── README.md
│   └── Problem List
├── Grader Exercises (Unit P1 - P3)
│   ├── Semester Folder
│   │   ├── Problem Folder
│   │   │   ├── Problem Description (.pdf)
│   │   │   ├── Code Solution (.py)
│   │   │   └── README.md
│   │   └── Problem List
│   └── Semester List
├── Midterm & Final
│   ├── Midterm
│   └── Final
├── Problem List
│   ├── Grader Exercise Database
│   └── Grader Examination Database
├── In-class Assignment
├── Study Materials
├── Components
└── MAIN PAGE (README.md)
```

---

# Naming Conventions

> [!IMPORTANT]
>
> Avoid using whitespaces and symbols except `-` and `_` (especially
> `&ZeroWidthSpace`) on a filename.

## Exercise Unit Name

-   Add `-` between words instead of space or comma (`,`).
-   Change the from the symbol `&` to word `and`.

**Example**

```
00 Python Intro         -->     00-Python-Intro
10 Tuple, Set, Dict     -->     10-Tuple-Set-Dict
12 Class & Object       -->     12-Class-and-Object
```

## Category Folder Name

-   Add code on first 2 or 3 characters, then follow by the folder name.

**Example**

```
PL-Problem-List
SM-Study-Materials
```

## Problem Name

-   Just follow the naming convention from the official 2110101 COMP PROG grader
    website. (Beware of `&ZeroWidthSpace` character).
-   In some problems may have multiple interesting solutions, just add
    `-sol<no.>` at the end

**Example**

```
00_Intro_00
P1_04_Bowling-sol1
P1_04_Bowling-sol2
```

## Grader Examination Semester

**Pattern** `G<year><semester>-Exam-<semester2>`

-   `<year>` is partial buddhist year (eg. 67)
-   `<semester>` is `01`, `02` or `03`. (`03` is for summer semester.)
-   `<semester2>` is `S1`, `S2` or `Summer`.

**Example**

```
G6501-Exam-2565-S1
G6603-Exam-2566-Summer
```

## Grader Examination Name

**Pattern** `Grader-<no.>-<section>`.

-   `<no>` is `1`, `2` or `3`. (`4` is for survey department section.)
-   `<section>` is `Withdrawal` for year 2 - 8 section, and `Survey` for Survey
    department section. Otherwise, just ignore this part.

**Example**

```
Grader-01
Grader-01-Withdrawal
Grader-04-Survey
```

## Grader Problem Name

**Pattern** `<year>_<semester>_<quiz>_<problem>_<section>`

-   `<year>` is full buddhist year (eg. 2567)
-   `<semester>` is a single digit. `1` and `2` are for normal semester, and `3`
    is for summer semester.
-   `<quiz>` is `Q1`, `Q2` or `Q3`. (`Q4` is for survey department section.)
-   `<problem>` has 2 character. Use `01`, `02` and `03` for old grader system
    (year 2566 or below), and use `A1`, `A2`, `A3`, `B1`, `B2`, `C1` and `C2`
    for new grader system (year 2567 or above).
-   `<section>` is `W` for year 2 - 8 section, and `S` for Survey department
    section. Otherwise, just ignore this part.

**Example**

```
2567_1_Q1_A3
2567_1_Q1_A1-W
2567_1_Q4_B1-S
```

## Course Syllabus

**Pattern** `S<year><semester>-Course-Syllabus-<year2>-<semester2>-<section>`.

-   `<year>` is partial buddhist year (eg. 67)
-   `<semester>` is `01`, `02` or `03`. (`03` is for summer semester.)
-   `<year2>` is full buddhist year (eg. 2567)
-   `<semester2>` is `S1` or `S2`.
-   `<section>` is `CP` if computer department otherwise, just ignore it.

**Example**

```
S6501-Course-Syllabus-2565-S1.pdf
S6701-Course-Syllabus-2567-S1-CP.pdf
```

---

# Coding Conventions

## Code Header

On every solution code, This needed to be added

```python
# Problem:  <problem_name> [<problem_code>]
# Author:   Worralop Srichainont
# Date:     <solve_date>
```

## PEP 8

The code inside this repository mainly follow the conventions from PEP 8
(https://peps.python.org/pep-0008/)

In python we can save a lot of time by using `black` library instead of manually
do it yourself.

To install it, use this command in terminal

```bash
pip install black
```

After finishing writing your code and already install the library, you can just
open the terminal and use the command.

```bash
# Format a single file
black my_python_file.py

# Format an entire project directory
black my_project_directory/
```

And `black` will automatically format the code according to PEP 8.

---

# Problem Database

Since writing table markdown of the problem list is really tedious, I use python
script to generate markdown for me instead.

-   Prepare the data from excel. This is easier to modify data, and lot more
    easier to maintain. Save as `.csv` file.
-   Use `pandas` to read `.csv` file, then construct the markdown or HTML.
-   Save as `.txt` file, then copy and paste on `README.md` pages

[**More Information**](/PL-Problem-List/database/)
