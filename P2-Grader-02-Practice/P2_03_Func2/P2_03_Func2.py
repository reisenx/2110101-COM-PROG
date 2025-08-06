# --------------------------------------------------
# File Name : P2_03_Func2.py
# Problem   : Part-II Potpourri Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Function to calculate the area of a convex polygon given its vertices
# The vertices are provided in a counterclockwise order.
def convex_polygon_area(points):
    # Initialize terms for the area calculation
    terms01 = 0
    terms02 = 0
    # Iterate through each vertex and calculate the terms
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        terms01 += x1 * y2
        terms02 += y1 * x2
    # Calculate the area
    return abs(terms01 - terms02) / 2


# Function to check if a given text is a heterogram
# where a heterogram is a word or phrase without a repeating letter.
def is_heterogram(text):
    # Initialize a dictionary to count occurrences of each character
    char_count = {}
    # Iterate through each character in the text
    for char in text.upper():
        # First occurrence of the character
        if char.isalpha() and char not in char_count:
            char_count[char] = 1
        # Repeated occurrence of the character
        elif char.isalpha() and char in char_count:
            return False
    # If no character is repeated, return True
    return True


# Function to replace all occurrences of a target substring with a replacement substring
def replace_ignorecase(text, target, replacement):
    # Initialize variables for the result
    result = ""
    # Initialize start and end indices for substring comparison
    start = 0
    end = len(target)
    # Iterate through the text to find and replace occurrences of the target substring
    while start < len(text):
        # Replace the target substring with the replacement substring
        if text[start:end].lower() == target.lower():
            result += replacement
            start += len(target)
            end += len(target)
        # Add the current character to the result if no match is found
        else:
            result += text[start]
            start += 1
            end += 1
    # Return the modified text
    return result


# Function to find the top 3 candidates based on votes
def top3(votes):
    # Sort the candidates based on their scores in descending order
    ranked_votes = []
    for candidate, score in votes.items():
        ranked_votes.append([-score, candidate])
    ranked_votes.sort()

    # Extract the top 3 candidates from the sorted list
    top_candidates = []
    for _, candidate in ranked_votes[:3]:
        top_candidates.append(candidate)
    return top_candidates


# Execute the input string as code
for _ in range(2):
    exec(input().strip())
