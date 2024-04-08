import math
W = float(input())
H = float(input())

mos = math.sqrt(W*H)/60
print(mos)
hay = 0.024265*(W**0.5378)*(H**0.3964)
print(hay)
boyd = 0.0333*(W**(0.6157-(0.0188*math.log10(W))))*(H**0.3)
print(boyd)