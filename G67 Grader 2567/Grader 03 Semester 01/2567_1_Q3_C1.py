# Input electoral votes of each state
n = int(input())
electoralVotes = {}
for i in range(n):
    state,votes = input().strip().split(',')
    electoralVotes[state] = int(votes)

# Input county of each state
n = int(input())
stateCounty = {}
for i in range(n):
    county,state = input().strip().split(',')
    if(state not in stateCounty):
        stateCounty[state] = [county]
    else:
        stateCounty[state].append(county)

# Calculate stateVotes
# Key: state name
# Value: [Republican votes, Democrat votes]
stateVotes = {}
n = int(input())
for i in range(n):
    county,state,rVote,dVote = input().strip().split(',')
    rVote,dVote = int(rVote), int(dVote)
    # Check if that state is valid
    if(state not in electoralVotes):
        continue
    # Check if that county is valid
    if(county not in stateCounty[state]):
        continue
    
    # Calculate total score of each state
    if(state not in stateVotes):
        stateVotes[state] = [rVote, dVote]
    else:
        stateVotes[state][0] += rVote
        stateVotes[state][1] += dVote

# Calculate democrat and republican electoral votes
republican = 0
democrat = 0
for state, [rVote, dVote] in stateVotes.items():
    if(rVote > dVote):
        republican += electoralVotes[state]
    if(dVote > rVote):
        democrat += electoralVotes[state]

# Output
print(str(republican) + ':' + str(democrat))
if(republican > democrat):
    print("Republican wins")
if(democrat > republican):
    print("Democrat wins")
if(republican == democrat):
    print("Undecided")