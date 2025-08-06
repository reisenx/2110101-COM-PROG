<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Roman Numberal ★★★ (
      <a href="https://drive.google.com/file/d/11l2prjZRO4y18gnNhQcr6QshCzTOvojf/view?usp=drive_link">
        <code>12_Class_35</code>
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
# File Name : 12_Class_35.py
# Problem   : Roman Numeral
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Dictionary to convert between numbers and Roman numerals
NUMBER_TO_ROMAN = {
    0: "",
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    20: "XX",
    30: "XXX",
    40: "XL",
    50: "L",
    60: "LX",
    70: "LXX",
    80: "LXXX",
    90: "XC",
    100: "C",
    200: "CC",
    300: "CCC",
    400: "CD",
    500: "D",
    600: "DC",
    700: "DCC",
    800: "DCCC",
    900: "CM",
    1000: "M",
    2000: "MM",
    3000: "MMM",
    4000: "MMMM",
}
ROMAN_TO_NUMBER = {
    "I": (("III", 3), ("IX", 9), ("IV", 4), ("II", 2), ("I", 1)),
    "V": (("VIII", 8), ("VII", 7), ("VI", 6), ("V", 5)),
    "X": (("XXX", 30), ("XC", 90), ("XL", 40), ("XX", 20), ("X", 10)),
    "L": (("LXXX", 80), ("LXX", 70), ("LX", 60), ("L", 50)),
    "C": (("CCC", 300), ("CM", 900), ("CD", 400), ("CC", 200), ("C", 100)),
    "D": (("DCCC", 800), ("DCC", 700), ("DC", 600), ("D", 500)),
    "M": (("MMMM", 4000), ("MMM", 3000), ("MM", 2000), ("M", 1000)),
}


class Roman:
    # __init__ method
    # Initializes the Roman numeral with a string representation.
    def __init__(self, roman):
        self.roman = roman

    # __lt__ method
    # Compares two Roman numeral objects based on their integer values.
    def __lt__(self, rhs):
        return int(self) < int(rhs)

    # __str__ method
    # Returns the string representation of the Roman numeral.
    def __str__(self):
        return self.roman

    # __int__ method
    # Converts the Roman numeral to its integer value.
    def __int__(self):
        # Initialize the number to 0
        number = 0
        string = self.roman
        # Loop through the string until it is empty
        while string != "":
            # Check for the longest matching Roman numeral substring
            for substring, value in ROMAN_TO_NUMBER[string[0]]:
                # Found a match substring at the start of the string
                if string.find(substring) == 0:
                    # Add the value to the number
                    number += value
                    # Remove the matched substring from the string
                    string = string[len(substring) :]
                    break
        return number

    # __add__ method
    # Calculates the sum of two Roman numeral objects and returns a new Roman object.
    def __add__(self, rhs):
        # Initialize the sum of the two Roman numerals, and string result
        total = int(self) + int(rhs)
        result = ""
        # Convert the total back to Roman numeral format
        for i in range(3, 0, -1):
            result += NUMBER_TO_ROMAN[total - (total % 10**i)]
            total %= 10**i
        result += NUMBER_TO_ROMAN[total]
        return Roman(result)


# Output
t, r1, r2 = input().split()
a = Roman(r1)
b = Roman(r2)
if t == "1":
    print(a < b)
elif t == "2":
    print(int(a), int(b))
elif t == "3":
    print(str(a), str(b))
elif t == "4":
    print(int(a + b))
else:
    print(str(a + b))
```
