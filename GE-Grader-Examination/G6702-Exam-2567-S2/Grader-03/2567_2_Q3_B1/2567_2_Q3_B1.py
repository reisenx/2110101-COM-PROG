# --------------------------------------------------
# File Name : 2567_2_Q3_B1.py
# Problem   : Graduation Ceremony
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Constants for GPAX thresholds
FIRST_HONOR_GPAX = 3.60
SECOND_HONOR_GPAX = 3.25

# Constants for grade order and minimum honor grade
GRADE_ORDER = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]
MINIMUM_HONOR_GRADE = GRADE_ORDER.index("C")

# Constants for maximum years to qualify for honors
MAX_YEARS_HONOR = 4.0

# Initialize lists to store student info based on their honors status
first_honor_students = []
second_honor_students = []
general_students = []


# Function to process each student's information
def process_student_info(line):
    # Extract student data from the input line
    data = line.strip().split()
    student_id = data[0].strip()
    gpax = float(data[1].strip())
    # Convert grade to index in GRADE_ORDER
    minimum_grade = GRADE_ORDER.index(data[2].strip())
    # Check if the student has withdrawn any subject
    has_withdrawn = data[3].strip() == "Y"
    study_years = float(data[4].strip())

    # Check if the student qualifies for honors
    if (
        has_withdrawn
        or study_years > MAX_YEARS_HONOR
        or minimum_grade < MINIMUM_HONOR_GRADE
        or gpax < SECOND_HONOR_GPAX
    ):
        general_students.append(student_id)

    # Check if the student qualifies for first honors
    elif gpax >= FIRST_HONOR_GPAX:
        # Add the student to first honors list with negative GPAX for sorting
        first_honor_students.append([-gpax, student_id])

    # Check if the student qualifies for second honors
    elif gpax >= SECOND_HONOR_GPAX:
        # Add the student to second honors list with negative GPAX for sorting
        second_honor_students.append([-gpax, student_id])


def display_students():
    # Check if there are any first honor students
    if len(first_honor_students) > 0:
        print(1)
        # Output student IDs sorted by GPAX in descending order
        for _, student_id in sorted(first_honor_students):
            print(student_id)

    # Check if there are any second honor students
    if len(second_honor_students) > 0:
        print(2)
        # Output student IDs sorted by GPAX in descending order
        for _, student_id in sorted(second_honor_students):
            print(student_id)

    # Check if there are any general students
    if len(general_students) > 0:
        print("General")
        # Output student IDs sorted in ascending order
        for student_id in sorted(general_students):
            print(student_id)


# Main function
def main():
    # Input student information until "-1" is encountered
    while True:
        line = input().strip()
        if line == "-1":
            break
        process_student_info(line)
    # Display the categorized students
    display_students()


# Run the main function
main()
