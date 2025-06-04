start, stop, step = [int(e) for e in input().split()]
# No data occurs when
# 1.) start = stop (Ex. list[9:9:1])
# 2.) start > stop but step > 0 (Ex. list[12:5:1])
# 3.) start < stop but step < 0 (Ex. list[5:10:-1])
if(start == stop or (start < stop and step < 0) or (start > stop and step > 0)):
    print("No data")
else:
    # Members Calculation
    # Example:
    # list[0:1:2] = [0]   | list[0:13:2] = [0,2,4,6,8,10,12]
    # list[0:2:2] = [0]   | list[0:14:2] = [0,2,4,6,8,10,12]
    # list[0:3:2] = [0,2] | list[0:15:2] = [0,2,4,6,8,10,12,14]
    # list[0:4:2] = [0,2] | list[0:16:2] = [0,2,4,6,8,10,12,14]
    members = (stop - start - 1)//step + 1
    nums = []
    # Has 1-5 numbers
    if(members <= 5):
        for num in range(start,stop,step):
            nums.append(str(num))
    # Has more than 5 number
    else:
        # Add first two number
        nums.append(str(start))
        nums.append(str(start + step))
        nums.append("...")
        # Add last two number
        nums.append(str(start + (members-2)*step))
        nums.append(str(start + (members-1)*step))
    # Output
    print(", ".join(nums))