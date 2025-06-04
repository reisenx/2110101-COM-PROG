# ---------- Algorithm ----------
# Example:
# Pasta is a type of food typically made
# from an unleavened dough of wheat
# flour mixed with water or eggs, and
# formed into sheets or other shapes,
# then cooked by boiling or baking.

# Step 1: Input and convert message
# - Input searching word
# - output = 1 line string Input (convert newline to '\n')
# - passage = 1 line string Input (convert newline to space)

# Step 2: Find and insert <found> and </found>
# Given start = 0
# Loop process until passage.find(search, start) is -1 (not found)
# - Given start = passage.find(search, start)
# - Given end = start + len(search)
# - Insert <found> at start (Insert to both passage and output)
# - Insert </found> at end (Insert to both passage and output)
# - Given start = end + len("<found>") + len("</found>")
# NOTE: Use .lower() to find search in passage (Case Insensitive)
# Example:
# output = "... unleavened dough of wh<found>eat\nflour</found> mixed with ..."
# passage = "... unleavened dough of wh<found>eat flour</found> mixed with ..."

# Step 1: Input and convert message
search = input().strip()
N = int(input())
passage = ""
output = ""
for i in range(N):
    line = input().strip()
    passage += line + " "
    output += line + "\n"

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
    output = output[0:start] + "<found>" + output[start:end] + "</found>" + output[end:]
    # Find new start
    start = end + len("<found>") + len("</found>")
    
# Output
print(output.strip())