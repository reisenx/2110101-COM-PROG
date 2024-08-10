# Not guarantee 100/100 points on this code

# Input interested character
n = int(input())
character = []
for i in range(n):
    character.append(input().strip())

# As you can see a dialogue always starts with * and ends with "
# Example:
# *author123: "I would like to send a 
# special gift to you as a thank you." 
# *Main Character: "Gift?"

# Algorithm
# 1.) If a string start with * and if find() character in list not returns -1
# then put that line in a dialogue list
# 2.) If a string ends with ", put that line in a dialogue list then stop and find a string starts with *

# But there are hard cases which the dialogue ends between the string (" symbol not at the end of the string)
# Example:
# *Main Character: "Wow, really?" I'm surprised. 
# *Villian: "Here, you are."
    
# If you split *Main Character: "Wow, really?" I'm surprised. 
# You will get a list [*Main Character:, "Wow, really?", I'm surprised.]
# And you can see a data in index 1 have " at the end, so that means it's the end of the dialogue
# So if we join a string at index 0 and 1 we will get a string
# *Main Character: "Wow, really?"
# and the length of the string above is 31, so the index of " at the end is 30
# That means we can slice a string from index 0 to 30 which is [:30+1] and put it in the dialogue list

dialogue = []
IsDialogue = False
IsEnd = False
while True:
    line = input().strip()
    if(line == "END"):
        break
    else:
        # Check if the string starts with * and is a dialogue we interested
        if(line[0] == '*'):
            for name in character:
                if(line.find(name) != -1):
                    IsDialogue = True
                    break
        
        # Check if the dialogue ends
        # Split a dialogue to a list
        check = line.split()
        # Find a string in a list that ends with "
        for string in check:
            if(string[-1] == '\"'):
                IsEnd = True
                list_index = check.index(string)
                break
        # Find index of "
        if(IsEnd):
            index = len(" ".join(check[:list_index+1])) - 1

        # Put a dialogue in a list
        # If a dialogue starts with *, remove it
        if(IsDialogue):
            if(line[0] == '*' and (not IsEnd)):
                dialogue.append(line[1:])
            elif(not IsEnd):
                dialogue.append(line)
            elif(line[0] == '*' and IsEnd):
                dialogue.append(line[1:index+1])
            elif(IsEnd):
                dialogue.append(line[:index+1])
        
        # Reset the variables if the dialouge ends
        if(IsEnd):
            IsDialogue = False
            IsEnd = False

# Output
if(dialogue == []):
    print("Maybe wrong novel")
else:
    for line in dialogue:
        print(line)