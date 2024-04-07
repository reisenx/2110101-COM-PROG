# Input
result = str(input().strip())
frame_display = int(input())
index = 0
total_score = 0

# Create a list
frame_score = []
number = ['0','1','2','3','4','5','6','7','8','9']

# Calculate a score
# 1.) 1 frame = 2 turns but if 'X', then go to the next turn
# 2.) If 'X', score = 10 + next 2 turns
# 3.) If '/', score = 10 + next 1 turn
for frame in range(1,11):
    # Case 1: XXX = 30
    if(result[index] == 'X' and result[index+1] == 'X' and result[index+2] == 'X'):
        total_score = total_score + 30
        frame_score.append(30)
        index = index + 1
    
    # Case 2: XX? = 20 + ?
    elif(result[index] == 'X' and result[index+1] == 'X' and result[index+2] in number):
        score = 20 + int(result[index+2])
        total_score = total_score + score
        frame_score.append(score)
        index = index + 1
    
    # Case 3: X?/ = 20
    elif(result[index] == 'X' and result[index+1] in number and result[index+2] == '/'):
        total_score = total_score + 20
        frame_score.append(20)
        index = index + 1
    
    # Case 4: X?? = 10 + ? + ?
    elif(result[index] == 'X' and result[index+1] in number and result[index+2] in number):
        score = 10 + int(result[index+1]) + int(result[index+2])
        total_score = total_score + score
        frame_score.append(score)
        index = index + 1
    
    # Case 5: ?/X = 20
    elif(result[index] in number and result[index+1] == '/' and result[index+2] == 'X'):
        total_score = total_score + 20
        frame_score.append(20)
        index = index + 2
    
    # Case 6: ?/? = 10 + ?
    elif(result[index] in number and result[index+1] == '/' and result[index+2] in number):
        score = 10 + int(result[index+2])
        total_score = total_score + score
        frame_score.append(score)
        index = index + 2
    
    # Case 7: ?? = ? + ?
    elif(result[index] in number and result[index+1] in number):
        score = int(result[index]) + int(result[index+1])
        total_score = total_score + score
        frame_score.append(score)
        index = index + 2

# Output
# If frame_display is between 1-10, output the its frame score
# Else, output the total score
if(frame_display in range(1,11)):
    print(frame_score[frame_display - 1])
else:
    print(total_score)