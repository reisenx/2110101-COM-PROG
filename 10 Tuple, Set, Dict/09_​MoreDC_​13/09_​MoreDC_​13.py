# Input number of input team
n = int(input())

# Input team in each football match in the format
# [Winning team] [Losing team]
win = set()
lose = set()
for i in range(n):
    data = input().split()
    # Input winning team and losing team in a set to prevent duplicates
    win.add(data[0])
    lose.add(data[1])

# Find all winning team that never lose by subtracting set
# Because winning team that never lose must not appear in 'lose' set 
ans = win - lose

# Output a list of winning team that never lose in alphabetical order
# sorted() function always returns a list 
print(sorted(ans))