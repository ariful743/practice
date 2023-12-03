import numpy as np

def gaussian_elimination_with_pivot(A, b):
    n = len(b)
    # Augmenting the matrix A with the column vector b
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))

    for i in range(n):
        # Partial Pivoting: Find the row with the maximum absolute value in the current column
        pivot_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        # Swap the current row with the pivot row
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

        # Make the diagonal element 1
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]

        # Eliminate the values below the pivot
        for j in range(i + 1, n):
            augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]

    # Back-substitution to find the solution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:])

    return x

# Example usage:
A = np.array([[0.3, 0.52, 1],
              [0.5, 1, 1.9],
              [0.1, 0.3, 0.5]])

b = np.array([-0.01, 0.67, -0.44])

solution = gaussian_elimination_with_pivot(A, b)
print("Solution:", solution)