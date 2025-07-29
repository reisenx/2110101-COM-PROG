# --------------------------------------------------
# File Name : 2567_1_Q2_B2.py
# Problem   : Text Search
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Replacement offset for "<found>" and "</found>" tags
REPLACEMENT_OFFSET = len("<found>") + len("</found>")

# Input replacement target
target = input().strip().lower()

# Initialize query passage and output strings
query_passage = ""
output = ""

# Input number of lines and read each line of the passage
n = int(input())
for _ in range(n):
    # Input each line of the passage
    line = input().strip()

    # Add lowercase line and replace newline characters with spaces
    # to query passage for case-insensitive search
    query_passage += line.lower() + " "

    # Add the exact passage line to the output string
    output += line + "\n"

# Remove trailing spaces from the query passage
query_passage = query_passage.strip()

# Initialize variables for searching and replacing
replacement_count = 0
find_start_idx = 0

while True:
    # Find the next occurrence of the target in the query passage
    start_idx = query_passage.find(target, find_start_idx)
    end_idx = start_idx + len(target)

    # Update the start index for the next search
    find_start_idx = end_idx

    # If no more occurrences are found, break the loop
    if start_idx == -1:
        break
    # Add the offset to the start and end indices for replacement on the output string
    start_idx += REPLACEMENT_OFFSET * replacement_count
    end_idx += REPLACEMENT_OFFSET * replacement_count

    # Add "<found>" and "</found>" tags around the found target in the output string
    output = (
        output[:start_idx]
        + "<found>"
        + output[start_idx:end_idx]
        + "</found>"
        + output[end_idx:]
    )

    # Increment the replacement count
    replacement_count += 1

# Output the final result
print(output.strip())
