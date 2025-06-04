def missing_digits(text):
    # Create a list to count how many of each number in a string
    # Example: count[1] is used to count how many "1" in the srting
    count = [0,0,0,0,0,0,0,0,0,0]

    # Count a number in a string
    for character in text:
        if("0" <= character <= "9"):
            count[int(character)] += 1

    # Create a new list that contains number that missing
    # Example: count = [5,0,0,0,0,9,12,3,1,7] --> missing = [1,2,3,4]
    missing = []
    for i in range(0,10):
        if(count[i] == 0):
            missing.append(i)
    
    # Return a list
    return missing

# Execute the input string
exec(input())