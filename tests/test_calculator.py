'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiplication(): 
    '''Test that multiplication function works '''
    assert multiply(3, 4) == 12

def test_division(): 
    '''Test that division function works '''
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False
