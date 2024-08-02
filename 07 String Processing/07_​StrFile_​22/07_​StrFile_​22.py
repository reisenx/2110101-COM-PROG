# Input 2 strings and lower them into a lowercase string
text1 = input().lower()
text2 = input().lower()

# Create a list to count number of alphabet and number
alphabet = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
alphabet_count1 = [0]*26
number_count1 = [0]*10
alphabet_count2 = [0]*26
number_count2 = [0]*10

# Count alphabet and number of each string
for char in text1:
    if(char in alphabet):
        index = alphabet.find(char)
        alphabet_count1[index] += 1
    elif(char in number):
        index = number.find(char)
        number_count1[index] += 1

for char in text2:
    if(char in alphabet):
        index = alphabet.find(char)
        alphabet_count2[index] += 1
    elif(char in number):
        index = number.find(char)
        number_count2[index] += 1

# Output
# Anagram is a text that can be created by shuffle a letter of other text
# So anagram must have a same alphabet_count and number_count
if(alphabet_count1 == alphabet_count2 and number_count1 == number_count2):
    print("YES")
else:
    print("NO")