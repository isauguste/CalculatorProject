'''My Calculator Test Suite'''

import pytest
from calculator import Calculator

def test_addition():
    '''Test that addition function works'''
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert Calculator.subtract(2, 2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert Calculator.multiply(3, 4) == 12

def test_division():
    '''Test that division function works'''
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    '''Test that division by zero raises an error'''
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)
