"""
This module implements the secant method for root finding.
"""
import csv
import math


def secant_method(func, p0, p1, tolerance, max_iter=50, output_file="secant_results.csv"):
    """
    Implements the Secant Method to find a root of a function.

    Args:
        func: The function for which to find the root.
        p0: First initial guess.
        p1: Second initial guess.
        tolerance: Error tolerance (10^-n). The loop stops when |p_n - p_{n-1}| < tolerance.
        max_iter: Maximum number of iterations to prevent infinite loops.
        output_file: Name of the CSV file to write results to.
    """

    # Format: (iteration, p_n, error)
    iterations = []

    decimal_places = int(-math.log10(tolerance)) + 1

    current_p_minus_1 = p0
    current_p = p1

    # Store initial guesses
    iterations.append((0, round(current_p_minus_1, decimal_places),
                          round(func(current_p_minus_1), decimal_places), "N/A"))
    iterations.append((1, round(current_p, decimal_places),
                          round(func(current_p), decimal_places),
                          round(abs(current_p - current_p_minus_1), decimal_places)))

    for i in range(2, max_iter + 2):
        if func(current_p) - func(current_p_minus_1) == 0:
            print(
                f"Division by zero error in Secant Method with p0 = {current_p_minus_1} \
                  and p1 = {current_p}."
            )
            break

        p_next = current_p - (func(current_p) * (current_p - current_p_minus_1)
                              ) / (func(current_p) - func(current_p_minus_1))

        error = abs(p_next - current_p)
        iterations.append((i, round(p_next, decimal_places), round(func(p_next), decimal_places),
                           round(error, decimal_places)))

        if error < tolerance:
            print(f"Converged to root: {p_next} after {i} iterations.")
            break

        current_p_minus_1 = current_p
        current_p = p_next
    else:
        print("Maximum iterations reached without convergence.")

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Iteration (n)", "$p_n$", "$f(p_n)$",
                        "Error $|p_n - p_{n-1}|$"])
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
        return x**3 - 3 * x**2 + 2 * x - 0.1

    P0 = 0.5
    P1 = 1.5

    TOLERANCE = 1e-3

    secant_method(f, P0, P1, TOLERANCE)
