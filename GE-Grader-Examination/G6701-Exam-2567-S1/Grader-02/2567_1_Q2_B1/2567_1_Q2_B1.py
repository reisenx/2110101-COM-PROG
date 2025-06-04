# Input list 'D'
D = [int(e) for e in input().split()]
# Find list 'P'
P = sorted(D)
# Given X is an empty list
X = []

# ---------- Algorithm ----------
# Example: D = [8,3,1,6] | P = [1,3,6,8] | X = [] | pos = 0
# Step 1: Find X[0]   | D = [8,3,1,6]
# - Add P[0] to pos   | pos = 1
# - Mod pos to len(D) | index = pos%4 = 1
# - Add D[1] to X     | X = [3]
# - Remove D[1]       | D = [8,1,6]

# Step 2: Find X[1]   | D = [8,1,6]
# - Add P[1] to pos   | pos = 4
# - Mod pos to len(D) | index = pos%3 = 1
# - Add D[1] to X     | X = [3,1]
# - Remove D[1]       | D = [8,6]

# Step 3: Find X[2]   | D = [8,6]
# - Add P[2] to pos   | pos = 10
# - Mod pos to len(D) | index = pos%2 = 0
# - Add D[0] to X     | X = [3,1,8]
# - Remove D[0]       | D = [6]

# Step 4: Find X[3]   | D = [6]
# - Add P[3] to pos   | pos = 16
# - Mod pos to len(D) | index = pos%1 = 0
# - Add D[0] to X     | X = [3,1,8,6]
# - Remove D[0]       | D = []
# ----------------------------------------

# Find list X using algorithm above
pos = 0
for i in range(len(P)):
    pos += P[i]
    index = pos % len(D)
    X.append(D[index])
    D.pop(index)

# Output
# To use join() function, we need to convert all item in list from int to str
X = [str(item) for item in X]
print(" ".join(X))