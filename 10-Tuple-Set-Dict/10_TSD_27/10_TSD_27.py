# --------------------------------------------------
# File Name : 10_TSD_27.py
# Problem   : Celebrity
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


# Check if a person 'a' knows another person 'b'
def knows(relation: dict, a: str, b: str) -> bool:
    return b in relation[a]


# Check if a candidate is a celebrity
def is_celeb(relation: dict, candidate: str) -> bool:
    # Return false if candidate knows anyone other than themselves
    if len(relation[candidate]) > 1:
        return False
    # Check if everyone knows the candidate
    for person, known_people in relation.items():
        if person != candidate and candidate not in known_people:
            return False
    return True


# Find the celebrity in the relations
def find_celeb(relation: dict) -> None | str:
    for candidate in relation:
        if is_celeb(relation, candidate):
            return candidate
    return None


# Function to read relations from input until 'q' is entered
def read_relations() -> dict:
    relations = {}
    while True:
        # Read a line of input
        line = input().strip()
        # If the line is 'q', break the loop
        if line == "q":
            break
        # Update the relations dictionary
        a, b = line.split()
        if a not in relations:
            relations[a] = set()
        if b not in relations:
            relations[b] = set()
        relations[a].add(b)
    # Return the relations dictionary
    return relations


# Main function
def main() -> None:
    relations = read_relations()
    celebrity = find_celeb(relations)
    if celebrity is not None:
        print(celebrity)
    else:
        print("Not Found")


# Execute the input string as code
exec(input().strip())
