import struct

# Function to convert binary to float (double precision)
def binary_to_double(binary_string):
    int_representation = int(binary_string, 2)
    double_representation = struct.unpack('!d', struct.pack('!Q', int_representation))[0]
    return double_representation

# Function to format to 5 decimal places
def format_to_five_decimal(value):
    return round(value, 5)

# Function for 3-digit chopping arithmetic
def three_digit_chopping(value):
    str_value = f"{value:.10f}"
    chopped_value = str_value[:4] if value >= 1 else str_value[:5]
    return float(chopped_value)

# Function for 3-digit rounding arithmetic
def three_digit_rounding(value):
    return round(value, 3)

# Binary string from question
binary_string = "010000000111111010111001"

# 1) Double precision value
exact_value = binary_to_double(binary_string)
exact_value_rounded = format_to_five_decimal(exact_value)

# 2) Three-digit chopping arithmetic
three_digit_chop = three_digit_chopping(exact_value)

# 3) Three-digit rounding arithmetic
three_digit_round = three_digit_rounding(exact_value)

# 4) Errors
absolute_error_rounding = abs(exact_value - three_digit_round)
relative_error_rounding = absolute_error_rounding / abs(exact_value)

results = {
    "Exact Value (Rounded)": exact_value_rounded,
    "Three-Digit Chopping": three_digit_chop,
    "Three-Digit Rounding": three_digit_round,
    "Absolute Error (Rounding)": absolute_error_rounding,
    "Relative Error (Rounding)": relative_error_rounding
}


# Function to compute the number of terms needed for the series to achieve the desired error threshold
def compute_minimum_terms(error_threshold=1e-4, x=1):
    k = 1
    term = abs((-1) ** k * (x ** k) / (k ** 3))
    while term >= error_threshold:
        k += 1
        term = abs((-1) ** k * (x ** k) / (k ** 3))
    return k

# Error threshold
error_threshold = 1e-4

# Compute minimum terms for f(1)
minimum_terms = compute_minimum_terms(error_threshold)
minimum_terms


import math

# Define the function and its derivative for Newton-Raphson
def f(x):
    return x**3 + 4*x**2 - 10

def f_prime(x):
    return 3*x**2 + 8*x

# Bisection method
def bisection_method(a, b, tolerance):
    iterations = 0
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if f(c) == 0:  # Exact root found
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return iterations

# Newton-Raphson method
def newton_raphson_method(x0, tolerance):
    iterations = 0
    while abs(f(x0)) > tolerance:
        x0 = x0 - f(x0) / f_prime(x0)
        iterations += 1
    return iterations

# Define the interval and tolerance
a, b = -4, 7
tolerance = 1e-4

# Initial guess for Newton-Raphson (midpoint of interval)
x0 = (a + b) / 2

# Calculate iterations for both methods
bisection_iterations = bisection_method(a, b, tolerance)
newton_raphson_iterations = newton_raphson_method(x0, tolerance)

bisection_iterations, newton_raphson_iterations

