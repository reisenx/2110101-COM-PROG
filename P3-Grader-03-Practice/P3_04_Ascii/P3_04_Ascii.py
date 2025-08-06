# --------------------------------------------------
# File Name : P3_04_Ascii.py
# Problem   : Part-III ASCII Text
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Extract text from a file and return it as a list of lines.
def extract_image_from_file(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


# Check if all characters in each column of the image are dots ('.')
def get_column_all_dots(image):
    rows, cols = len(image), len(image[0])
    result = [True] * cols
    for col in range(cols):
        for row in range(rows):
            if image[row][col] != ".":
                result[col] = False
                break
    return result


# Get the left strip of columns where all characters are dots ('.').
def get_column_left_strip(is_all_dots):
    cols = len(is_all_dots)
    for idx in range(cols):
        if not is_all_dots[idx]:
            break
    return [True] * idx + [False] * (cols - idx)


# Get the right strip of columns where all characters are dots ('.').
def get_column_right_strip(is_all_dots):
    cols = len(is_all_dots)
    for idx in range(cols):
        if not is_all_dots[-idx - 1]:
            break
    return [False] * (cols - idx) + [True] * idx


# Get the strip of columns where all characters are dots ('.') on either side.
def get_column_strip(is_all_dots):
    cols = len(is_all_dots)
    left_strip = get_column_left_strip(is_all_dots)
    right_strip = get_column_right_strip(is_all_dots)
    return [left_strip[i] or right_strip[i] for i in range(cols)]


# Output the image without the columns that are all dots ('.').
def print_image(image, is_strip):
    for row in image:
        line = ""
        for col in range(len(row)):
            if not is_strip[col]:
                line += row[col]
        print(line)


# Input filename and command
filename = input().strip()
command = input().strip()

# Extract the image from the file
image = extract_image_from_file(filename)
# Get the columns where all characters are dots ('.')
is_all_dots = get_column_all_dots(image)
# Print the image based on the command
if command == "STRIP_ALL":
    print_image(image, is_all_dots)
elif command == "STRIP":
    is_strip = get_column_strip(is_all_dots)
    print_image(image, is_strip)
elif command == "LSTRIP":
    is_strip = get_column_left_strip(is_all_dots)
    print_image(image, is_strip)
elif command == "RSTRIP":
    is_strip = get_column_right_strip(is_all_dots)
    print_image(image, is_strip)
else:
    print("Invalid command")
