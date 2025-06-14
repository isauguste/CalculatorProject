class Calculation:
    '''Performs a single calculation using instance methods'''

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self) -> float:
        return self.a + self.b

    def subtract(self) -> float:
        return self.a - self.b

    def multiply(self) -> float:
        return self.a * self.b

    def divide(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a / self.b


class Calculations:
    '''Handles calculation history using class methods'''
    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_history(cls) -> list:
        return cls.history


class Calculator:
    '''Uses static methods to call instance methods on Calculation and store history'''

    @staticmethod
    def add(a: float, b: float) -> float:
        calc = Calculation(a, b)
        result = calc.add()
        Calculations.add_calculation(calc)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        calc = Calculation(a, b)
        result = calc.subtract()
        Calculations.add_calculation(calc)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        calc = Calculation(a, b)
        result = calc.multiply()
        Calculations.add_calculation(calc)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        calc = Calculation(a, b)
        result = calc.divide()
        Calculations.add_calculation(calc)
        return result

