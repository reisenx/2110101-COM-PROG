# Example testcase filename 1: text1.txt
# Example testcase filename 2: text2.txt

# Open a file
filename = input().strip()
file = open(filename,"r")

# Read every line in a file, split them with '_' then convert them all to a list of words
words = []
for line in file:
    # Strip a line to get rid of "\n" at the end of each line
    line = line.strip()
    # Considered only non-empty line
    if(line != ""):
        temp = line.split("_")
        for item in temp:
            words.append(item)

# Output
# In the first line, output 50 "-"
print("-"*50)

# Algorithm
# 1.) Setup inital value start = 0 and end = 0
# 2.) Find the length of line = "_".join(words[start:end])
# - If the length is less than 50, Increase 'end' by 1
# - If the length is more than 50, Output "_".join(words[start:end-1])
#   and setup start = end-1 and end = end-1
# 3.) If it reached the end of the 'words' list and the length less than 50, output it then break

# Example:
# words = ['Mary','had','a','little','lamb','little','lamb','little','lamb','Mary','had','a','little',
#          'lamb','its','fleece','was','white','as','snow']

# Process
# Loop 1: start = 0 | end = 0 | Length = 0
# > line = ""
# Loop 2: start = 0 | end = 1 | Length = 4
# > line = "Mary"
# Loop 3: start = 0 | end = 2 | Length = 8
# > line = "Mary_had"
# ...
# Loop 10: start = 0 | end = 9 | Length = 46
# > line = "Mary_had_a_little_lamb_little_lamb_little_lamb"    
# Loop 11: start = 0 | end = 10 | Length = 51
# > line = "Mary_had_a_little_lamb_little_lamb_little_lamb_Mary"
# > Output "Mary_had_a_little_lamb_little_lamb_little_lamb"
# > Setup start = 9, end = 9

# Loop 12: start = 9 | end = 9 | Length = 0
# > line = ""
# Loop 13: start = 9 | end = 10 | Length = 4
# > line = "Mary"
# Loop 14: start = 9 | end = 11 | Length = 8
# > line = "Mary_had"
# ...
# Loop 22: start = 9 | end = 19 | Length = 46
# > line = "Mary_had_a_little_lamb_its_fleece_was_white_as"
# Loop 23: start = 9 | end = 20 | Length = 51
# > line = "Mary_had_a_little_lamb_its_fleece_was_white_as_snow"
# > Output "Mary_had_a_little_lamb_its_fleece_was_white_as"
# > Setup start = 19, end = 19

# Loop 24: start = 19 | end = 19 | Length = 0
# > line = ""
# Loop 25: start = 19 | end = 20 | Length = 4
# > line = "snow"
# Loop 26: start = 19 | end = 21 (end > len(words))
# > Output "snow", then break a loop
start = 0
end = 0
while(start < len(words)):
    line = "_".join(words[start:end])
    if(len(line) <= 50 and end > len(words)):
        print("_".join(words[start:end-1]))
        break
    elif(len(line) <= 50):
        end += 1
    else:
        print("_".join(words[start:end-1]))
        start = end - 1
        end = end - 1

# Close a file
file.close()