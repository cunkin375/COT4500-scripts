"""
This module implements the False Position Method (Regula Falsi) for root finding.
"""
import csv
import math


def false_position(func, a, b, tolerance, max_iter=50, output_file="false_position_results.csv"):
    """
    Implements the False Position Method (Regula Falsi) to find a root of a function.

    Args:
        func: The function for which to find the root.
        a: First initial guess (lower bound of bracket).
        b: Second initial guess (upper bound of bracket).
        tolerance: Error tolerance (10^-n). The loop stops when |p_n - p_{n-1}| < tolerance.
        max_iter: Maximum number of iterations to prevent infinite loops.
        output_file: Name of the CSV file to write results to.
    """

    # Format: (iteration, p_n, error)
    iterations = []

    # Calculate decimal places for rounding
    decimal_places = int(-math.log10(tolerance)) + 1

    # Check if initial guesses bracket the root
    if func(a) * func(b) >= 0:
        print("Warning: Initial guesses do not bracket the root. The method may fail.")
        # Proceeding anyway as per "similar to secant" request, though standard FP requires bracket.

    # Store initial guesses similar to Secant script
    # Iteration 0: a
    # Iteration 1: b
    iterations.append((0, round(a, decimal_places), "N/A"))
    iterations.append((1, round(b, decimal_places),
                      round(abs(b - a), decimal_places)))

    p_prev = b
    current_a = a
    current_b = b

    # Main loop
    for i in range(2, max_iter + 2):
        fa = func(current_a)
        fb = func(current_b)

        if fb - fa == 0:
            print("Division by zero error in False Position Method.")
            break

        # Calculate p_next (root approximation)
        # Use the secant method formula
        p_next = current_a - fa * (current_b - current_a) / (fb - fa)

        # Calculate error (change from previous estimate)
        error = abs(p_next - p_prev)

        # Store result
        iterations.append((i, round(p_next, decimal_places),
                          round(error, decimal_places)))

        # Check tolerance
        if error < tolerance:
            print(f"Converged to root: {p_next} after {i} iterations.")
            break

        # Update bracket
        # If f(current_a) and f(p_next) have opposite signs, root is in [current_a, p_next]
        # otherwise root is in [p_next, current_b]
        if func(current_a) * func(p_next) < 0:
            current_b = p_next
            # current_a stays same
        else:
            current_a = p_next
            # current_b stays same

        p_prev = p_next

    else:
        print("Maximum iterations reached without convergence.")

    # Write to CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["$n$", "$p_n$", "Error $|p_n - p_{n-1}|$"])
        for row in iterations:
            writer.writerow(row)

    print(f"Results written to {output_file}")


if __name__ == "__main__":
    def f(x):
        """
        The function to find the root of.

        Args:
            x: The value to evaluate.

        Returns: The value of the function at x.
        """
        return math.e**(-x) - 0.2

    P0 = 0.0
    P1 = 2.0

    TOLERANCE = 1e-3

    false_position(f, P0, P1, TOLERANCE)
