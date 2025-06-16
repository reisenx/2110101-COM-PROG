# --------------------------------------------------
# File Name : 11_Numpy_13.py
# Problem   : Logistic Regression
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Calculate the probability of a binary outcome using logistic regression
def p(X: np.ndarray) -> np.ndarray:
    logit = -3.98 + (0.1 * X[:, 0]) + (0.5 * X[:, 1])
    return 1 / (1 + np.exp(-logit))


# Execute an input string as code
exec(input().strip())
