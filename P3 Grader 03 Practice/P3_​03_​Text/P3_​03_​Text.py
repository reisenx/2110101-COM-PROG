# This function can return a ruler string
def ruler(k):
    line = ""
    for i in range(k//10):
        line += "-"*9 + str(i+1)
    line += "-"*(k%10)
    return line

# This function can read text in a file and convert to a list of all words
def file_to_wordslist(filename):
    file = open(filename, "r")
    wordslist = []
    for line in file:
        data = line.strip().split('.')
        for item in data:
            wordslist.append(item)
    file.close()
    return wordslist

# Input filename and k
filename = input().strip()
k = int(input())

# Output ruler
print(ruler(k))

# Get a list of words
words = file_to_wordslist(filename)

# Rearrange the text
# Algorithm is similar to 2566_2_Quiz_2_3.py
start = 0
end = 0
while(start < len(words)):
    # There's no '.' at the front and the end of each line so we need to strip '.' every loop
    line = ".".join(words[start:end]).strip('.')
    # Stop when reached the end of the 'words' list
    if(end > len(words)):
        print(line)
        break
    # If using only 1 words but the len(line) already exceed 'k', output the line
    elif(end-start == 1 and len(line) > k):
        print(line)
        start = end
    # If len(line) exceed k, output the line.
    elif(len(line) > k):
        print(".".join(words[start:end-1]).strip('.'))
        start = end-1
        end = end-1
    # If len(line) is less than k, add 'end' by 1 until it exceed 'k'
    else:
        end += 1