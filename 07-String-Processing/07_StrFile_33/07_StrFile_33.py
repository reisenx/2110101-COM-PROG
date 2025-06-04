# Create function to read 1 line in a text file
# If it there no data in that line, return 2 empty string
# data[0] is ID and data[1] is GPA
def read_next(filename):
    while True:
        line = filename.readline()
        if(len(line) == 0):
            break
        data = line.strip().split()
        if(len(data) == 2):
            return data[0],data[1]
    return "",""

# Input 2 filenames then open 2 files
filename01, filename02 = input().strip().split()
file01 = open(filename01,"r")
file02 = open(filename02,"r")

# Output
# Since data in both files are in order already, so we can compare each line in both files
# 1.) Compare faculty (Example: 66322002[21])
# 2.) Compare ID
ID01, GPA01 = read_next(file01)
ID02, GPA02 = read_next(file02)
while True:
    if(ID01 == "" and ID02 == ""):
        break

    elif(ID02 == ""):
        print(ID01,GPA01)
        ID01, GPA01 = read_next(file01)

    elif(ID01 == ""):
        print(ID02,GPA02)
        ID02, GPA02 = read_next(file02)

    elif(ID01[-2:] < ID02[-2:]):
        print(ID01,GPA01)
        ID01, GPA01 = read_next(file01)

    elif(ID02[-2:] < ID01[-2:]):
        print(ID02,GPA02)
        ID02, GPA02 = read_next(file02)

    elif(ID01[-2:] == ID02[-2:]):
        if(ID01 < ID02):
            print(ID01,GPA01)
            ID01, GPA01 = read_next(file01)
            
        elif(ID02 < ID01):
            print(ID02,GPA02)
            ID02, GPA02 = read_next(file02)

# Close files
file01.close()
file02.close()