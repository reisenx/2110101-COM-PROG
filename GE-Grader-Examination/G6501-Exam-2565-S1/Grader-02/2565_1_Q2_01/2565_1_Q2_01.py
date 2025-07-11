# --------------------------------------------------
# File Name : 2565_1_Q2_01.py
# Problem   : Scrabble
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Calculate the score of each letter in Scrabble
def letter_point(letter: str) -> int:
    if letter in "AEIOULNRST":
        return 1
    elif letter in "DG":
        return 2
    elif letter in "BCMP":
        return 3
    elif letter in "FHVWY":
        return 4
    elif letter == "K":
        return 5
    elif letter in "JX":
        return 8
    return 10


# Calculate the total score of a word based on its letters
def word_point(word: str) -> int:
    total_point = 0
    for letter in word:
        total_point += letter_point(letter)
    return total_point


# Read input words and calculate their scores
word_points = []
for word in input().split():
    points = word_point(word)
    word_points.append([-points, word])

# Sort the words by their scores in descending order
# if scores are equal, sort alphabetically
word_points.sort()
# Output the words with their scores
for points, word in word_points:
    print(word, -points)
