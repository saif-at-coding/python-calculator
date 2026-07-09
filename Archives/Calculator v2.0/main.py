import utils
import operations
from utils import menu
from utils import history

print("Welcome to Calculator v2.0")
print(menu)

while True:
    try:
        choice = (
            input(
                "\nEnter 'M' or '15' for Menu.\nChoose an operation (1-16 or Symbols)\n>> "
            )
            .replace(" ", "")
            .upper()
        )

        if choice in ["1", "2", "3", "4", "+", "-", "*", "/"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice in ["1", "+"]:
                result = f"{num1} + {num2} = {operations.add(num1, num2)}"
            elif choice in ["2", "-"]:
                result = f"{num1} - {num2} = {operations.subtract(num1, num2)}"
            elif choice in ["3", "*"]:
                result = f"{num1} * {num2} = {operations.multiply(num1, num2)}"
            else:
                try:
                    result = f"{num1} / {num2} = {operations.divide(num1, num2)}"
                except ZeroDivisionError as e:
                    print(e)
                    result = ""
            utils.add_to_history(result)
            print(result)

        elif choice in ["5", "6", "7", "8", "11", "SQ", "CB", "ROOT", "CBRT", "ABS"]:
            num = float(input("Enter the number: "))
            if choice in ["5", "SQ"]:
                result = f"{num} ** 2 = {operations.square(num)}"
            elif choice in ["6", "CB"]:
                result = f"{num} ** 3 = {operations.cube(num)}"
            elif choice in ["7", "ROOT"]:
                result = f"Square Root of {num} = {operations.root(num)}"
            elif choice in ["8", "CBRT"]:
                result = f"Cube root of {num} = {operations.cube_root(num)}"
            else:
                result = f"|{num}| = {operations.absolute(num)}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["9", "P"]:
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = f"{base} ** {exponent} = {operations.power(base, exponent)}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["10", "%"]:
            base = float(input("Enter original base value: "))
            value = float(input("Enter new value: "))
            result = f"{value} is {operations.percentage(value, base)}% of {base}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["12", "RAND"]:
            minimum = int(input("Enter the minimum integer range: "))
            maximum = int(input("Enter the maximum integer range: "))
            result = f"Random Integer: {operations.random_int_gen(minimum, maximum)}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["13", "RH"]:
            print("Recent history: ")
            print(utils.show_recent())
            if not history:
                print("No calculations yet, User!")

        elif choice in ["14", "FH"]:
            print(utils.show_history())
            if not history:
                print(f"No calculations yet, User!")
            else:
                print(f"Total calculations: {len(history)}")

        elif choice in ["15", "M"]:
            print(menu)

        elif choice in ["16", "Q"]:
            final_choice = (
                input("Are you sure to quit, User? (Y/N)\n>> ").replace(" ", "").upper()
            )
            if final_choice in ["Y", "YES"]:
                print("Calculator closed by User.")
                break

        else:
            print("Did you mean something else, User?")

    except ValueError:
        print(f"Invalid input, User!")
    except KeyboardInterrupt:
        print(f"Calculator closed by user.")
        break
