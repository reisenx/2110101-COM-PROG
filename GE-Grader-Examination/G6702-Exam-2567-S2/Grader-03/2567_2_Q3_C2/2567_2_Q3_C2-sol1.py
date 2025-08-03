# --------------------------------------------------
# File Name : 2567_2_Q3_C2-sol1.py
# Problem   : Grandson
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Initialize a dictionary to store the children of each person
children = {}

# Input relationships in the family and build the dictionary
n = int(input())
for _ in range(n):
    # Input relationships
    parent, child = input().strip().split()

    # Update the dictionary with the parent-child relationship
    if parent not in children:
        children[parent] = set()
    if child not in children:
        children[child] = set()
    children[parent].add(child)

# Input the names of people to query
queries = input().strip().split()

# Output the number of grandchildren for each queried person
for person in queries:
    # If the person exists in the dictionary, count their grandchildren
    if person in children:
        # Initialize a counter for grandchildren
        total_grandchildren = 0

        # Count the children of each child of the person
        for child in children[person]:
            if child in children:
                total_grandchildren += len(children[child])

        # Output the total number of grandchildren
        print(total_grandchildren)

    # If the person does not exist in the dictionary, output 0
    else:
        print(0)
