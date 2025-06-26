from ..calculator import Calculator

class AddCommand:
    name = "add"

    @staticmethod
    def execute(a, b):
        return Calculator.add(a, b)

