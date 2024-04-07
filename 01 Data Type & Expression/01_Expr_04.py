# Import Math library
import math

# Input W and H as float variable
# W is a width of a medicine
# H is a height of a medicine
W = float(input())
H = float(input())

# Calculate and Output body surface area using Mosteller's formula
mos = math.sqrt(W*H)/60
print(mos)

# Calculate and Output body surface area using Haycock's formula
hay = 0.024265*(W**0.5378)*(H**0.3964)
print(hay)

# Calculate and Output body surface area using Boyd's formula
boyd = 0.0333*(W**(0.6157-(0.0188*math.log10(W))))*(H**0.3)
print(boyd)
