# Input a string and convert them all to lowercase
text = input().lower()

# Create an alphabet list
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Count an alphabet in a text and put them in a dictionary
# Example: "AaBbbbbbbCcDddd" --> {'a':2, 'b':7, 'c':2, 'd':4}
count = {}
for char in text:
    if(char in alphabet):
        if(char not in count):
            count[char] = 1
        else:
            count[char] += 1

# Put the data in a dictionary into a list and sort
# Example: {'a': 2, 'b': 7, 'c': 2, 'd': 4} --> [[-7,'a'],[-4,'d'],[-2,'a'],[-2,'c']]
# Make a count number into a negative because we need to sort them in descending order
# Don't use char_list.sort(reverse = True) becuase [2,'c'] will be in front of [2,'a'] which is incorrect
sorted_count = []
for char,num in count.items():
    sorted_count.append([-1*num, char])
sorted_count.sort()

# Output
for num,char in sorted_count:
    print(char, "->", -1*num)