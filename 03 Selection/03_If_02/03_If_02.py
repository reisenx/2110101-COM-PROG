# Input 2 strings
student1 = str(input())
student2 = str(input())

# Split a string to gain an information about each student
# Don't forget to convert a GPA from string to float
id1, GPA1, Com1, Cal1_1, Cal2_1 = student1.split()
id2, GPA2, Com2, Cal1_2, Cal2_2 = student2.split()
GPA1,GPA2 = float(GPA1),float(GPA2)

# == Requirement ==
# 1.) Com Prog A, Calculus I and Calculus II >= C
# 2.) Select the one that has more GPA
# 3.) If same GPA, Select the one that has more Calculus I grade
# 4.) If same Calculus I grade, Select the one that has more Calculus II grade
# 5.) If all GPA, Calculus I and Calculus II are the same, select both

# Check if student pass the first requirement
# Please don't forget that in string comparison: A < B < C < D < F
if(Com1 == 'A' and Cal1_1 <= 'C' and Cal2_1 <= 'C'):
    status1 = True
else:
    status1 = False
if(Com2 == 'A' and Cal1_2 <= 'C' and Cal2_2 <= 'C'):
    status2 = True
else:
    status2 = False

# Checking in 1st citeria
# Case 1: Both pass the 1st citeria
if(status1 and status2):
    # Checking in 2nd citeria (GPA)
    if(GPA1 == GPA2):
        
        # Checking in 3rd citeria (Calculus I Grade)
        if(Cal1_1 == Cal1_2):
            
            # Checking in 4th citeria (Calculus II Grade)
            if(Cal2_1 == Cal2_2):
                print("Both")
            elif(Cal2_1 < Cal2_2):
                print(id1)
            elif(Cal2_2 < Cal2_1):
                print(id2)
        
        elif(Cal1_1 < Cal1_2):
            print(id1)
        elif(Cal1_2 < Cal1_1):
            print(id2)
    
    elif(GPA1 > GPA2):
        print(id1)
    elif(GPA2 > GPA1):
        print(id2)

# Case 2: Only student 1 pass 1st citeria
elif(status1):
    print(id1)

# Case 3: Only student 2 pass 1st citeria
elif(status2):
    print(id2)

# Case 4: None pass the 1st citeria
else:
    print("None")