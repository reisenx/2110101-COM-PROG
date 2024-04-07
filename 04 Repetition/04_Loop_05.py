# Input 2 string
word = str(input())
sentence = str(input())

# Replace symbol from the string to " "
symbol = ["\"", "(", ")", ",", ".", "\'"]
for item in symbol:
    sentence = sentence.replace(item," ")

# Split a sentences into a list
words_list = sentence.split()

# Set initial word count = 0
count = 0

# Check how many word in a list is the same to input word 
for item in words_list:
    if(item == word):
        count += 1

# Output the word count
print(count)