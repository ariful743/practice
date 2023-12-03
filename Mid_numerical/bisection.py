def bisection_method_auto_interval(func, interval_range=1.0, tol=1e-6, max_iter=100):
    """
    Bisection method to find the root of a given function with automatic interval calculation.

    Parameters:
    - func: The target function.
    - interval_range: Range around the automatically determined initial guess within which to search for the interval (default is 1.0).
    - tol: Tolerance for stopping criterion (default is 1e-6).
    - max_iter: Maximum number of iterations (default is 100).

    Returns:
    - root: Approximate root of the function.
    - iterations: Number of iterations performed.
    """
    # Find an initial guess by searching for a sign change within the interval range
    initial_guess = 0.0
    sign_change_found = False

    while initial_guess < 1e6:  # Add a safety check to avoid an infinite loop
        if func(initial_guess) * func(initial_guess + interval_range) <= 0:
            sign_change_found = True
            break
        initial_guess += interval_range

    if not sign_change_found:
        raise ValueError("Unable to find an initial guess with a sign change in the specified range.")

    # Automatically calculate the interval
    a = initial_guess
    b = initial_guess + interval_range

    print(f"Iteration\t a\t\t b\t\t\t c\t\t\t f(c)")

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {func(c):.6f}")

        if func(c) == 0:
            # Exact root found
            return c, iteration + 1
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    root = (a + b) / 2
    print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {root:.6f}\t {func(root):.6f}")
    return root, iteration


# Example usage with automatic interval calculation and no explicit initial guess:
def target_function(x):
    return x ** 2 - 3  # Example function: f(x) = x^2 - 3

root, iterations = bisection_method_auto_interval(target_function)

print(f"\nRoot found: {root}")
print(f"Iterations: {iterations}")