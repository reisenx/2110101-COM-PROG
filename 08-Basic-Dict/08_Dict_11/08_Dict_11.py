# This function can return a dictionary that swap keys and values
def reverse(dict):
    new_dict = {}
    for key,value in dict.items():
        new_dict[value] = key
    return new_dict

# This function can a list that contains a key that have the input value
def keys(dict,v):
    keys_list = []
    for key,value in dict.items():
        if(value == v):
            keys_list.append(key)
    return keys_list

# Execute the input string
exec(input().strip())