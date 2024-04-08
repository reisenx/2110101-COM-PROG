student1 = str(input())
student2 = str(input())
id1, GPA1, Com1, Cal1_1, Cal2_1 = student1.split()
id2, GPA2, Com2, Cal1_2, Cal2_2 = student2.split()
GPA1,GPA2 = float(GPA1),float(GPA2)

if(Com1 == 'A' and Cal1_1 <= 'C' and Cal2_1 <= 'C'):
    status1 = True
else:
    status1 = False
if(Com2 == 'A' and Cal1_2 <= 'C' and Cal2_2 <= 'C'):
    status2 = True
else:
    status2 = False

if(status1 and status2):
    if(GPA1 == GPA2):

        if(Cal1_1 == Cal1_2):

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

elif(status1):
    print(id1)
elif(status2):
    print(id2)
else:
    print("None")