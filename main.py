import os
import importlib
import pkgutil
import calculator.commands as commands

def load_commands():
    command_dict = {}
    package_dir = os.path.dirname(commands.__file__)

    for (_, name, ispkg) in pkgutil.iter_modules([package_dir]):
        module = importlib.import_module(f"calculator.commands.{name}")
        class_name = name.capitalize() + "Command"
        command_class = getattr(module, class_name)
        command_dict[command_class.name] = command_class

    return command_dict

def main():
    commands_dict = load_commands()

    print("Welcome to the Command Calculator!")
    print("Type 'menu' to see available commands or 'exit' to quit.")

    while True:
        user_input = input(">>> ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "menu":
            print("Available commands:", ", ".join(commands_dict.keys()))
        elif user_input in commands_dict:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = commands_dict[user_input].execute(a, b)
                print("Result:", result)
            except Exception as e:
                print("Error:", e)
        else:
            print("Invalid command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    main()

