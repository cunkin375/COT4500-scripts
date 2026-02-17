import pandas as pd
import numpy as np

def fixed_point_iteration_with_error(g, p0, tol=1e-4, max_iter=100):
    iterations = []
    p_prev = p0
    # For n=0, error is not defined relative to a previous step
    iterations.append({'n': 0, 'p': p_prev, 'error': None})
    
    for n in range(1, max_iter + 1):
        p_curr = g(p_prev)
        error = abs(p_curr - p_prev)
        iterations.append({'n': n, 'p': p_curr, 'error': error})
        
        if error < tol:
            break
        p_prev = p_curr
    
    return pd.DataFrame(iterations)

# Define g(p) = cos(p)
g = lambda p: np.cos(p)
p0 = 0.5
tol = 1e-4

df_with_error = fixed_point_iteration_with_error(g, p0, tol)
df_with_error.to_csv('fixed_point_iterations_with_error.csv', index=False)

print(df_with_error)
