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
    factor = 10 ** digits
    return int(value * factor) / factor

def round_arithmetic(value, digits):
    factor = 10 ** digits
    return int(value * factor + 0.5) / factor

def compute_errors(exact, approx):
    absolute_error = abs(exact - approx)
    relative_error = absolute_error / abs(exact) if exact != 0 else absolute_error
    return absolute_error, relative_error

binary_input = "010000000111111010111001"

result_double = binary_to_double(binary_input + "0" * (52 - len(binary_input) + 1))
print(f"1) Double Precision Result: {result_double:.5f}")

result_chop = chop(result_double, 3)
print(f"2) Three-Digit Chopping Result: {result_chop:.5f}")

result_round = round_arithmetic(result_double, 3)
print(f"3) Three-Digit Rounding Result: {result_round:.5f}")

absolute_error, relative_error = compute_errors(result_double, result_round)
print(f"4) Absolute Error (3-Digit Rounding): {absolute_error:.5e}")
print(f"5) Relative Error (3-Digit Rounding): {relative_error:.5e}")
