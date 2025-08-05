# --------------------------------------------------
# File Name : 2566_3_Q2_02.py
# Problem   : Euro 2024 Sub-routing
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------


# Extract team names and scores from a match result string.
def get_info(result):
    data = result.split()
    teams = data[0].split(":")
    scores = data[1].split(":")
    return teams[0], teams[1], int(scores[0]), int(scores[1])


# Find the scores between two teams in a list of match results.
def get_score(team01, team02, results):
    # Iterate through the results to find the match between team01 and team02.
    for result in results:
        # Extract scores from the result string.
        _, _, score01, score02 = get_info(result)
        # Check if the order is team01:team02
        if f"{team01}:{team02}" in result:
            return [score01, score02]
        # Check if the order is team02:team01
        elif f"{team02}:{team01}" in result:
            return [score02, score01]
    # If no match is found, return an empty list.
    return []


# Extract scores from actual results and guess results.
def extract_scores(actual_results, guess_results):
    # Initialize an empty list to store the results of every match.
    results = []
    # Iterate through each match in the actual results.
    for match in actual_results:
        # Extract team names and scores from the actual match string.
        team01, team02, score01, score02 = get_info(match)

        # Get the score for the guessed match.
        exact_scores = [score01, score02]
        guess_scores = get_score(team01, team02, guess_results)
        # Add the scores to the results list.
        if guess_scores != []:
            results += [exact_scores + guess_scores]
        else:
            results += [[]]
    # Return the list of results for all matches.
    return results


# Execute the input string as code.
exec(input().strip())
exec(input().strip())
exec(input().strip())
