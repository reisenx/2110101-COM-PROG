# Not guarantee 100/100 points on this code

# This function can check if 
# 1.) len(word) is not equal to len(pattern)
# Example: word = "MACMA", pattern = "M?C?????"
# 2.) Incorrect pattern
# Example: word = "MACMA", pattern = "X??X?"
def check_pattern(word,pattern):
    # Check len(word) and len(pattern)
    LengthValid = True
    if(len(pattern) != len(word)):
        LengthValid = False
    # Check incorrect pattern
    PatternValid = True
    if(not LengthValid):
        PatternValid = False
    else:
        for i in range(len(word)):
            # Skip a loop, if pattern[i] equal to '?'
            if(pattern[i] == '?'):
                continue
            elif(word[i] != pattern[i]):
                PatternValid = False
                break
    # Both must be True to return True
    return LengthValid and PatternValid

# This function return dictionary contains letter count of a input string
# Example: "MACMA" = {'A':2, 'C':1, 'M':2}
def count_letter(word):
    # Get a unique character in a input string and sort them in ascending order
    unique_char = []
    for char in word:
        if(char not in unique_char):
            unique_char.append(char)
    unique_char.sort()
    # Count each unique character and put them in a dictionary
    char_count = {}
    for char in unique_char:
        char_count[char] = word.count(char)
    # Return a dictionary
    return char_count

# This function can get a string of a character on symbol '?' in 'pattern'
# check_pattern(word,pattern) must returns True before use this function
# Example: word = "MACMA", pattern = "M?C??"
# This function returns "AMA"
def get_missing(word,pattern):
    # Create a string contains character on symbol '?' in 'pattern'
    missing = ""
    for i in range(len(word)):
        # Skip a loop, if pattern[i] not equal to '?'
        if(pattern[i] != '?'):
            continue
        else:
            missing += word[i]
    # Return a string
    return missing

# This function can check if a missing character have excluded character
# Example: missing = "AMA", exclude_chars = "MX"
# This function return True becuase it has 'M' in exclude_chars
def check_exclude(missing, exclude_chars):
    HaveExclude = False
    # Check exclude characters by count them in 'missing' string
    # Example: "AMA".count("M") = 1
    for char in exclude_chars:
        if(missing.count(char) > 0):
            HaveExclude = True
            break
    return HaveExclude

# Create match() function
# Input Parameters
# 1.) 'word' is a string contains only uppercase letters
# 2.) 'pattern' is a string contains only uppercase letters and '?' symbol
# 3.) 'include_chars' is a string contains only uppercase letters and guarantee that 
# a number of letters won't exceed number of '?' in 'pattern'
# 4.) 'exclude_chars' is a string contains only uppercase letters

# Output
# This function returns True when meets all citeria below
# 1.) len(word) must equal to len(pattern)
# 2.) All letters (not '?') in 'pattern' must match with 'word'
# 3.) All letters in 'word' at the '?' in 'pattern' must not have letter in 'exclude_chars'
# 4.) All letters in 'include_chars' must have a unique position at '?' in 'pattern'
def match(word, pattern, include_chars, exclude_chars):
    # Check citeria 1-2
    if(not check_pattern(word,pattern)):
        return False
    # Check citeria 3
    if(check_exclude(get_missing(word,pattern), exclude_chars)):
        return False
    # Check citeria 4
    # Example: match("MACMA", "M?C??", "AM", "")
    # missing_dict = {'A':2, 'M':1}
    # include_dict = {'A':1, 'M':1}
    missing_dict = count_letter(get_missing(word,pattern))
    include_dict = count_letter(include_chars)
    # Check if there are keys of 'include_dict' that isn't in a list of keys of 'missing_dict'
    # Example: match("MACMA", "M?C??", "MAX", "")
    # In this case list(include_dict.keys()) = ['A','M'] and list(missing_dict.keys()) = ['A','M','X']
    # There's no 'X' in 'missing' ("AMA") so the function returns False
    for letter in list(include_dict.keys()):
        if(letter not in list(missing_dict.keys())):
            return False
    # Check if all characters in 'include_chars' have a unique position at '?' in 'pattern'
    # Example: match("MACMA", "M?C??", "AAA", "")
    # In this case missing = "AMA" (which has only 2 'A') but include_chars has 3 'A'
    # So the function returns False
    else:
        for letter in include_dict:
            if(include_dict[letter] > missing_dict[letter]):
                return False
    # Else, the function returns True
    return True