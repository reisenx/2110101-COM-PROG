# Example testcase filename 1: 101.txt
# Example testcase filename 2: error.txt

# This function can read file and returns a list that contains each line in a file
# Example:
# ..............
# .|_|......|_|.
# .|_|_|..|_|_|.
# ..............
# textlist = ["..............", ".|_|......|_|.", ".|_|_|..|_|_|.", ".............."]
def file_to_textlist(filename):
    # Open a file
    file = open(filename,"r")
    # Read each line in the file and put it in a list
    textlist = []
    for line in file:
        textlist.append(line.strip())
    # Close a file
    file.close()
    # Return a list
    return textlist

# This function can check if the input column can be stripped (contains only '.')
# Example:
# ..............
# .|_|......|_|.
# .|_|_|..|_|_|.
# ..............
# check_column(textlist, 0) = True
# check_column(textlist, 1) = False
# check_column(textlist, 6) = True
def check_column(textlist, column):
    AllDot = True
    nrows = len(textlist)
    # Check if every row are all dot ('.')
    for row in range(nrows):
        if(textlist[row][column] != '.'):
            AllDot = False
            break
    # Returns a result
    return AllDot

# This function returns list of all column that need to be stripped
# Example:
# ..............
# .|_|......|_|.
# .|_|_|..|_|_|.
# ..............
# check_all_column(textlist) = [0,6,7,13]
def check_all_column(textlist):
    ncols = len(textlist[0])
    # Loop every column in 'textlist' and put all column that need to be stripped in a list
    all_cols = []
    for col in range(ncols):
        if(check_column(textlist,col)):
            all_cols.append(col)
    # Returns a list of column
    return all_cols

# This function returns list of left column that need to be strip
# Example:
# ..............
# .|_|......|_|.
# .|_|_|..|_|_|.
# ..............
# check_left_column(textlist) = [0]
def check_left_column(textlist):
    ncols = len(textlist[0])
    # Loop every column in 'textlist' and put left column that need to be stripped in a list
    left_cols = []
    for col in range(ncols):
        if(check_column(textlist,col)):
            left_cols.append(col)
        # Break the loop if the left column ended
        else:
            break
    # Returns a list of column
    return left_cols

# This function returns list of right column that need to be strip
# Example:
# ..............
# .|_|......|_|.
# .|_|_|..|_|_|.
# ..............
# check_right_column(textlist) = [13]
def check_right_column(textlist):
    ncols = len(textlist[0])
    # Loop every column in 'textlist' and put left column that need to be stripped in a list
    # Need to start at the last column first, then decrease the column by 1 each loop 
    right_cols = []
    for col in range(ncols-1, -1, -1):
        if(check_column(textlist,col)):
            right_cols.append(col)
        # Break the loop if the right column ended
        else:
            break
    # Returns a list of column
    return right_cols

# This function can delete all column in 'cols_list' parameter
# Example:
# ..............
# .|_|......|_|.
# .|_|_|..|_|_|.
# ..............
# delete_column(textlist, [0,6,7,13]) returns
# ..........
# |_|....|_|
# |_|_||_|_|
# ..........
def delete_column(textlist, cols_list):
    nrows = len(textlist)
    ncols = len(textlist[0])
    new_textlist = []
    # Recontruct the a string in each line by deleting column in 'cols_list' and put it in 'new_textlist'
    for row in range(nrows):
        line = ""
        for col in range(ncols):
            if(col not in cols_list):
                line += textlist[row][col]
        new_textlist.append(line)
    # Returns 'new_textlist'
    return new_textlist

# Input filename and command
filename = input().strip()
command = input().strip()

# Read file and convert it to a list
textlist = file_to_textlist(filename)

# Check command and get a list of column that needed to be stripped
IsError = False
if(command == "LSTRIP"):
    cols_list = check_left_column(textlist)
elif(command == "RSTRIP"):
    cols_list = check_right_column(textlist)
elif(command == "STRIP"):
    cols_list = check_left_column(textlist) + check_right_column(textlist)
elif(command == "STRIP_ALL"):
    cols_list = check_all_column(textlist)
else:
    IsError = True

# If error
if(IsError):
    print("Invalid command")
# If not error
else:
    # Strip the textlist
    textlist = delete_column(textlist, cols_list)
    # Output
    for line in textlist:
        print(line)