# --------------------------------------------------
# File Name : 2565_1_Q2_03.py
# Problem   : Colors
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input the color file and text file names
color_filename = input().strip()
text_filename = input().strip()

# Read the colors from the file and store them in a list
colors = []
with open(color_filename) as file:
    for line in file:
        for color in line.strip().split():
            colors.append(color.lower())

# Read the text from the file and store it in a string
text = ""
with open(text_filename) as file:
    for line in file:
        text += line.strip() + "\n"


# Mark HTML tags around the colors in the text
def mark_color(text, color):
    # Initialize the result with the original text
    result = text
    start_find_idx = 0
    while True:
        start_idx = result.lower().find(color, start_find_idx)
        end_idx = start_idx + len(color)
        if start_idx == -1:
            break

        before_color = result[:start_idx]
        current_color = result[start_idx:end_idx]
        after_color = result[end_idx:]
        result = f"{before_color}<{color}>{current_color}</>{after_color}"

        start_find_idx = end_idx + len(f"<{color}></>")
    return result


# Apply the color marking function for every color in the list
for color in colors:
    text = mark_color(text, color)
# Output the modified text with colors marked
print(text.strip())
