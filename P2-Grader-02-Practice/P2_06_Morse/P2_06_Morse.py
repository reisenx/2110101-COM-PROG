# Input the name of a file
filename = input().strip()

# Open the file
file = open(filename, "r")

# Get a command from the first line of the file
# Get a pattern from the second line of the file
command = file.readline()
pattern = file.readline()
command = command.strip()
pattern = pattern.strip()

# Check if the command is valid or not
IsCommandValid = True
if(command != "T2M" and command != "M2T"):
    IsCommandValid = False

# Convert a pattern to a dictionary
# Example: pattern = "[A].-[B]-...[C]-.-.[E].["
# str2morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'E':'.'}
# morse2str = {'.-':'A', '-...':'B', '-.-.':'C', '.':'E'}

# Algorithm
# 1.) Replace ']' with '['
# Example: "[A].-[B]-...[C]-.-.[E].[" --> "[A[.-[B[-...[C[-.-.[E[.["
# 2.) Strip the string using '['
# Example: "[A[.-[B[-...[C[-.-.[E[.[" --> "A[.-[B[-...[C[-.-.[E[."
# 3.) Split the string using '['
# Example: "A[.-[B[-...[C[-.-.[E[." --> ['A', '.-', 'B', '-...', 'C', '-.-.', 'E', '.']
# 4.) Convert a list into str2morse and morse2str dictionary
str2morse = {}
morse2str = {}
pattern_list = pattern.replace(']','[').strip('[').split('[')
for i in range(len(pattern_list)//2):
    str2morse[pattern_list[2*i]] = pattern_list[2*i + 1]
    morse2str[pattern_list[2*i + 1]] = pattern_list[2*i]

# Read the rest of the file
while True:
    text = file.readline()
    # Invalid command
    if(not IsCommandValid):
        print("Invalid code")
        break
    # When the line is empty, readline() function will return an empty srting
    elif(text == ""):
        break
    else:
        # "T2M" command is to convert text to a morse code
        # Example: "BBE" --> "-... -... ."
        if(command == "T2M"):
            text = text.strip()
            morse = ""
            IsValid = True
            # Convert text to a string if valid (All letter in input are in the str2morse dictionary)
            for letter in text:
                if(letter in str2morse):
                    morse += str2morse[letter] + " "
                else:
                    IsValid = False
                    break
            # Output
            if(IsValid):
                print(morse.strip())
            else:
                print("Invalid :", text)
        
        # "M2T" command is to convert morse code to a text
        # All letter in the morse code will be seperated by a spacebar
        # Example: "-... -... ." --> "BBE"
        elif(command == "M2T"):
            # Split a morse code to get a list
            # Example: "-... -... ." --> ['-...', '-...', '.']
            morse = text.strip().split()
            string = ""
            IsValid = True
            # Convert text to a string if valid (All morse code in input are in the morse2str dictionary)
            for code in morse:
                if(code in morse2str):
                    string += morse2str[code]
                else:
                    IsValid = False
                    break
            # Output
            if(IsValid):
                print(string)
            else:
                print("Invalid :", text.strip())

# Close the file
file.close()