def binary_to_double(binary):
    sign = int(binary[0])
    exponent = int(binary[1:12], 2) - 1023
    mantissa_binary = binary[12:]

    mantissa = 1.0
    for i, bit in enumerate(mantissa_binary):
        mantissa += int(bit) * (2 ** -(i + 1))

    value = ((-1) ** sign) * (mantissa * (2 ** exponent))
    return value

def chop(value, digits):
    v = value
    i = 0
    while v > 1:
        v /= 10
        i+=1
    chopped = int(v * 10**digits) / 10**digits
    return chopped * 10**i

def round_arithmetic(value, digits):
    v = value
    i = 0
    while v > 1:
        v /= 10
        i+=1
    rounded = round(v, digits)
    return rounded * 10**i

def compute_errors(exact, approx):
    absolute_error = abs(exact - approx)
    relative_error = absolute_error / abs(exact) if exact != 0 else absolute_error
    return absolute_error, relative_error

binary_input = "010000000111111010111001"

result_double = binary_to_double(binary_input + "0" * (52 - len(binary_input) + 1))
print(f"\nDouble Precision: {result_double:.5f}\n")

result_chop = chop(result_double, 3)
print(f"Three-Digit Chopping: {result_chop:.5f}\n")

result_round = round_arithmetic(result_double, 3)
print(f"Three-Digit Rounding: {result_round:.5f}\n")

absolute_error, relative_error = compute_errors(result_double, result_round)
print(f"Absolute Error (3-Digit Rounding): {absolute_error:.5e}\n")
print(f"Relative Error (3-Digit Rounding): {relative_error:.5e}\n")


def compute_min_terms(error_threshold):
    n = 1
    while True:
        term = 1 / ((n + 1) ** 3)
        if term < error_threshold:
            break
        n += 1
    return n

error_threshold = 1e-4

min_terms = compute_min_terms(error_threshold)
print(f"Minimum Number of Terms: {min_terms}\n")

def func(x):
    return x**3 + 4*x**2 - 10
def bisection_method(a, b, error_threshold):
    left = a
    right = b
    iter = 0
    max = 1000
    while (abs(right - left) > error_threshold and iter < max):
        iter += 1
        p = (left + right) / 2
        if ((func(left) < 0 and func(p) < 0) or (func(left) > 0 and func(p) > 0)):
            left = p
        else:
            right = p

    return iter

error_threshold = 1e-4
a = -4 
b = 7
iterations = bisection_method(a, b, error_threshold)
print(f"Iterations for Bisection: {iterations}\n")

def func_prime(x):
    return 3*x**2 + 8*x
def newtons(a, b, error_threshold):
    p = func((a+b)/2)
    iter = 0
    max = 1000
    while (iter < max):
        iter += 1
        p = p - func(p) / func_prime(p)
        if (abs(func(p)) < error_threshold):
            break
    return iter

error_threshold = 1e-4
a = -4
b = 7
iterations = newtons(a, b, error_threshold)
print(f"Iterations for Newton-Raphson: {iterations}\n")
        
