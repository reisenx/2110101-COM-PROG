# Create a dictionary that can convert row letter to a number
# alpha_to_num = {'a':1. 'b':2, 'c':3, ...}
# Example: row = "A" --> row = 27
alpha_to_num = {}
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for num in range(1,53):
    alpha_to_num[alpha[num-1]] = num

# This function can check that it is black or white
# Example:
# > a1 --> row = 1 and col = 1 --> White
# > b2 --> row = 2 and col = 2 --> White
# > x52 --> row = 24 and col = 52 --> White
# > A35 --> row = 27 and col = 35 --> White
def white_or_black(row, col):
    if(row%2 == col%2):
        return "White"
    else:
        return "Black"

# This function can convert 'row' and 'col' parameter to row and column number
# If it is invalid, this function will return an empty string instead
# Example: row_column_convert(r,3 1) returns row = 18 and column = 31
def row_column_convert(row,col):
    # Strip row and col
    new_row = row.strip()
    new_col = col.strip()
    
    # Check 'new_row' if it is all alphabet and only have 1 letter (Otherwise, reset to empty string)
    if(not new_row.isalpha() or len(new_row) != 1):
        new_row = ""
    # Check 'new_col' if it is all number and between 1-52 (Otherwise, reset to empty string)
    if(not new_col.isnumeric()):
        new_col = ""
    elif(int(new_col) < 1 or int(new_col) > 52):
        new_col = ""

    # Convert 'new_row' to number (If valid) 
    if(new_row != ""):
        new_row = alpha_to_num[new_row]
    # Convert 'new_col' to number (If valid)
    if(new_col != "" and 1 <= int(new_col) <= 52):
        new_col = int(new_col)
    
    # Return 'new_row' and 'new_col' value
    return new_row, new_col

# This function returns row and column from a text in pattern01
# pattern01 is a text that less or equal than 3 characters when strip()
# The first letter is row and the rest are column
# Example: pattern01("r3w") returns row = 'r' and col = '3w'
def pattern01(text):
    row = text[0]
    col = text[1:]
    return row,col

# This function returns row and column from a text in pattern02
# pattern02 is a text in pattern "row = ??? ,col = ???"
# Example: pattern02("row = AAA ,col=0 9") returns row = "AAA" and col = "0 9"
def pattern02(text):
    # It is guaruntee that ',' will appear once and '=' will appear twice
    # So we replace text ',' to '=' to make it easier to split
    new_text = text.replace(',', '=')
    
    # Split 'new_text' into a list then strip each items in a list
    data = [item.strip() for item in new_text.strip().split('=')]
    
    # Case 1: ['row','???','col','???']
    if(data[0] == 'row' and data[2] == 'col'):
        row = data[1]
        col = data[3]
    # Case 2: ['col','???','row','???']
    elif(data[0] == 'col' and data[2] == 'row'):
        row = data[3]
        col = data[1]
    
    # Return a row and col value
    return row,col

# Input a text
text = input().strip()

# Get row and column from the input
if(len(text) <= 3):
    row,col = pattern01(text)
else:
    row,col = pattern02(text)

# Convert row can col into a number
row,col = row_column_convert(row,col)

# Output
# Check if row, col are valid
if(row == "" and col == ""):
    print("Invalid row and column")
elif(row == ""):
    print("Invalid row")
elif(col == ""):
    print("Invalid column")
else:
    print(white_or_black(row,col))