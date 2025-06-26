from ..calculator import Calculator

class MultiplyCommand:
    name = "multiply"

    @staticmethod
    def execute(a, b):
        return Calculator.multiply(a, b)

