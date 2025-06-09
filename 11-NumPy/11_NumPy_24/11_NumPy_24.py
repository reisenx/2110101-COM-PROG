import numpy as np

# The problem is the same with 05_List_F14.py
# But in this solution, we use NumPy instead of loop

# Returns array that contains peak value
# Example: x = [1 4 5.1 5.2 5.3 6 9 6.1 6.2 7.1 7.2 7.3 8.4 8.5 9.2 9.3 20 6 8 11.2 11.5]
# In this case, we will create 3 array
# > left    = [1     4 5.1 5.2 5.3   6   9 6.1 6.2 7.1 7.2 7.3 8.4 8.5 9.2 9.3 20  6      8]
# > center  = [4   5.1 5.2 5.3   6   9 6.1 6.2 7.1 7.2 7.3 8.4 8.5 9.2 9.3  20  6  8   11.2]
# > right   = [5.1 5.2 5.3   6   9 6.1 6.2 7.1 7.2 7.3 8.4 8.5 9.2 9.3  20   6  8 11.2 11.5]
# Peaks are numbers in 'center' that satisfy 'center' > 'left' and 'center' > right
def peak_indexes(x):
    # If there are less than 3 numbers in 'x' array, it has 0 peaks
    if(len(x) < 3):
        return []
    else:
        left = x[0 : len(x)-2]
        center = x[1 : len(x)-1]
        right = x[2 : len(x)]
        
        # Find a position of all peaks
        condition = (center > left) & (center > right)
        position = np.arange(1,len(x)-1)[condition]
        return position

def main():
    # Input number and create array
    d = np.array([float(e) for e in input().split()])
    # Get array with only peaks
    pos = peak_indexes(np.array(d))
    # Output
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

# Execute an input string
exec(input().strip())