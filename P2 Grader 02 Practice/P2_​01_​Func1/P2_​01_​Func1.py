# This function can check if the number is odd number
def is_odd(number):
    return number%2 == 1

# This function can check if the list has odd number
def has_odds(data):
    HasOdds = False
    for number in data:
        if(is_odd(number)):
            HasOdds = True
            break
    return HasOdds

# This function can check if all number in a list are odd number 
def all_odds(data):
    AllOdds = True
    for number in data:
        if(not is_odd(number)):
            AllOdds = False
            break
    return AllOdds

# This function can check if the list has no odd number
def no_odds(data):
    return not has_odds(data)

# This function can return a list with odd number in the input list
def get_odds(data):
    odds_list = []
    for number in data:
        if(is_odd(number)):
            odds_list.append(number)
    return odds_list

# This function can create a new list by following the instruction below
# Example: a = [0,8,1,2,4,6,5,7,9,2,3], b = [4,19,11,12,10,17]
# 1.) Get a list with only odd number from list a and b
#     We would get odds_a = [1,5,7,9,3] and odds_b = [19,11,17]
# 2.) Put a number from odd_list_a into zip_odds_list then put a number from odd_list_b and so on ...
#     We would get zip_odds = [1,19,5,11,7,17]
# 3.) These 2 list may have different length. 
#     So in this example, we put the rest of odd_list_a into zip_odds_list
#     We would get zip_odds_list = [1,19,5,11,7,17,9,3] then return this list
def zip_odds(a,b):
    odds_a = get_odds(a)
    odds_b = get_odds(b)
    zip_odds = []

    # Put a number from odd_list_a into zip_odds_list then put a number from odd_list_b and so on ... 
    add = max(len(odds_a) ,len(odds_b))
    for index in range(add):
        if(index < len(odds_a)):
            zip_odds.append(odds_a[index])
        
        if(index < len(odds_b)):
            zip_odds.append(odds_b[index])
    
    return zip_odds

# Execute the input string
exec(input().strip())