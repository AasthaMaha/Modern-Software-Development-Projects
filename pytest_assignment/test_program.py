import unittest
import pytest
from program import divide_numbers, reverse_string, get_list_element

# Tests for divide_numbers()
def test_divide_numbers_normal():
    assert divide_numbers(10, 2) == 5 #normal case

def test_divide_numbers_edge():
    assert divide_numbers(7,3) == 2.33 #edge case: rounding

def test_divide_number_corner():
    with pytest.raises(ZeroDivisionError): #corner case: expecting failure here
        divide_numbers(5,0)


# Tests for reverse_string()

def test_reverse_string_normal():
    assert reverse_string("Hello") == "OLLEh" #normal case

def test_reverse_string_edge():
    assert reverse_string("") == "" #edge case: empty string here

def test_reverse_string_corner():
    with pytest.raises(TypeError):
        reverse_string(123) #corner case: non string input


# Tests for get_list_element()

def test_get_list_element_normal():
    assert get_list_element([1, 2, 3], 1) == 2 #normal case

def test_get_list_element_edge():
    assert get_list_element([1,2,3], -1) == 3 #edge case: negative index

def test_get_list_element_corner():
    with pytest.raises(IndexError):
        get_list_element([1,2,3], 5) #corner case: out of bounds