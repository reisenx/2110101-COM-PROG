# Create a list that contains names
# 'SNames' list contains candidates names
# 'PNames' list contains party names
SNames = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "X9", "Y10", "Z11"]
PNames = ["PT1", "PP2", "RT3", "TT4", "KK5", "ST6"]

# Create a list that contains votes
# 'SCount' list contains votes of each candidates
# > Index 0 of 'SCount' is for "A1"
# > Index 1 of 'Scount' is for "B2"
# > Index 2 of 'SCount' is for "C3" and so on...
# 'PCount' list contains votes of each party
# > Index 0 of 'PCount' is for "PT1"
# > Index 1 of 'PCount' is for "PP2"
# > Index 2 of 'PCount' is for "RT3" and so on...
SCount = [0]*11
PCount = [0]*6

# Input
while(True):
    data = input().strip().split()
    # If the input is 'q', then break
    if(data[0] == 'q'):
        break
    
    # The input will be in the format
    # [Candidates number] [Party number]
    else:
        S,P = int(data[0]), int(data[1])
        # Count votes
        SCount[S-1] += 1
        PCount[P-1] += 1

# Find index of the most voted candidates and party in 'SCount' and 'PCount'
S_index = SCount.index(max(SCount))
P_index = PCount.index(max(PCount))

# Output
print(SNames[S_index], max(SCount))
print(PNames[P_index], max(PCount))