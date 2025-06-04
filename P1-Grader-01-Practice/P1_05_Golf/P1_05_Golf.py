# Import math library
import math

# Create and empty list and necessary variable
par_list = []
stroke_list = []
mod_stroke_list = []

# Input a string of each hole, split them, then put them in the list
# Each line contains [Par] [Stroke] [Select]

# == Modified stroke ==
# - If select = 1, mod_stroke = min(stroke, par+2)
# - If select = 0, mod_stroke = 0
for i in range(9):
    par,stroke,select = [int(e) for e in input().split()]
    if(select == 1):
        mod_stroke = min(stroke, par+2)
    else:
        mod_stroke = 0
    par_list.append(par)
    stroke_list.append(stroke)
    mod_stroke_list.append(mod_stroke)

# Calculate a handicap and score
handicap = math.floor(0.8*(1.5*sum(mod_stroke_list) - sum(par_list)))
score = sum(stroke_list) - handicap

# Output a sum of stroke, handicap and score
print(sum(stroke_list))
print(handicap)
print(score)