# --------------------------------------------------
# File Name : 2567_1_Q4_B1-S.py
# Problem   : T-Scores
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize constants
DEFAULT_AVG_SCORE = 50.0
TGAT_TPAT_CONST = 8.69031
A_LEVEL_CONST = 5.21299


# Function to calculate the mean of a list of scores
def get_mean(scores):
    # Check if the list is empty
    if len(scores) == 0:
        return 0.0
    # Return the mean of the scores
    return sum(scores) / len(scores)


# Function to calculate the standard deviation of a list of scores
def get_std_dev(scores, mean):
    # Check if the list is empty
    if len(scores) == 0:
        return 0.0

    # Calculate the squared differences between each score and the mean
    squared_diffs = []
    for score in scores:
        squared_diffs.append((score - mean) ** 2)
    # Return the standard deviation
    return (sum(squared_diffs) / len(scores)) ** 0.5


# Input the scores list and the subject
scores = [int(score) for score in input().split()]
subject = input().strip()

# Calculate the mean and standard deviation of the scores
mean_score = get_mean(scores)
std_dev = get_std_dev(scores, mean_score)

# Initialize the list to hold T-scores
t_scores = []

# Calculate T-scores based on the subject
for score in scores:
    t_score = 0
    # Calculate T-score of subject TGAT, TPAT
    if subject in ["TGAT", "TPAT"]:
        t_score = DEFAULT_AVG_SCORE + TGAT_TPAT_CONST * ((score - mean_score) / std_dev)

    # Calculate T-score of subject A-Level
    elif subject == "A-Level":
        t_score = DEFAULT_AVG_SCORE + A_LEVEL_CONST * ((score - mean_score) / std_dev)

    # Append the calculated T-score rounded to two decimal places to the list
    t_scores.append(str(round(t_score, 2)))

# Output the T-scores
print(" ".join(t_scores))
