
def f(x):
    return x**3 - x**2 + 4

def f_prime(x):
    return 3*x**2 - 2*x

x0 = 1
tolerance = 0.001
max_iterations = 100


iterations = 0
while iterations < max_iterations:
    # Compute the next approximation
    x1 = x0 - f(x0) / f_prime(x0)
    
    # Check for convergence
    if abs(x1 - x0) < tolerance:
        break
    
    # Update for next iteration
    x0 = x1
    iterations += 1

# Output the result
print(x1, iterations)
