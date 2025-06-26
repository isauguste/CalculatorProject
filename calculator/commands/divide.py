from ..calculator import Calculator

class DivideCommand:
    name = "divide"

    @staticmethod
    def execute(a, b):
        return Calculator.divide(a, b)

