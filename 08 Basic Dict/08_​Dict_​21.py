# Input a string and convert them all to lowercase
text = input().lower()

# Create an alphabet list
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Count an alphabet in a text and put them in a dictionary
# Example: "AaBbbbbbbCcDddd" --> {'a': 2, 'b': 7, 'c': 2, 'd': 4}
char_dict = {}
for i in range(len(text)):
    if(text[i] in alphabet):
        if(text[i] not in char_dict):
            char_dict[text[i]] = 1
        else:
            char_dict[text[i]] += 1

# Put the data in a dictionary into a list and sort
# Example: {'a': 2, 'b': 7, 'c': 2, 'd': 4} --> [[-7,'a'],[-4,'d'],[-2,'a'],[-2,'c']]
# Make a count number into a negative because we need to sort them in descending order
# Don't use char_list.sort(reverse = True) becuase [2,'c'] will be in front of [2,'a'] which is incorrect
char_list = []
for key in char_dict:
    char_list.append([-1*char_dict[key], key])
char_list.sort()

# Output
for i in range(len(char_list)):
    print(char_list[i][1],"->",-1*char_list[i][0])