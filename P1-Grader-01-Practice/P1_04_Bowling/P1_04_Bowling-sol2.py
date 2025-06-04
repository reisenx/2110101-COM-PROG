# Input
result = input().strip()
display = int(input())

# Convert 'result' to a list of number
# Strike ('X') = 10
# Spare ('/')  = 10-number  (Example: '2/' <-- '/' = 10-2 = 8)
result_score = []
for i in range(len(result)):
    if(result[i] == 'X'):
        result_score.append(10)
    elif(result[i] == '/'):
        result_score.append(10 - int(result[i-1]))
    else:
        result_score.append(int(result[i]))

# Calculate score in each frame and put it in 'frame_score' list
# - If start with 10, it must be Strike ('X')
# - If sum of any 2 frames = 10, it must be Spare ('/')
frame = 1
frame_score = []
index = 0
while(frame <= 10):
    # Strike ('X')
    if(result_score[index] == 10):
        score = sum(result_score[index : index+3])
        frame_score.append(score)
        index += 1
    
    # Spare ('/')
    elif(sum(result_score[index : index+2]) == 10):
        score = sum(result_score[index : index+3])
        frame_score.append(score)
        index += 2
    
    # Numbers
    else:
        score = sum(result_score[index : index+2])
        frame_score.append(score)
        index += 2
    
    # Add 'frame' by 1 each loop
    frame += 1

# Output
if(1 <= display <= 10):
    print(frame_score[display - 1])
else:
    print(sum(frame_score))