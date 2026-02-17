"""
This module implements the bisection method for root finding.
"""
import csv

def bisection_method(func, a, b, tolerance, max_iter=100):
    """
    Implements the Bisection Method to find a root of a function.
    
    Args:
        func: The function for which to find the root.
        a: The lower bound of the interval [a, b].
        b: The upper bound of the interval [a, b].
        tolerance: The error tolerance. The method stops when (b - a) / 2 < tolerance.
        max_iter: The maximum number of iterations.
        
    Returns:
        None (writes to CSV file)
    """
    # Check if a root is bracketed
    if func(a) * func(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return
    iterations = []
    # Header for CSV
    header = ["$n$", "$a_n$", "$b_n$", "$p_n$", "$f(p_n)$", "Error"]
    an = a
    bn = b
    for n in range(1, max_iter + 1):
        # Midpoint
        pn = (an + bn) / 2
        fpn = func(pn)
        # Error bound
        error = (bn - an) / 2
        # Store iteration data
        # n, a_n, b_n, p_n, f(p_n), Error
        iterations.append([n, an, bn, pn, fpn, error])
        # Check convergence
        if error < tolerance or fpn == 0:
            print(f"Converged to root: {pn} after {n} iterations.")
            break
        # Determine new interval
        if func(an) * fpn < 0:
            bn = pn
        else:
            an = pn
    else:
        print("Maximum iterations reached without convergence.")
    # Write to CSV
    with open('bisection_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(iterations)
    print("Results written to bisection_results.csv")

if __name__ == "__main__":
    # Example usage: Find root of f(x) = x^3 + 4x^2 - 10 = 0 in [1, 2]
    # Adjust this function and interval as needed
    def f(x):
        """
        The function to find the root of.

        Args:
            x: The value to evaluate.
        
        Returns: The value of the function at x.
        """
        return x**3 - 3 * x**2 + 2 * x - 0.1
    A_INITIAL = 0.0
    B_INITIAL = 2.0
    TOL = 1e-6
    bisection_method(f, A_INITIAL, B_INITIAL, TOL)
