# --------------------------------------------------
# File Name : 2566_2_Q2_03.py
# Problem   : Text Formatter
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize the length limit
LENGTH_LIMIT = 50
# Read the filename
filename = input().strip()

# Extract words from the file and store them in a list
words = []
with open(filename) as file:
    for line in file:
        if line.strip() != "":
            words += line.strip().split("_")

# Print the header
print("-" * LENGTH_LIMIT)
# Initialize the start index for the first word
start_idx = 0
# Output the words in lines not exceeding the length limit
while start_idx < len(words):
    # Initialize the end index and current line length
    end_idx = start_idx + 1
    length = len(words[start_idx])
    # Calculate the end index for the current line
    while end_idx < len(words):
        # Calculate the length of the current line if the next word is added
        length += len(words[end_idx]) + 1
        # If the length exceeds the limit, break the loop
        if length > LENGTH_LIMIT:
            break
        # Otherwise, include the next word
        end_idx += 1

    # Output the current line
    line = "_".join(words[start_idx:end_idx])
    print(line)
    # Update the start index for the next iteration
    start_idx = end_idx
