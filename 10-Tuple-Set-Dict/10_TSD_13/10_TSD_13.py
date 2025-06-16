# --------------------------------------------------
# File Name : 10_TSD_13.py
# Problem   : Winner
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input number of matches
n = int(input())

# Initialize sets for winners and losers
winners = set()
losers = set()

# Process each match
for _ in range(n):
    # Read the match result
    winner, loser = input().strip().split()

    # Update winners and losers sets
    winners.add(winner)
    losers.add(loser)

# Output the winner who is not in the losers set
print(sorted(winners - losers))
