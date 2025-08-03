# --------------------------------------------------
# File Name : 2567_3_Q4_B2.py
# Problem   : Student Ranking
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for grade criteria and order
GRADE_ORDER = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
GRADE_CRITERIA = {
    "A": [80.0, 100.0],
    "B+": [75.0, 80.0],
    "B": [70.0, 75.0],
    "C+": [65.0, 70.0],
    "C": [60.0, 65.0],
    "D+": [55.0, 60.0],
    "D": [50.0, 55.0],
    "F": [0.0, 50.0],
}


# Function to calculate the average score from a list of scores
def calculate_average(scores: list[float]) -> float:
    # If the list is empty, return 0.0
    if len(scores) == 0:
        return 0.0

    # Calculate and return the average score
    return sum(scores) / len(scores)


# Function to determine the grade based on the score
def get_grade(score: float) -> str:
    # Check the score against the grade criteria and return the corresponding grade
    for grade, [low, high] in GRADE_CRITERIA.items():
        if low <= score < high:
            return grade
    # If the score does not match any criteria, return "F"
    return "F"


# Function to process student data and return their name and grade
def process_student_data(student_data: list) -> list:
    # Extract the student's name and calculate their grade from their scores
    name = student_data[0]
    grade = get_grade(calculate_average(student_data[1]))
    # Return the name and grade as a list
    return [name, grade]


# Function to print students ranked by their grades
def print_students_ranked_by_grades(list_of_student_data: list[list]) -> None:
    # Initialize a dictionary to map grades to student names
    grade_to_students = {}

    # Process each student's data
    for student in list_of_student_data:
        # Get the student's name and grade
        name, grade = process_student_data(student)

        # Store the student's name in the dictionary under their grade
        if grade not in grade_to_students:
            grade_to_students[grade] = []
        grade_to_students[grade].append(name)

    # Print the students sorted by grade in the defined order
    for grade in GRADE_ORDER:
        # Check if there are students for the current grade
        if grade in grade_to_students:
            # Sort the students' names alphabetically and print them with their grade
            for student in sorted(grade_to_students[grade]):
                print(student, grade)


# Run the input string as code until it ends with a semicolon
while cmd := input().strip():
    exec(cmd)
    if cmd[-1] == ";":
        break
