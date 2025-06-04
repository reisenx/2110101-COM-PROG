# Input a grade
# "A B C B" --> ["A", "B", "C", "B"]
grade_list = input().split()

# Convert grade to a number then find a sum of them
# A = 4; B = 3; C = 2; D = 1; F = 0
grade_sum = 0
for i in range(0,len(grade_list)):
    if(grade_list[i] == 'A'):
        grade_sum = grade_sum + 4
    elif(grade_list[i] == 'B'):
        grade_sum = grade_sum + 3
    elif(grade_list[i] == 'C'):
        grade_sum = grade_sum + 2
    elif(grade_list[i] == 'D'):
        grade_sum = grade_sum + 1

# Calculate and output the GPA

print(round(grade_sum/len(grade_list),2))