# Input number of department
n = int(input())

# Input department details which contains
# [Department] [Number of student]
# Example: "CP 1"
# Put a data in a dictionary 'department_len' and 'department_sid'
# department_len = {'CP':1, 'ME':2, 'PE':1, 'CHE':1, 'MT':3}
# department_sid = {'CP':[], 'ME':[], 'PE':[], 'CHE':[], 'MT':[]}
department_len = {}
department_sid = {}
for i in range(n):
    department, student = input().strip().split()
    department_len[department] = int(student)
    department_sid[department] = []

# Input number of student
m = int(input())

# Input student details which contains
# [Student ID] [Score] [Rank 1] [Rank 2] [Rank 3] [Rank 4]
# Example: "59301234521 23.6 PE CP MT CHE"
# Put a data in a dictionary 'students_rank', 'std2score' and 'score2std''
# It is guarantee that all student will have different score 
# students_rank = {'59301234521' : ['PE', 'CP', 'MT', 'CHE'], ...}
# std2score = {'59301234521':23.6, '59300799921':44.5, ...}
# score2std = {23.6:'59301234521', 44.5:'59300799921', ...}
students_rank = {}
std2score = {}
score2std = {}
for i in range(m):
    ID, score, rank1, rank2, rank3, rank4 = input().strip().split()
    score = float(score)
    students_rank[ID] = [rank1, rank2, rank3, rank4]
    std2score[ID] = score
    score2std[score] = ID

# Select department for each student
std_department = []
# 1.) Get all input student ID
ID_list = list(students_rank.keys())
# 2.) Convert and sorting score in descending order
score_list = []
for ID in ID_list:
    score_list.append(std2score[ID])
score_list.sort(reverse = True)
# 3.) Convert score back to student ID
ID_list = []
for score in score_list:
    ID_list.append(score2std[score])
# 4.) Try to put ID in their ranking order. If put, note ID in 'department_std' and 'std_department'
for ID in ID_list:
    rank1, rank2, rank3, rank4 = students_rank[ID]
    # Consider rank1 of that student
    if(len(department_sid[rank1]) < department_len[rank1]):
        department_sid[rank1].append(ID)
        std_department.append([ID,rank1])
    # Consider rank2 of that student
    elif(len(department_sid[rank2]) < department_len[rank2]):
        department_sid[rank2].append(ID)
        std_department.append([ID,rank2])
    # Consider rank3 of that student
    elif(len(department_sid[rank3]) < department_len[rank3]):
        department_sid[rank3].append(ID)
        std_department.append([ID,rank3])
    # Consider rank4 of that student
    elif(len(department_sid[rank4]) < department_len[rank4]):
        department_sid[rank4].append(ID)
        std_department.append([ID,rank4])

# Output
std_department.sort()
for ID, department in std_department:
    print(ID, department)