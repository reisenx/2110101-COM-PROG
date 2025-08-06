<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Giant Checker ★★★ (
      <a href="https://drive.google.com/file/d/1yxHWqPdlpDYGA5fi5GwBWQIgUZU1_xvg/view?usp=drive_link">
        <code>P3_02_Checker</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_02_Checker.py
# Problem   : Part-III Giant Checker
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Constants for character to number mapping
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Parse the input string into row and column numbers
# This pattern supports formats: "A1", "B2", ..., "Z52"
def pattern01_parser(string):
    # Initialize row and column to -1 (invalid)
    row, col = -1, -1
    # Extract the first character as row and the rest as column
    row_str = string[0].strip()
    col_str = string[1:].strip()

    # Check if the row is a valid letter
    if row_str in ALPHABET and len(row_str) == 1:
        row = ALPHABET.index(row_str) + 1
    # Check if the column is a valid number between 1 and 52
    if col_str.isdigit() and 1 <= int(col_str) <= 52:
        col = int(col_str)
    # Return the row and column as a list
    return [row, col]


# Parse the input string into row and column numbers
# This pattern supports formats: "row=1, col=2", "col=3, row=A", etc.
def pattern02_parser(string):
    # Initialize row and column to -1 (invalid)
    row, col = -1, -1
    # Split the string by commas and equal signs
    parts = [p.strip() for p in string.replace(",", "=").split("=")]

    # Check if the input has exactly 4 parts
    if len(parts) == 4:
        # Extract the keys and values
        key1, val1, key2, val2 = parts
        # Check if the keys are "row" and "col" in any order
        if (key1 == "row" and key2 == "col") or (key1 == "col" and key2 == "row"):
            # Determine the row and column based on the keys
            if key1 == "row" and key2 == "col":
                row_str, col_str = val1, val2
            else:
                row_str, col_str = val2, val1

            # Check if the row is a valid letter
            if row_str in ALPHABET and len(row_str) == 1:
                row = ALPHABET.index(row_str) + 1
            # Check if the column is a valid number between 1 and 52
            if col_str.isdigit() and 1 <= int(col_str) <= 52:
                col = int(col_str)
    # Return the row and column as a list
    return [row, col]


# Input a string
string = input().strip()
# Determine the pattern and parse the input
if len(string) <= 3:
    row, col = pattern01_parser(string)
else:
    row, col = pattern02_parser(string)

# Output the results
if row == -1 and col == -1:
    print("Invalid row and column")
elif row == -1:
    print("Invalid row")
elif col == -1:
    print("Invalid column")
elif row % 2 == col % 2:
    print("White")
else:
    print("Black")
```
