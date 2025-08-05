# --------------------------------------------------
# File Name : 2565_2_Q2_02.py
# Problem   : Matching Rule
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Convert a pattern string to a pattern list which contains
# each character and its matching rule.
def pattern_to_list(pattern_str):
    # Add spaces around brackets and parentheses for splitting
    temp = (
        pattern_str.replace("[", " [")
        .replace("]", "] ")
        .replace("(", " (")
        .replace(")", ") ")
    )

    # Split the string into parts and create a pattern list
    pattern = []
    for part in temp.split():
        # Check if the part has parentheses which indicate a exclude rule
        if part[0] + part[-1] == "()":
            pattern.append([part[1:-1], "exclude"])
        # Check if the part has brackets which indicate a include rule
        elif part[0] + part[-1] == "[]":
            pattern.append([part[1:-1], "include"])
        # Otherwise, it is a single character with exact or any rule
        else:
            # Add each character in the part to the pattern list
            for char in part:
                if char == "?":
                    pattern.append(["?", "any"])
                else:
                    pattern.append([char, "exact"])
    # Return the pattern list
    return pattern


# Match a text against a pattern list
def match(text, pattern_str):
    # Convert the pattern string to a pattern list
    pattern = pattern_to_list(pattern_str)
    # Check if the length of text matches the length of pattern
    if len(text) != len(pattern):
        return False

    # Check each character in the text against the pattern
    for i in range(len(text)):
        # Extract the characters and rule from the pattern list
        chars, rule = pattern[i]
        # Check if the character in text matches the rule
        if (
            (rule == "exact" and text[i] != chars)
            or (rule == "include" and text[i] not in chars)
            or (rule == "exclude" and text[i] in chars)
        ):
            return False
    return True


# Execute a input string as code
exec(input().strip())
