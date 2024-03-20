# Not guarantee 100/100 points on this code

# Create a dictionary that contains a letter with its score
letter_score = {'A':1, 'E':1, 'I':1, 'N':1, 'O':1, 'R':1, 'S':1, 'T':1, 'U':1,
                'D':2, 'G':2,
                'B':3, 'C':3, 'M':3, 'P':3,
                'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
                'K':5,
                'J':8, 'X':8,
                'Q':10, 'Z':10}

# Create a function that can calculate that word score
def word_point(word):
    score = 0
    for char in word:
        score += letter_score[char]
    return score

# Input a string of words, then split them to a list of words
# Sort them in reversed alphabetical order
words_list = input().strip().split()

# Create a dictionary contains words with its score
# Create a list contains all unique scores, then sort them in descending order
words_scores = {}
unique_scores = []
for word in words_list:
    words_scores[word] = word_point(word)
    if(word_point(word) not in unique_scores):
        unique_scores.append(word_point(word))
unique_scores.sort(reverse = True)

# Output
# Sorting by unique scores
for score in unique_scores:
    temp = []
    # Find a list that contains words that have the same score
    for word in words_scores:
        if(words_scores[word] == score):
            temp.append(word)
    # Sort these word in alphabetical order
    temp.sort()
    for word in temp:
        print(word, words_scores[word])