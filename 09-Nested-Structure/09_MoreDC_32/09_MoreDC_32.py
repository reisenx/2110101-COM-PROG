# First fit
# - Consider the data from left to right
# - If a number can fit in the sublist (sum(sublist) + number <= 100), put that number in that sublist
# - If it has no sublist that fit, create new a sublist at the end
# Example: 10 --> [[50],[90]]
# Sublist 1: 50+10 < 100 --> [[50,10],[90]]
def first_fit(L, num):
    FitAble = False
    # If a number can fit in a sublist, put the number in a sublist
    for i in range(len(L)):
        if(sum(L[i]) + num <= 100):
            L[i].append(num)
            FitAble = True
            break
    # If a number can't fit in a sublist, create a new sublist at the end
    if(not FitAble):
        L.append([num])
    return L

# Best fit
# - Consider all data
# - Find a sublist that sum(sublist) + number near 100 the most (Also sum(sublist) + number <= 100)
# - If it has no sublist that fit, create a sublist at the end
# Example: 10 --> [[50],[90]]
# Sublist 1: 50+10 = 60
# Sublist 2: 90+10 = 100
# Choose Sublist 2 --> [[50],[90,10]]
def best_fit(L, num):
    # Find a difference between sum(sublist)+number and 100 in each sublist
    # If the sublist is impossible to fit, then input 100
    diff = [100]*len(L)
    for i in range(len(L)):
        if(sum(L[i]) + num <= 100):
            diff[i] = 100 - (sum(L[i]) + num)
    # Find an index that have the minimum difference
    # If it is possible to fit, minimum difference must not be 100 and diff must not an empty list
    if(diff == []):
        L.append([num])
    elif(min(diff) < 100):
        index = diff.index(min(diff))
        L[index].append(num)
    else:
        L.append([num])
    return L

# Partition FF (First Fit)
# Example: D = [50,90,10,80,50,20]
# Loop 6 times
# Loop 1: Put 50 to FF = []
# > FF = [[50]]
# Loop 2: Put 90 to FF = [[50]]
# > FF = [[50],[90]]
# Loop 3: Put 10 to FF = [[50],[90]]
# > FF = [[50,10],[90]]
# Loop 4: Put 80 to FF = [[50,10],[90]]
# > FF = [[50,10],[90],[80]]
# Loop 5: Put 50 to FF = [[50,10],[90],[80]]
# > FF = [[50,10],[90],[80],[50]]
# Loop 6: Put 20 to FF = [[50,10],[90],[80],[50]]
# > FF = [[50,10,20],[90],[80],[50]]
def partition_FF(D):
    FF = []
    for num in D:
        FF = first_fit(FF, num)
    return FF

# Partition BF (Best Fit)
# Example: D = [50,90,10,80,50,20]
# Loop 6 times
# Loop 1: Put 50 to BF = []
# > BF = [[50]]
# Loop 2: Put 90 to BF = [[50]]
# > BF = [[50],[90]]
# Loop 3: Put 10 to BF = [[50],[90]]
# > BF = [[50],[90,10]]
# Loop 4: Put 80 to BF = [[50],[90,10]]
# > BF = [[50],[90,10],[80]]
# Loop 5: Put 50 to BF = [[50],[90,10],[80]]
# > BF = [[50,50],[90,10],[80]]
# Loop 6: Put 20 to BF = [[50,50],[90,10],[80]]
# > BF = [[50,50],[90,10],[80,20]]
def partition_BF(D):
    BF = []
    for num in D:
        BF = best_fit(BF, num)
    return BF

# Execute an input string
exec(input().strip())