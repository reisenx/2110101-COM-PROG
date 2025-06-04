import numpy as np

# weight is an 1D array that contains score weight of [Midterm Final Project]
# data is an 2D array (Size: nx4) that each line contains [ID Midterm_score Final_score Project_score] 
def read_data():
    # Get 'weight' array
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    
    # Get 'data' array
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    
    # Returns both array
    return weight, data

# This function can returns ID of students that have total score lower than mean
def report_lower_than_mean(weight, data):
    # Get an 1D array of IDs
    # Example: [610111 610222 610333 610444 610555]
    ID = data[:,0]
    
    # Calculate and get an 1D array total score (weighted)
    # Example: [83.  68.6 79.5 61.  78. ]
    total = np.dot(data[:,1:4],weight)
    
    # Calculate mean score
    mean = np.mean(total)

    # Select item in array that (total < mean == True)
    lowers = ID[total < mean]
    
    # Output
    if(len(lowers) == 0):
        print("None")
    else:
        # Convert all item in 'lowers' array from int to str
        lowers = np.array(lowers, dtype = str)
        print(", ".join(lowers))

# Execute an input string
exec(input().strip())