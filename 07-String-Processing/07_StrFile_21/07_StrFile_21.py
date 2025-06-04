# Input an text and encode with ROT13 until the word "end"

# Create a string with an alphabet
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ROT13 encryption
# Convert a letter in the first line into a second line
# Convert a letter in the second line into a first line
# A B C D E F G H I J K L M
# | | | | | | | | | | | | |
# N O P Q R S T U V W X Y Z
ROT13_list = []
while True:
    text = input()
    ROT13 = ""
    if(text == "end"):
        break
    else:
        for char in text:
            # The character is in between a-m
            if(char in lowercase[0:13]):
                index = lowercase.find(char)
                ROT13 += lowercase[index + 13]
            # The character is in between n-z
            elif(char in lowercase[13:26]):
                index = lowercase.find(char)
                ROT13 += lowercase[index - 13]
            # The character is in between A-M
            elif(char in uppercase[0:13]):
                index = uppercase.find(char)
                ROT13 += uppercase[index + 13]
            # The character is in between N-Z
            elif(char in uppercase[13:26]):
                index = uppercase.find(char)
                ROT13 += uppercase[index - 13]
            # A character that is not an alphabet
            else:
                ROT13 += char
            
        # Put an encrypted text in a list
        ROT13_list.append(ROT13)

# Output
for item in ROT13_list:
    print(item)