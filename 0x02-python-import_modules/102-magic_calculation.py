#!/usr/bin/python3

def magic_calculation(a, b):
    """Bytecodefor Maths presented by Alx to work on it."""
    from magic_calculation_102 import add, sub

    result = add(a, b) if a < b else sub(a, b)

    if a < b:
        for i in range(4, 6):
            result = add(result, i)

    return result
