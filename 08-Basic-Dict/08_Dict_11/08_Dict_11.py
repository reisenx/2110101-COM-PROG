# --------------------------------------------------
# File Name : 08_Dict_11.py
# Problem   : Reverse and Keys
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Reverses the keys and values of a dictionary
def reverse(input_dict: dict) -> dict:
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[value] = key
    return new_dict


# Returns a list of keys that have the specified value in the dictionary
def keys(input_dict: dict, v: int) -> list:
    keys = []
    for key, value in input_dict.items():
        if value == v:
            keys.append(key)
    return keys


# Execute the input string
exec(input().strip())
