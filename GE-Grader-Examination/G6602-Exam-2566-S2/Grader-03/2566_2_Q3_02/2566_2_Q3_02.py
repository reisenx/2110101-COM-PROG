# --------------------------------------------------
# File Name : 2566_2_Q3_02.py
# Problem   : Friends
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------


# Read relationship data and return a list of tuples.
def read_friends() -> list[tuple[str, str]]:
    friends = []
    n = int(input())
    for _ in range(n):
        friends.append(tuple(input().strip().split()))
    return friends


# Count the number of friends for each person in the list of names.
def count_friends(
    friends: list[tuple[str, str]], names: list[str]
) -> list[tuple[str, int]]:
    # Create a dictionary to store set of friends of each person.
    all_friends = {}
    for a, b in friends:
        # Initialize the sets for each person if they do not exist.
        if a not in all_friends:
            all_friends[a] = set()
        if b not in all_friends:
            all_friends[b] = set()
        # Add each person to the other's set of friends.
        all_friends[a].add(b)
        all_friends[b].add(a)

    # Sort the names and count the number of friends for each.
    result = []
    for name in sorted(names):
        # If the name is not in the dictionary, they have no friends.
        if name not in all_friends:
            result.append((name, 0))
        # Otherwise, append the name and the count of friends.
        else:
            result.append((name, len(all_friends[name])))
    # Return the sorted list of tuples with names and their friend counts.
    return result


# Execute the input string as code
exec(input().strip())
