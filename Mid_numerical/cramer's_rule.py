# https://stackoverflow.com/questions/70323836/solving-system-of-linear-equation-using-cramers-method-in-python

import numpy as np


def cramer(mat, constant):  # takes the matrix and the costants

    D = np.linalg.det(mat)  # calculating the determinant of the original matrix

    # substitution of the column with costant and creating new matrix

    mat1 = np.array([constant, mat[:, 1], mat[:, 2]])
    mat2 = np.array([mat[:, 0], constant, mat[:, 2]])
    mat3 = np.array([mat[:, 0], mat[:, 1], constant])

    # calculatin determinant of the matrix
    D1 = np.linalg.det(mat1)
    D2 = np.linalg.det(mat2)
    D3 = np.linalg.det(mat3)

    # finding the X1, X2, X3
    X1 = D1 / D
    X2 = D2 / D
    X3 = D3 / D

    print(f"X1= {X1:.2f}\nX2= {X2:.2f}\nX3= {X3:.2f}")


# main function
a = np.array([[0.3, 0.52, 1],
             [0.5, 1, 1.9],
             [0.1, 0.3, 0.5]])

b = np.array([-0.01, 0.67, -0.44])

cramer(a, b)