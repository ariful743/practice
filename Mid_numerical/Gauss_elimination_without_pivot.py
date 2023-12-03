import numpy as np
import sys

# Reading number of unknowns
n = 3


# Making numpy array of n size and initializing
# to zero for storing solution vector
x = np.zeros(n)

# Define augmented matrix coefficients
# Example matrix, you can modify this based on your problem
a = np.array([
    [0.3, 0.52, 1, -0.01],
    [0.5, 1, 1.9, 0.67],
    [0.1, 0.3, 0.5, -0.44]
], dtype=float)

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')