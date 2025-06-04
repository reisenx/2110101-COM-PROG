# Anagram is a text that can be created by shuffle a letter of other text
# Assume that the uppercase and lowercase is the same character
# Ignore all symbol
# Example: "Debit card" is an anagram of "Bad credit !!!"

# Create important variables
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Input 2 string and convert them into all lowercase
text01 = input()
text02 = input()
textl01 = text01.lower()
textl02 = text02.lower()

# Find all unique character in both string
# Example:
# text01 = "gentleman" --> unique_letter = ['g','e','n','t','l','m','a']
# text02 = "elegant woman" --> unique_letter = ['g','e','n','t','l','m','a','w','o']
unique_letter = []
for letter in textl01:
    if((letter in alphabet) and (letter not in unique_letter)):
        unique_letter.append(letter)
for letter in textl02:
    if((letter in alphabet) and (letter not in unique_letter)):
        unique_letter.append(letter)
# Sort all unique character
# Example: ['g','e','n','t','l','m','a','w','o'] --> ['a','e','g','l','m','n','o','t','w']
unique_letter.sort()

# Prepare a dictionary and count the unique letter
# Example: unique_letter = ['a','e','g','l','m','n','o','t','w']
# count01 = count02 = {'a':0, 'e':0, 'g':0, 'l':0, 'm':0, 'n':0, 'o':0, 't':0, 'w':0}
count01 = {}
count02 = {}
for letter in unique_letter:
    count01[letter] = 0
    count02[letter] = 0
# Count a letter
# Example: text01 = "gentleman" and text02 = "elegant woman"
# count01 = {'a':1, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':0, 't':1, 'w':0}
# count02 = {'a':2, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':1, 't':1, 'w':1}
for letter in textl01:
    if(letter in count01):
        count01[letter] += 1
for letter in textl02:
    if(letter in count02):
        count02[letter] += 1

# Find the dictionary of anagram string letter count
# The letter count of the anagram string created using 2 input string is minimum count of each unique letter
# Example:
# count01 = {'a':1, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':0, 't':1, 'w':0}
# count02 = {'a':2, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':1, 't':1, 'w':1}
# count_anagram = {'a':1, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':0, 't':1, 'w':0}
count_anagram = {}
for letter in unique_letter:
    count_anagram[letter] = min(count01[letter], count02[letter])

# Find how many letter needed to delete in each string
# Example:
# count01 = {'a':1, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':0, 't':1, 'w':0}
# count02 = {'a':2, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':1, 't':1, 'w':1}
# count_anagram = {'a':1, 'e':2, 'g':1, 'l':1, 'm':1, 'n':2, 'o':0, 't':1, 'w':0}
# delete01 = {}
# delete02 = {'a':1, 'o':1, 'w':1}
delete01 = {}
delete02 = {}
# Find delete01
for letter in unique_letter:
    temp_delete = count01[letter] - count_anagram[letter]
    if(temp_delete > 0):
        delete01[letter] = temp_delete
# Find delete02
for letter in unique_letter:
    temp_delete = count02[letter] - count_anagram[letter]
    if(temp_delete > 0):
        delete02[letter] = temp_delete

# Output
print(text01)
if(delete01 == {}):
    print(" -", "None")
else:
    for letter in delete01:
        if(delete01[letter] == 1):
            print(" -", "remove", delete01[letter], letter)
        else:
            print(" -", "remove", delete01[letter], letter + "'s")
print(text02)
if(delete02 == {}):
    print(" -", "None")
else:
    for letter in delete02:
        if(delete02[letter] == 1):
            print(" -", "remove", delete02[letter], letter)
        else:
            print(" -", "remove", delete02[letter], letter + "'s")