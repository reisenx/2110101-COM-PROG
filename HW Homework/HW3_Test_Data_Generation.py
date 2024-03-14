# HW3_Test_Data_Generation

# This function can random n number in range a to b with a seed
# Example: a = 2, b = 5, n = 10, seed = 2566
# Return: [2,5,3,4,5,4,4,2,5,2]
def generate_random_sequence(a, b, n, seed):
    import random
    # Setup a random seed
    random.seed(seed)
    # Create and return a random number list using a seed
    random_list = [random.randint(a,b) for _ in range(n)]
    return random_list

# This function can check that all the value in range a to b are in the data list or not
# Example: a = 2, b = 5, data = [2,5,3]
# Return: False
# Example: a = 2, b = 5, data = [2,5,3,4]
# Return: True
def all_values_in_list(a, b, data):
    # Create a list that contains all numbers in range a to b 
    check_number_list = [int(i) for i in range(a,b+1)]
    # Create a list to contain the unique number in the list
    unique_num = []
    for number in data:
        if(number in range(a,b+1) and number not in unique_num):
            unique_num.append(number)
    unique_num.sort()
    # Check if the data list has all numbers in range a to b
    if(unique_num == check_number_list):
        return True
    else:
        return False

# This function can return shortest sequence from range a to b of the input sequence
# Example: a = 2, b = 5, sequence = [2,8,4,6,8,5,6,1,8,2,9,9,3,8,6,5,9,6,2,3]
# Return: [2,4,5,2,3]
def get_shortest_sequence_range(a, b, sequence):
    # Create a list to contain the unique number in the list
    unique_num = []
    for number in sequence:
        if(number in range(a,b+1) and number not in unique_num):
            unique_num.append(number)
    # Create a shortest sequence
    short_seq = []
    # Create this list to check what the number that already use
    already_used = []
    i = 0
    unique_num.sort()
    # Add a number to a shortest sequence until all numbers are used
    while(already_used != unique_num):
        if(sequence[i] in unique_num):
            short_seq.append(sequence[i])
            if(sequence[i] not in already_used):
                already_used.append(sequence[i])
            already_used.sort()
        i += 1
    # Return the shortest sequence
    return short_seq

# This function can check if the "value" occurs in the list more than or equal n times
# Example: value = 5, n = 2, data = [2,5,3,4,5,4,4,2,5,2]
# Return: True
# Example: value = 5, n = 3, data = [2,5,3,4,5,4,4,2,5,2]
# Return: False
def check_all_occurrence(value, n, data):
    # Count the number "value" in the list "data"
    count = 0
    for number in data:
        if(number == value):
            count += 1
    # Return
    if(count >= n):
        return True
    else:
        return False

# This function can generate a shortest sequence from a list of random number 
# between range a to b using a seed
# Example: a = 2, b = 5, seed = 2567
# A list would be [4,4,4,2,5,3,5,2,5,2,4, ...]
# Return: [4,4,4,2,5,3]
def generate_shortest_sequence_from_a2b(a, b, seed):
    import random
    random.seed(seed)
    sequence = []
    # Add a random using a seed until all numbers in range a to b appears in the list
    while(not all_values_in_list(a,b,sequence)):
        sequence.append(random.randint(a,b))
    # Return a shortest sequnce using a function
    return get_shortest_sequence_range(a, b, sequence)

# This a function can return all unique numbers in a input list
# Example: [5,3,6,4,3,5,4,6,3,5,4,5,6,6,3,4,6,4,6,2]
# Return: [5,3,6,4,2]
def get_unique_sequence(sequence):
    unique_number = []
    for number in sequence:
        if(number not in unique_number):
            unique_number.append(number)
    return unique_number

# This function can return a list of handicap scale of hole from scale 1 to 18
# Example: seed = 2566
# We would get a unique list using seed 2556 as [4,16,7,11,9,1,3,18,5,12,10,17,13,8,2,15,6,14]
# Then we put the all odd number first then put all even number
# Return: [7,11,9,1,3,5,17,13,15,4,16,18,12,10,8,2,6,14]
def generate_course_hc_scales(seed):
    import random
    # Create a unique sequence in range 1 to 18 using a seed
    holes = generate_shortest_sequence_from_a2b(1,18,seed)
    holes = get_unique_sequence(holes)
    # Create a list that contains handicap scale
    handicap_scale = []
    # Put all odd number into a new list
    for number in holes:
        if(number%2 == 1):
            handicap_scale.append(number)
    # Then put all evem into a new list
    for number in holes:
        if(number%2 == 0):
            handicap_scale.append(number)
    # Return a handicap scale list
    return handicap_scale 

# This function can return a list of holes sorting by difficulty
# Diffculty is depends of handicap scale (1 = Hardest, 18 = Easiest)
# Example: [17,3,13,15,5,7,9,1,11,2,6,14,16,8,12,18,4,10]
# Return: [8,10,2,17,5,11,6,14,7,18,9,15,3,12,4,13,1,16]
def holes_sorted_by_hc_scales(hc_scales):
    # Create a list that contains number of holes sorting by difficulty
    sorted_hole = []
    # The index in hc_scales is a number of hole
    for handicap in range(1,19):
        sorted_hole.append(hc_scales.index(handicap) + 1)
    return sorted_hole