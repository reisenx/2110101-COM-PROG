# --------------------------------------------------
# File Name : 2567_1_Q3_C1.py
# Problem   : USA Election
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initialize dictionaries to store state, county, and votes
state_electoral_votes = {}
state_counties = {}
state_party_votes = {}
total_electoral = {"republican": 0, "democrat": 0}

# Input states and their electoral votes
n = int(input())
for _ in range(n):
    state, votes = input().strip().split(",")
    state_electoral_votes[state] = int(votes)

# Input counties and their states
n = int(input())
for _ in range(n):
    county, state = input().strip().split(",")
    if state not in state_counties:
        state_counties[state] = []
    state_counties[state].append(county)

# Calculate votes for each party in each state
n = int(input())
for _ in range(n):
    # Extract county, state, and votes from input
    data = input().strip().split(",")
    county = data[0].strip()
    state = data[1].strip()
    republican_votes = int(data[2].strip())
    democrat_votes = int(data[3].strip())

    # Validate state
    if state not in state_electoral_votes:
        continue

    # Validate county
    if county not in state_counties[state]:
        continue

    # Update party votes for the state
    if state not in state_party_votes:
        state_party_votes[state] = {"republican": 0, "democrat": 0}
    state_party_votes[state]["republican"] += republican_votes
    state_party_votes[state]["democrat"] += democrat_votes

# Calculate total electoral votes based on party votes on each state
for state, votes in state_party_votes.items():
    # Republican wins on the state and gains electoral votes
    if votes["republican"] > votes["democrat"]:
        total_electoral["republican"] += state_electoral_votes[state]

    # Democrat wins on the state and gains electoral votes
    elif votes["republican"] < votes["democrat"]:
        total_electoral["democrat"] += state_electoral_votes[state]

# Output the total electoral votes of each party
print(f"{total_electoral['republican']}:{total_electoral['democrat']}")

# Republican wins if they have more electoral votes
if total_electoral["republican"] > total_electoral["democrat"]:
    print("Republican wins")

# Democrat wins if they have more electoral votes
elif total_electoral["republican"] < total_electoral["democrat"]:
    print("Democrat wins")

# Both parties have equal electoral votes
else:
    print("Undecided")
