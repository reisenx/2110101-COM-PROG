def choose(stu1,stu2):
    id1, GPA1, Com1, Cal1_1, Cal2_1 = stu1[0], stu1[1], stu1[2], stu1[3], stu1[4]
    id2, GPA2, Com2, Cal1_2, Cal2_2 = stu2[0], stu2[1], stu2[2], stu2[3], stu2[4]

    if(Com1 == "A" and Cal1_1 <= "C" and Cal2_1 <= "C"):
        status1 = True
    else:
        status1 = False
    if(Com2 == "A" and Cal1_2 <= "C" and Cal2_2 <= "C"):
        status2 = True
    else:
        status2 = False

    if(status1 and status2):
        if(GPA1==GPA2):
            
            if(Cal1_1 == Cal1_2):
                
                if(Cal2_1 == Cal2_2):
                    return [id1,id2]
                elif(Cal2_1 < Cal2_2):
                    return [id1]
                elif(Cal2_2 < Cal2_1):
                    return [id2]
            
            elif(Cal1_1 < Cal1_2):
                return [id1]
            elif(Cal1_2 < Cal1_1):
                return [id2]
        
        elif(GPA1 > GPA2):
            return [id1]
        elif(GPA2 > GPA1):
            return [id2]
    
    elif(status1):
        return [id1]
    elif(status2):
        return [id2]
    else:
        return []

exec(input())