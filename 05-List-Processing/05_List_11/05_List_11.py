# --------------------------------------------------
# File Name : 05_List_11.py
# Problem   : Missing Digits
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input text
text = input().strip()

# Initialize a list of missing digits
missing_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Remove digits found in the input text
for char in text:
    if char in missing_digits:
        missing_digits.remove(char)

# Output the missing digits
if len(missing_digits) > 0:
    print(",".join(missing_digits))
else:
    print("None")
