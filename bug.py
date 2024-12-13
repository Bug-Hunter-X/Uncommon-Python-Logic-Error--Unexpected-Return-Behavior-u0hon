def function_with_uncommon_error(a, b):
    if a == 0:
        return 1 / a  # ZeroDivisionError, but the real issue is below
    result = a + b
    if result > 10:
        return result * 2 # The return statement is outside the if block but doesn't raise an error but might cause unexpected behavior if that logic is not intended
    return result

print(function_with_uncommon_error(0, 5))