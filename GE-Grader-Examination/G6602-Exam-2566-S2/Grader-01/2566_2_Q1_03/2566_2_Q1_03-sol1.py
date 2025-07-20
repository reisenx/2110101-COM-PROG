# --------------------------------------------------
# File Name : 2566_2_Q1_03-sol1.py
# Problem   : Repeat Count
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Count the number of times a pattern repeats in a text
def get_repeat_count(text: str, pattern: str) -> int:
    # Initialize the repeat as maximum possible repeats
    repeat = len(text) // len(pattern)
    # Decrease the repeat count until the pattern is found
    while repeat > 1:
        if pattern * repeat in text:
            return repeat
        repeat -= 1
    # If no repeat found, return 0
    return 0


# Read the pattern and the number of test cases
pattern = input().strip()
n = int(input())
# Read each test case and output the repeat count
for _ in range(n):
    text = input().strip()
    print(get_repeat_count(text, pattern))
