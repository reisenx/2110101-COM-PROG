import numpy as np
import math

# == Formula ==
# p(x) = 1/(1+e^(-logit(x)))
# logit(x) = -3.98 + 0.1x0 + 0.5x1

# X is an 2D array (nx2 size) contains [[x0_1 x1_1] [x0_2 x1_2] [x0_3 x1_3] ... [x0_n x1_n]]
# X[:,0] = [x0_1 x0_2 x0_3 ... x0_n]
# X[:,1] = [x1_1 x1_2 x1_3 ... x1_n]
def p(X):
    logit = -3.98 + (0.1*X[:,0]) + (0.5*X[:,1])
    p = 1/(1 + math.e**(-logit))
    return p

# Execute an input string
exec(input().strip())