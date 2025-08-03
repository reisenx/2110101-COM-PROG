# --------------------------------------------------
# File Name : 2567_2_Q2_B2.py
# Problem   : Text Replace in File
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------


# Read text from a file and return as a single-line string
def get_text_from_file(filename: str) -> str:
    text = ""
    with open(filename) as file:
        for line in file:
            text += line.strip() + " "
    return text.strip()


# Get the maximum line length from the file
def get_max_line_length(filename: str) -> int:
    max_length = 0
    with open(filename) as file:
        for line in file:
            max_length = max(max_length, len(line.strip()))
    return max_length


# Replace occurrences of target with replacement in the text (case-insensitive)
def replace_on_text(text: str, target: str, replacement: str) -> str:
    # Initialize the result with the original text
    result = text
    # Initialize the index for finding occurrences
    find_idx = 0

    # Loop to find and replace all occurrences of the target
    while True:
        # Find the next occurrence of the target in a case-insensitive manner
        start_idx = result.lower().find(target.lower(), find_idx)

        # If no more occurrences are found, break the loop
        if start_idx == -1:
            break

        # Calculate the end index of the found target
        end_idx = start_idx + len(target)

        # Replace the found target with the replacement in the result
        result = result[:start_idx] + replacement + result[end_idx:]

        # Update the find index to continue searching after the replaced text
        find_idx = start_idx + len(replacement)

    # Return the modified text
    return result


def display_text_on_limit(text: str, limit: int) -> None:
    # Split the text into words
    words = text.split()

    # Initialize the start index for the first word
    start_idx = 0

    # Output the words in lines not exceeding the length limit
    while start_idx < len(words):
        # Initialize the end index and current line length
        end_idx = start_idx + 1
        current_length = len(words[start_idx])

        # Calculate the end index for the current line
        while end_idx < len(words):
            # Calculate the length of the current line if the next word is added
            current_length += len(words[end_idx]) + 1

            # If the length exceeds the limit, break the loop
            if current_length > limit:
                break
            # Otherwise, include the next word
            end_idx += 1

        # Output the current line
        print(" ".join(words[start_idx:end_idx]))

        # Update the start index for the next iteration
        start_idx = end_idx


def main() -> None:
    # Extract the filename, target, and replacement from input
    filename, target, replacement = input().strip().split(",")

    # Get the text from the file
    text = get_text_from_file(filename)

    # Replace the target with the replacement in the text
    modified_text = replace_on_text(text, target, replacement)

    # Get the maximum line length from the file
    max_length = get_max_line_length(filename)

    # Display the modified text within the length limit
    display_text_on_limit(modified_text, max_length)


# Run the main function
main()
