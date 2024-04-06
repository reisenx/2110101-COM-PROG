import numpy as np

# This function can convert temperature in farenheit to celsius
# F is an 1D array that contains temperature in fahrenheit
# C = (F-32)/1.8
def toCelsius(F):
    celsius = (F-32)/1.8
    return celsius

# This function can calculate BMI from input array
# wh is an 2D array (nx2) that contains [[w1 h1] [w2 h2] ...] (weight in kg and height in cm) 
# So wh[:,0] is vector of weight and w[:,1] is vector of height
# Example: wh = [[60 170] [50 160]] --> wh[:,0] = [60 50] and wh[:,1] = [170 160]
# BMI = weight/(height^2) <-- height in m
def BMI(wh):
    weight = wh[:,0]
    height = wh[:,1] / 100
    return weight / (height**2)

# This function can calculate distance from 'p' to each coordinate in 'Points'
# p is an 1D array that contains [x0 y0] --> p[0] = x0 and p[1] = y0
# Points is an 2D array that contains [[x1 y1] [x2 y2] ...]
# > Points[:,0] is vector of x-coordinate = [x1 x2 x3 ...]
# > Points[:,1] is vector of y-coordinate = [y1 y1 y2 ...]
# Example: p = [0 0] and Points [[3 0] [0 4] [3 4]] returns [3. 4. 5.]
def distanceTo(p, Points):
    distance_x = Points[:,0] - p[0]
    distance_y = Points[:,1] - p[1]
    return ((distance_x**2) + (distance_y**2))**0.5

# Execute an input string
exec(input().strip())