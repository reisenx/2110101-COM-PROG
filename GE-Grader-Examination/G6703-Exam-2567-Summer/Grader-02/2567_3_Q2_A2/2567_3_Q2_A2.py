# --------------------------------------------------
# File Name : 2567_3_Q2_A2.py
# Problem   : Planting Plan
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

# Constants for tree types names
TREE_TYPES = ["A", "B", "C"]

# Input length of the field and tree distances
field_limit = int(input())
tree_distance = [int(num) - 1 for num in input().split()]

# Input the order of trees to be planted
trees_order = input().strip()

# Construct a string to show the planting result
planting_result = ""
for i in range(len(trees_order) - 1):
    # Get the current and next tree type
    tree_01 = trees_order[i]
    tree_02 = trees_order[i + 1]

    # Convert tree types to indices
    idx_01 = TREE_TYPES.index(tree_01)
    idx_02 = TREE_TYPES.index(tree_02)

    # Calculate the distance between the current and next tree
    distance = max(tree_distance[idx_01], tree_distance[idx_02])

    # Append the current tree and the distance to the result
    planting_result += tree_01 + ("." * distance)

# Append the last tree to the result
planting_result += trees_order[-1]

# Ensure the planting result does not exceed the field limit
if len(planting_result) < field_limit:
    remaining_space = field_limit - len(planting_result)
    planting_result += "." * remaining_space

elif len(planting_result) > field_limit:
    planting_result = planting_result[:field_limit]

# Output the final planting result
print(planting_result)
