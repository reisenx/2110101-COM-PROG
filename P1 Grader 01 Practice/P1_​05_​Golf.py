# Import math library
import math

# Create and empty list and necessary variable
par = []
stroke = []
select = []
mod_stroke = []
sum_par = 0
sum_stroke = 0
sum_mod_stroke = 0

# Input a string of each hole, split them, then put them in the list
# Each hole: [par, stroke, select]
for i in range(0,9):
    hole = [int(e) for e in input().split()]
    par.append(hole[0])
    stroke.append(hole[1])
    select.append(hole[2])

# Calculate the modified stroke
# Calculate the sum of par, sum of stroke and sum of modified stroke
# Modified stroke = min(stroke, par+2)
# If select = 0, modified stroke = 0
for i in range(0,9):
    if(select[i]==1):
        mod_stroke.append(min(stroke[i], par[i]+2))
    elif(select[i]==0):
        mod_stroke.append(0)
    sum_par = sum_par + par[i]
    sum_stroke = sum_stroke + stroke[i]
    sum_mod_stroke = sum_mod_stroke + mod_stroke[i]

# Calculate a score
handicap = math.floor(0.8*(1.5*sum_mod_stroke - sum_par))
score = sum_stroke - handicap

# Output a sum of stroke, handicap and score
print(sum_stroke)
print(handicap)
print(score)