import sys
from calculator import Calculator

def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py <a> <b> <operation>")
        return

    a_str, b_str, operation = sys.argv[1], sys.argv[2], sys.argv[3]

    # Validate numbers
    try:
        a = float(a_str) if "." in a_str else int(a_str)
        b = float(b_str) if "." in b_str else int(b_str)
    except ValueError:
        print(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
        return

    try:
        if not hasattr(Calculator, operation):
            print(f"Unknown operation: {operation}")
            return

        result = getattr(Calculator, operation)(a, b)
        print(f"The result of {a} {operation} {b} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

