# Set the initial value
N = 0
min_01 = 0
max_01 = 0
min_02 = 0
max_02 = 0

# Input a data until input Zig-Zag or Zag-Zig
while(True):
    # Input a string
    txt = str(input())

    # Zig-Zag: Output Min 01 and Max 02 then break
    if(txt == "Zig-Zag"):
        print(min_01,max_02)
        break
    
    # Zag-Zig: Min 02 and Max 01
    elif(txt == "Zag-Zig"):
        print(min_02,max_01)
        break
    
    # Input data in line N = 0
    elif(N == 0):
        data = [int(e) for e in txt.split()]
        min_01 = data[0]
        max_01 = data[0]
        min_02 = data[1]
        max_02 = data[1]
        
        # Add the line count by 1
        N += 1
    
    # Input data in line N >= 1
    elif(N >= 1):
        # data[0] is X and data[1] is Y of line N
        # Min 01 is the minimum value of the sequence X0,Y1,X2,Y3,X4,Y5,... (Index starts at 0)
        # Max 01 is the maximum value of the sequence X0,Y1,X2,Y3,X4,Y5,... (Index starts at 0)
        # Min 02 is the minimum value of the sequence Y0,X1,Y2,X3,Y4,X5,... (Index starts at 0)
        # Max 02 is the maximum value of the sequence Y0,X1,Y2,X3,Y4,X5,... (Index starts at 0)
        data = [int(e) for e in txt.split()]
        if(N%2 == 1):
            min_01 = min(min_01, data[1])
            max_01 = max(max_01, data[1])
            min_02 = min(min_02, data[0])
            max_02 = max(max_02, data[0])
        elif(N%2 == 0):
            min_01 = min(min_01, data[0])
            max_01 = max(max_01, data[0])
            min_02 = min(min_02, data[1])
            max_02 = max(max_02, data[1])
        
        # Add the line count by 1
        N += 1