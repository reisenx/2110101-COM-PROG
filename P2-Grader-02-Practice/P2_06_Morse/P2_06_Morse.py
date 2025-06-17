# --------------------------------------------------
# File Name : P2_06_Morse.py
# Problem   : Part-II Morse Code
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize Morse code dictionary
CHAR_TO_MORSE = {}
MORSE_TO_CHAR = {}


# Read Morse code mappings from the input
def read_mappings(line: str) -> None:
    # Replace brackets with whitespace
    line = line.replace("[", " ").replace("]", " ")
    # Split the line into character and Morse code pairs
    mappings = line.split()
    # Store Morse code mappings in dictionaries
    for i in range(0, len(mappings), 2):
        char = mappings[i]
        morse_code = mappings[i + 1]
        CHAR_TO_MORSE[char] = morse_code
        MORSE_TO_CHAR[morse_code] = char


# Convert Morse code to text
def morse_to_text(morse_code: str) -> None:
    result = ""
    for code in morse_code.split():
        if code in MORSE_TO_CHAR:
            result += MORSE_TO_CHAR[code]
        else:
            result = f"Invalid : {morse_code}"
            break
    print(result)


# Convert text to Morse code
def text_to_morse(text: str) -> None:
    result = []
    for char in text:
        if char in CHAR_TO_MORSE:
            result.append(CHAR_TO_MORSE[char])
        else:
            result = [f"Invalid : {text}"]
            break
    print(" ".join(result))


# Input filename
filename = input().strip()

# Read Morse code mappings from the file
with open(filename) as file:
    # Read command from the first line
    cmd = file.readline().strip()

    # Read the second line for Morse code mappings
    line = file.readline().strip()
    read_mappings(line)

    # Process the command for the rest of the file
    if cmd == "M2T":
        for line in file:
            morse_to_text(line.strip())
    elif cmd == "T2M":
        for line in file:
            text_to_morse(line.strip())
    else:
        print("Invalid code")
