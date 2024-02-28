# Input a string 
word = str(input())

# Create a list that contains vowel
vowel = ['a','e','i','o','u']

# Convert a word into plural
# 1.) If a word end with -s, -x or -ch then add -es at the end
# 2.) If a word end with -y and a letter before y is not a vowel then change -y to -i then add -es
# 3.) Else, add -s
if(word[-1] == 's' or word[-1] == 'x' or word[-2:] == 'ch'):
    plural = word + "es"
elif(word[-1] == 'y' and word[-2] not in vowel):
    plural = word[:-1] + 'ies'
else:
    plural = word + 's'

# Output
print(plural)