'''My Calculator Test Suite'''

import pytest
from calculator import Calculator, Calculations

@pytest.fixture(autouse=True)
def clear_history_before_test():
    '''Clear history before each test'''
    Calculations.clear_history()

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 2, 4),
    (1.5, 2.5, 4.0),
    (-1, 5, 4)
])
def test_addition(num1, num2, expected):
    '''Test addition with multiple inputs'''
    assert Calculator.add(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (5, 2, 3),
    (3, 3, 0),
    (-2, -2, 0)
])
def test_subtraction(num1, num2, expected):
    '''Test subtraction with multiple inputs'''
    assert Calculator.subtract(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 4, 12),
    (-1, 6, -6),
    (0, 10, 0)
])
def test_multiplication(num1, num2, expected):
    '''Test multiplication with multiple inputs'''
    assert Calculator.multiply(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-8, 2, -4)
])
def test_division(num1, num2, expected):
    '''Test division with multiple inputs'''
    assert Calculator.divide(num1, num2) == expected


def test_divide_by_zero():
    '''Test that division by zero raises an error'''
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

def test_history_tracking():
    '''Test that calculation history stores instances correctly'''
    Calculator.add(1, 2)
    Calculator.subtract(4, 1)
    history = Calculations.get_history()
    assert len(history) == 2
    last = Calculations.get_last_calculation()
    assert last.a == 4
    assert last.b == 1
    assert last.subtract() == 3

def test_generated_cases(generated_test_case):
    '''Test calculator operations using dynamically generated Faker data'''
    num1, num2, operation, expected = generated_test_case
    result = getattr(Calculator, operation)(num1, num2)
    assert result == expected
