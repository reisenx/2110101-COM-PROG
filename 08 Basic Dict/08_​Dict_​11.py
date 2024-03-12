# This function can return a dictionary that swap keys and values
def reverse(dict):
    new_dict = {}
    for key in dict:
        new_dict[dict[key]] = key
    return new_dict

# This function can a list that contains a key that have the input value
def keys(dict,value):
    keys_list = []
    for key in dict:
        if(dict[key] == value):
            keys_list.append(key)
    return keys_list

# Execute the input string
exec(input().strip())