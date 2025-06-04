# Definition: CELEBRITY is a person that everyone can recognizes, but they can't recognize anyone

# This function can check if 'name01' can recognize 'name02'
# 'relations' is a dictionary in the format
# relations = {Person : Set of People recognized by that Person, ...}
def knows(relations, name01, name02):
    if(name02 in relations[name01]):
        return True
    else:
        return False

# This function can check if 'celeb_name' is CELEBRITY or not
# Citeria
# 1.) relations[celeb_name] must be an empty set or is a set with only their name (because they can't recognize anyone)
# 2.) Other 'relations' dictionary value must have 'name' in it
def is_celeb(relations, celeb_name):
    # Check citeria 1
    if(len(relations[celeb_name]) == 0):
        Citeria01 = True
    elif(relations[celeb_name] == {celeb_name}):
        Citeria01 = True
    else:
        Citeria01 = False
    
    # Check citeria 2
    Citeria02 = True
    for name, names_set in relations.items():
        # Skip if name is celeb_name
        if(name == celeb_name):
            continue
        # If names_set doesn't have 'celeb_name', set Citeria02 to False then break
        if(celeb_name not in names_set):
            Citeria02 = False
            break
    
    # Return a value
    return Citeria01 and Citeria02

# This function can find CELEBRITY in 'relations' dictionary
# If found, return CELEBRITY's name
# If not found, return None
def find_celeb(relations):
    # Create a list with all name in 'relations' dictionary
    name_list = list(relations.keys())
    
    # Find CELEBRITY in 'relations' dictionary
    for name in name_list:
        # If found, return CELEBRITY's name
        if(is_celeb(relations, name)):
            return name
    # If not found, return None
    return None

# This function can input data in this format
# [Person 01] [People recognized by that Person 01]
# [Person 02] [People recognized by that Person 02]
# ...
# q
# And convert into dictionary with this format
# {Person : Set of People recognized by that Person, ...}
def read_relations():
    # Create an empty dictionary and set
    relations = {}
    unique_name = set()
    
    # Input all relationship
    while(True):
        data = input().strip()
        # Break the loop, if the input is 'q'
        if(data == 'q'):
            break
        else:
            name,know = data.split()
            # Put data to 'unique_name' set
            unique_name.add(name)
            unique_name.add(know)
            # Put data to 'relations' dictionary
            if(name not in relations):
                relations[name] = set()
                relations[name].add(know)
            else:
                relations[name].add(know)
    
    # Check if there's a person can't recognize anyone
    # If found, add them in a dictionary with empty set value
    for name in unique_name:
        if(name not in relations):
            relations[name] = set()
    
    # Return a relations dictionary
    return relations

# This function can read input and find CELEBRITY from the input
def main():
    relations = read_relations()
    celebrity = find_celeb(relations)
    if celebrity == None :
        print('Not Found')
    else:
        print(celebrity)

# Execute an input string
exec(input().strip())