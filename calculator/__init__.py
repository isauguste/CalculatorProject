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


class Calculator:
    '''Uses static methods to call instance methods on Calculation'''

    @staticmethod
    def add(a: float, b: float) -> float:
        return Calculation(a, b).add()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return Calculation(a, b).subtract()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return Calculation(a, b).multiply()

    @staticmethod
    def divide(a: float, b: float) -> float:
        return Calculation(a, b).divide()
