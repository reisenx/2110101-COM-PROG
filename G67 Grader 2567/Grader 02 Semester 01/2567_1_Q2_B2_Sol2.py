# ---------- Algorithm ----------
# Example:
# Pasta is a type of food typically made    | wordCount = 8 [0:8]
# from an unleavened dough of wheat         | wordCount = 6 [8:14]
# flour mixed with water or eggs, and       | wordCount = 7 [14:21]
# formed into sheets or other shapes,       | wordCount = 6 [21:27]
# then cooked by boiling or baking.         | wordCount = 6 [27:33]

# Step 1: Input and convert message
# - Input searching word
# - Convert all input into 1 line string (convert newline to space)
# - Find [start:stop] position of each line
# Example:
# search  = "eat Flour"
# passage = "... unleavened dough of wheat flour mixed with ..."
# positions = [[0,8], [8,14], [14,21], [21,27], [27,33]]

# Step 2: Find and insert <found> and </found>
# Given start = 0
# Loop process until passage.find(search, start) is -1 (not found)
# - Given start = passage.find(search, start)
# - Given end = start + len(search)
# - Insert <found> at start
# - Insert </found> at end
# - Given start = end + len("<found>") + len("</found>")
# NOTE: Use .lower() to find search in passage (Case Insensitive)
# Example:
# passage = "... unleavened dough of wh<found>eat flour</found> mixed with ..."

# Step 3: Output
# - Split 'passage' into a list
# - Use position to output each line
# Example:
# passage = [..., "unleavened", "dough", "of", "wh<found>eat", "flour</found>", "mixed", "with", ...]
# ------------------------------

# Step 1: Input and convert message
# Input search message
search = input().strip()
N = int(input())
# Convert into one-line message and find [start,end] position of each line
passage = ""
positions = []
start,end = 0,0
for i in range(N):
    # Add line to passage
    line = input().strip()
    passage += line + " "
    # Find [start,end] of each line
    end += len(line.split())
    positions.append([start, end])
    start += len(line.split())

# Step 2: Find and insert <found> and </found>
start,end = 0,0
while(True):
    # Find position to insert
    start = (passage.lower()).find(search.lower(), start)
    end = start + len(search)
    # If not found (start = -1), then break the loop
    if(start == -1):
        break
    # Insert <found> and </found>
    passage = passage[0:start] + "<found>" + passage[start:end] + "</found>" + passage[end:]
    # Find new start
    start = end + len("<found>") + len("</found>")

# Step 3: Output
# Split passage to a list
passage = passage.split()
# Output item by using positions
for start,end in positions:
    print(" ".join(passage[start:end]))