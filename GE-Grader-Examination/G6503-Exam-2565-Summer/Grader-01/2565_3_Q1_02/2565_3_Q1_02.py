# --------------------------------------------------
# File Name : 2565_3_Q1_02.py
# Problem   : Election
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

# List of candidates and parties names
CANDIDATE = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "X9", "Y10", "Z11"]
PARTY = ["PT1", "PP2", "RT3", "TT4", "KK5", "ST6"]

# Initialize vote counts for candidates and parties
candidate_votes = [0] * len(CANDIDATE)
party_votes = [0] * len(PARTY)

while True:
    # Input data until "q" is entered
    data = input().strip().split()
    if data == ["q"]:
        break
    # Extract candidate and party indices from input
    candidate_idx = int(data[0]) - 1
    party_idx = int(data[1]) - 1
    # Increment the vote counts for the candidate and their party
    candidate_votes[candidate_idx] += 1
    party_votes[party_idx] += 1

# Find the candidate and party with the maximum votes
candidate_idx = candidate_votes.index(max(candidate_votes))
party_idx = party_votes.index(max(party_votes))

# Output the candidate and party with the most votes
print(CANDIDATE[candidate_idx], max(candidate_votes))
print(PARTY[party_idx], max(party_votes))
