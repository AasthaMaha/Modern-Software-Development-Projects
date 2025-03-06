def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")   #fixed division by zero
    return round(a / b, 2)

def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")   #fixed non string input handling
    revert_s = s[::-1]
    return ''.join([char.swapcase() for char in revert_s])

def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not found' if out of range."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")   #handling non list input
    if index < -len(lst) or index >= len(lst):   #allowing valid negative indexing
        raise IndexError("Index out of range.")
    return lst[index]   #it now allows negative indexing while correctly raising an error

