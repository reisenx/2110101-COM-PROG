# --------------------------------------------------
# File Name : 2567_3_Q3_B2.py
# Problem   : Survival game
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------


# Separate the input into sublist by slicing and sort each sublist.
# Then concatenate into a single list.
def sorted_by_sublist(data: list, sublist_amount: int) -> list:
    result = []
    for i in range(sublist_amount):
        result += sorted(data[i::sublist_amount])
    return result


# Get the names of students whose at the same position in both lists.
def get_matched_names(initial_data: list, modified_data: list) -> list:
    # Initialize an empty list to store matched names
    matched_names = []

    # Iterate through the initial data and modified data
    for i in range(len(initial_data)):
        # Get the student's name
        name = initial_data[i][1]
        # Check if the name at the same index in both lists matches
        if initial_data[i] == modified_data[i]:
            # If it matches, add the name to the matched names list
            matched_names.append(name)

    # Return the list of matched names
    return matched_names


# Main function
def main():
    # Input the amount of lines that the students will be arranged in
    line_amount = int(input())

    # Input the order of students in their original line
    student_line = []
    data = input().strip().split()
    for i in range(0, len(data), 2):
        # Extract the name and height of each student
        name = data[i]
        height = int(data[i + 1])
        # Append the height and name to a list
        student_line.append([-height, name])

    # Create a modified student line by using the custom sorting function
    modified_student_line = sorted_by_sublist(student_line, line_amount)

    # Sort the student line by height in descending order,
    # then by name in ascending order
    student_line.sort()

    # Get the names of students who are at the same position in both lines
    matched_names = get_matched_names(student_line, modified_student_line)

    # Output the names of students who are at the same position in both lines
    if len(matched_names) > 0:
        print(" ".join(matched_names))
    else:
        print("None")


# Run the main function
main()
