#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide two integers and print the result.
    
    Args:
        a (int): The numerator.
        b (int): The denominator.
    
    Returns:
        The result of division, or None if division fails.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
