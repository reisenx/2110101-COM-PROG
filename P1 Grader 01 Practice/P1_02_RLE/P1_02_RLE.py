# Input a command
command = str(input())

# Command: "str2RLE"
# Convert a string into a RLE code
if(command == "str2RLE"):
    # Input string
    string = str(input())

    # Create empty RLE string
    RLE = ""

    # Convert string into RLE
    # Example: ABBA --> A 1 B 2 A 1
    for i in range(0,len(string)):
        # Setup a matching character = character in index 0 and starts counting
        if(i == 0):
            character = string[0]
            count = 1
        # If the current character doesn't match anymore
        # Note it in to RLE, setup a new character then reset the variable
        elif(string[i] != character):
            RLE = RLE + character + " " + str(count) + " "
            character = string[i]
            count = 1
        # If the current character matches, then count them
        elif(string[i] == character):
            count += 1
    # Don't forget note the last one into RLE
    RLE += character + " " + str(count) + " "

    # Output RLE
    print(RLE)

# Command: "RLE2str"
# Convert RLE Code into a string
elif(command == "RLE2str"):
    # Input RLE Code
    RLE = str(input())

    # Create an empty string
    string = ""

    # Split a RLE string into a list
    # Example: "A 2 B 3 C 1" --> ['A','2','B','3','C','1']
    RLE = RLE.split()


    # Convert RLE into a string
    # Example: RLE = ['A','2','B','3','C','1']
    # Index 0,2,4,..., len(RLE)-2 is a character
    # Index 1,3,5,...., len(RLE)-1 is a number
    for i in range(len(RLE)//2):
        char = RLE[2*i]
        num = int(RLE[2*i + 1])
        string += char*num

    # Output a string
    print(string)

# Invalid command
else:
    print("Error")