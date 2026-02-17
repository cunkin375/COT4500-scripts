"""
This module implements Newton's method for root finding.
"""
import csv


def newton_method(func, d_func, x0, tolerance, max_iter=50):
    """
    Implements Newton's Method to find a root of a function.

    Args:
        func: The function f(x).
        d_func: The derivative of the function f'(x).
        x0: Initial guess.
        tolerance: Error tolerance.
        max_iter: Maximum number of iterations.
    """
    iterations = []

    xn = x0
    error = None

    print(f"{'n':<5} {'x_n':<20} {'f(x_n)':<20} {'f\'(x_n)':<20} {'Error':<20}")

    for n in range(max_iter):
        fx = func(xn)
        dfx = d_func(xn)

        # Avoid division by zero
        if dfx == 0:
            print("Derivative is zero. Newton's method fails.")
            return None
        x_next = xn - fx / dfx

        # Store iteration data
        # Round to 7 decimal places
        iterations.append((n, round(xn, 7), round(fx, 7),
                            round(dfx, 7), round(error, 7) if error is not None else "N/A"))

        error_str = f"{error:.10f}" if error is not None else "N/A"
        print(f"{n:<5} {xn:<20.10f} {fx:<20.10f} {dfx:<20.10f} {error_str:<20}")

        # Check for convergence
        if abs(x_next - xn) < tolerance:
            print(f"\nConverged to root: {x_next} after {n+1} iterations.")
            break

        error = abs(x_next - xn)
        xn = x_next
    else:
        print("\nMaximum iterations reached without convergence.")

    # Write results to CSV (optional but useful)
    with open('newton_results.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Iteration (n)", "$p_n$", "$f(p_n)$",
                        "$f'(p_n)$", "Error $|p_n - p_{n-1}|$"])
        writer.writerows(iterations)
        print("Results written to newton_results.csv")


if __name__ == "__main__":
    def f(x):
        """
        The function to find the root of.

        Args:
            x: The value to evaluate.

        Returns: The value of the function at x.
        """
        return x**3 - 3 * x**2 + 2 * x - 0.1

    def df(x):
        """
        The derivative of the function to find the root of.

        Args:
            x: The value to evaluate.

        Returns: The value of the derivative of the function at x.
        """
        return 3*x**2 - 6*x + 2

    INITIAL_GUESS = 1.5
    TOLERANCE = 1e-3

    newton_method(f, df, INITIAL_GUESS, TOLERANCE)
