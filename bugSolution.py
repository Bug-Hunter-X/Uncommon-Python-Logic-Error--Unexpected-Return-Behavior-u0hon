def function_with_uncommon_error_fixed(a, b):
    if a == 0:
        return 0 # Handle division by zero gracefully
    result = a + b
    if result > 10:
        return result * 2
    return result

print(function_with_uncommon_error_fixed(0,5))
print(function_with_uncommon_error_fixed(5, 6))