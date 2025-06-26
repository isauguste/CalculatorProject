from ..calculator import Calculator

class SubtractCommand:
    name = "subtract"

    @staticmethod
    def execute(a, b):
        return Calculator.subtract(a, b)

