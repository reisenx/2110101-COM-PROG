# ---------- Algorithm ----------
# Example:
# Python is a HIGH-LEVEL
# programming language.
# I love Python.

# Step 1: Input and convert message
# - Input searching word and replace word
# - output = 1 line string Input (convert newline to '\n')
# - passage = 1 line string Input (convert newline to space)

# Step 2: Find and replace string
# Given start = 0
# Loop process until passage.find(search, start) is -1 (not found)
# - Given start = passage.find(search, start)
# - Given end = start + len(search)
# - Replace a string (Replace to both passage and output)
# - Given start = start + len(replace)
# NOTE: Use .lower() to find search in passage (Case Insensitive)
# Example (Before replace):
# output = "Python is a HIGH-LEVEL\nprogramming language.\nI love Python."
# passage = "Python is a HIGH-LEVEL programming language. I love Python."
# Example (After replace):
# output = "Python is a popular language.\nI love Python."
# passage = "Python is a popular language. I love Python."

# Step 1: Input and convert message
search, replace = input().strip().split('/')
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
    # Replace a string
    passage = passage[0:start] + replace + passage[end:]
    output = output[0:start] + replace + output[end:]
    # Find new start
    start += len(replace)
    
# Output
print(output.strip())