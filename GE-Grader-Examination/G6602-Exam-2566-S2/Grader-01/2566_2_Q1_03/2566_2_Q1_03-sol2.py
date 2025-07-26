# --------------------------------------------------
# File Name : 2566_2_Q1_03-sol2.py
# Problem   : Repeat Count
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Count the number of times a pattern repeats in a text
def get_repeat_count(text: str, pattern: str) -> int:
    # Initialize the index and repeat count
    idx = 0
    repeat = 0
    max_repeat = 0
    # Iterate through the text to find the pattern
    while idx < len(text):
        # If the pattern is found, increase the repeat count
        # and move the index forward by the length of the pattern
        if text[idx : idx + len(pattern)] == pattern:
            repeat += 1
            idx += len(pattern)
        # If the pattern is not found, check if we have a maximum repeat
        # and reset the repeat count
        else:
            max_repeat = max(max_repeat, repeat)
            repeat = 0
            idx += 1
    # Do not forget to check the last repeat count
    max_repeat = max(max_repeat, repeat)

    # Return the maximum repeat count if greater than 1
    if max_repeat > 1:
        return max_repeat
    # If no repeat found, repeat count is 0
    return 0


# Read the pattern and the number of test cases
pattern = input().strip()
n = int(input())
# Read each test case and output the repeat count
for _ in range(n):
    text = input().strip()
    print(get_repeat_count(text, pattern))
