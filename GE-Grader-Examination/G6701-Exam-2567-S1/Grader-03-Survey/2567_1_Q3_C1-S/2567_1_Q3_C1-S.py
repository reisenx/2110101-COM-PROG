# Input N
N = int(input())

# Problem: How many solution of 10A + 5B + 2C + D = N
# Constrains
# 1.) 0 <= N <= 100
# 2.) 0 <= B,C,D <= 9
# 3.) 0 <= A <= 10 (Since N <= 100)

# Since N <= 100, we can simply use a nested for loop
solutions = 0
for A in range(11):
    for B in range(10):
        for C in range(10):
            for D in range(10):
                if(10*A + 5*B + 2*C + D == N):
                    solutions += 1
# Output
print(solutions)