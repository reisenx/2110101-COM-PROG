# --------------------------------------------------
# File Name : 2565_2_Q2_03.py
# Problem   : Complex Replace
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------


# Find the leftmost replaceable pattern in the text
def find_leftmost_replace(text, patterns, replacements):
    # Find all patterns that are replaceable in the text
    all_replaceable = []
    for i in range(len(patterns)):
        # Extract the pattern and replacement
        pattern = patterns[i]
        replacement = replacements[i]
        # Find the index of the first occurrence of the pattern
        idx = text.find(pattern)
        # If the pattern is found, add it to the list of replaceable patterns
        if idx != -1:
            all_replaceable.append([idx, pattern, replacement])

    # If no patterns are found, return [-1, "", ""]
    if len(all_replaceable) == 0:
        return [-1, "", ""]
    # Sort the replaceable patterns by their index and return the leftmost one
    all_replaceable.sort()
    return all_replaceable[0]


# Replace the leftmost pattern in the text with its replacement
def complex_replace(text, patterns, replacements):
    # Find the leftmost replaceable pattern
    idx, pattern, replacement = find_leftmost_replace(text, patterns, replacements)
    # If no pattern is found, return the original text
    if idx == -1:
        return text
    # Replace the pattern with its replacement and return the modified text
    return f"{text[:idx]}<{replacement}>{text[idx + len(pattern):]}"


# Execute a input string as code
exec(input().strip())
