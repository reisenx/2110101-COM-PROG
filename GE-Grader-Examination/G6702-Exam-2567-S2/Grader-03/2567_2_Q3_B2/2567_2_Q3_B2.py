# --------------------------------------------------
# File Name : 2567_2_Q3_B2.py
# Problem   : License Plate Extractor
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------


# Function to extract license plates from a string
def get_plates_from_str(raw_data: str) -> list[str]:
    # Initialize an empty string to hold modified data
    modified_data = ""

    # Iterate through the characters in the raw string
    for i in range(len(raw_data) - 1):
        # Check the pattern of one digits followed by a non-digit character
        if raw_data[i].isdigit() and not raw_data[i + 1].isdigit():
            # Add whitespace before the digit for splitting
            modified_data += " " + raw_data[i]
        # The current character does not match the pattern
        else:
            modified_data += raw_data[i]
    # Add the last character to modified_data
    modified_data += raw_data[-1]

    # Split the modified data by whitespace and return the list of plates
    return modified_data.strip().split()


# Function to read a file and extract license plates
def get_plates_from_file(filename: str) -> list[str]:
    # Initialize an empty list to hold the plates
    plates = []

    # Open the file, read each line and extract license plates
    with open(filename, encoding="utf-8") as file:
        for line in file:
            plates += get_plates_from_str(line.strip())

    # Return the list of all license plates in the file
    return plates


# Main function
def main():
    # Input the filename
    filename = input().strip()

    # Extract the license plates from the file
    plates = get_plates_from_file(filename)

    # Output all the license plates
    for plate in plates:
        print(plate)


# Run the main function
main()
