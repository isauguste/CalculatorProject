'''My Calculator Test Suite'''

import pytest
from calculator import Calculator, Calculations
from faker import Faker

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

fake = Faker()

def test_fake_addition():
    '''Test Calculator.add using random fake data'''
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    expected = a + b
    result = Calculator.add(a, b)
    assert result == expected

def test_fake_subtraction():
    '''Test Calculator.subtract using random fake data'''
    a = fake.random_int(min=50, max=100)
    b = fake.random_int(min=1, max=49)
    expected = a - b
    result = Calculator.subtract(a, b)
    assert result == expected

def test_fake_multiplication():
    '''Test Calculator.multiply using random fake data'''
    a = fake.random_int(min=1, max=20)
    b = fake.random_int(min=1, max=10)
    expected = a * b
    result = Calculator.multiply(a, b)
    assert result == expected

def test_fake_division():
    '''Test Calculator.divide using random fake data (avoid zero)'''
    a = fake.random_int(min=10, max=100)
    b = fake.random_int(min=1, max=10)  # Avoid divide-by-zero
    expected = a / b
    result = Calculator.divide(a, b)
    assert result == expected
