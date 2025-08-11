# --------------------------------------------------
# File Name : 12_Class_35.py
# Problem   : Roman Numeral
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# Dictionary to convert between numbers and Roman numerals
NUMBER_TO_ROMAN = {
    1000: ("", "M", "MM", "MMM", "MMMM"),
    100: ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
    10: ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
    1: ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
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

        # Convert the total back to Roman numeral format
        result = ""
        for value, roman_numerals in NUMBER_TO_ROMAN.items():
            idx = total // value
            result += roman_numerals[idx]
            total %= value

        # Return a new Roman object with the resulting Roman numeral
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
