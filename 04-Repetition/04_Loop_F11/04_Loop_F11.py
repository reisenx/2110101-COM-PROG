# --------------------------------------------------
# File Name : 04_Loop_F11.py
# Problem   : RLE (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------


def RLE(text: str) -> list:
    # Empty string check
    if text == "":
        return []

    # Construct RLE list
    rle = []

    # Initialize counter
    char = text[0]
    count = 1

    # Iterate through the text
    for i in range(1, len(text)):
        if text[i] == char:
            count += 1
        else:
            rle += [[char, count]]
            char = text[i]
            count = 1

    # Append the last character and its count
    rle += [[char, count]]
    # Return the RLE list
    return rle


# Execute input string as code
exec(input())
