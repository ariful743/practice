import numpy as np

# Define the masses and spring constants
m1 = 2.0  # kg
m2 = 3.0  # kg
m3 = 2.5  # kg
k = 10.0  # N/m

# Define the gravitational acceleration
g = 9.81  # m/s^2

# Set up the system of equations
A = np.array([[k, -k, 0],
              [-k, k + k, -k],
              [0, -k, k + k]])
b = np.array([-m1 * g, -m2 * g, -m3 * g])

# Solve the system of equations
x = np.linalg.solve(A, b)

# Print the displacements
print("Displacement of mass 1:", x[0], "m")
print("Displacement of mass 2:", x[1], "m")
print("Displacement of mass 3:", x[2], "m")