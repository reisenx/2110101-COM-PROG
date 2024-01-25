# Input a string
func = str(input())

# str2RLE - Convert a string into a RLE Code
if(func == "str2RLE"):
    # Input string
    txt = str(input())

    # Create empty RLE string
    RLE = ""

    # Convert string into RLE
    # Example: ABBA --> A 1 B 2 A 1
    for i in range(0,len(txt)):
        # Setup a matching character = character in index 0 and starts counting
        if(i==0):
            character = txt[0]
            count = 1
        # If the current character doesn't match anymore
        # Note it in to RLE, setup a new character then reset the variable
        elif(txt[i] != character):
            RLE = RLE + character + " " + str(count) + " "
            character = txt[i]
            count = 1
        # If the current character matches, then count them
        elif(txt[i] == character):
            count = count + 1
    # Don't forget note the last one into RLE
    RLE = RLE + character + " " + str(count) + " "

    # Output RLE
    print(RLE)

# RLE2str - Convert RLE Code into a string
elif(func == "RLE2str"):
    #Input RLE Code
    RLE = str(input())

    # Create an empty string
    txt = ""

    # Split a RLE string into a list
    # Example: "A 2 B 3 C 1" --> ["A","2","B","3","C","1"]
    data = RLE.split()

    # Convert RLE into a string
    # Example: data = ["A","2","B","3","C","1"]
    # Index 0,2,4,..., len(data)-2 is a character
    # Index 1,3,5,...., len(data)-1 is a number
    for i in range(0,int(len(data)/2)):
        txt = txt + data[2*i]*int(data[2*i + 1])
    
    # Output a string
    print(txt)

# Invalid function
else:
    print("Error")