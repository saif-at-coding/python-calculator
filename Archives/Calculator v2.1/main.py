import operations
import utils
from utils import menu
from utils import history

print("Welcome to Calculator v2.0")
print(menu)

while True:
    try:
        choice = (
            input(
                "\nEnter 'M', '1' or 'H' for Help/Menu.\nChoose an operation (1-22 or Symbols)\n>> "
            )
            .replace(" ", "")
            .upper()
        )

        if choice in ["5", "6", "7", "8", "+", "-", "*", "/"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice in ["5", "+"]:
                result = f"{num1} + {num2} = {operations.add(num1, num2)}"
            elif choice in ["6", "-"]:
                result = f"{num1} - {num2} = {operations.subtract(num1, num2)}"
            elif choice in ["7", "*"]:
                result = f"{num1} * {num2} = {operations.multiply(num1, num2)}"
            else:
                try:
                    result = f"{num1} / {num2} = {operations.divide(num1, num2)}"
                except ZeroDivisionError as e:
                    print(e)
                    result = ""
            utils.add_to_history(result)
            print(result)

        elif choice in ["9", "10", "11", "12", "15", "SQ", "CB", "ROOT", "CBRT", "ABS"]:
            num = float(input("Enter the number: "))
            if choice in ["9", "SQ"]:
                result = f"{num} ** 2 = {operations.square(num)}"
            elif choice in ["10", "CB"]:
                result = f"{num} ** 3 = {operations.cube(num)}"
            elif choice in ["11", "ROOT"]:
                result = f"Square Root of {num} = {operations.root(num)}"
            elif choice in ["12", "CBRT"]:
                result = f"Cube root of {num} = {operations.cube_root(num)}"
            else:
                result = f"|{num}| = {operations.absolute(num)}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["13", "P"]:
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = f"{base} ** {exponent} = {operations.power(base, exponent)}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["14", "%"]:
            base = float(input("Enter original base value: "))
            value = float(input("Enter new value: "))
            result = f"{value} is {operations.percentage(value, base)}% of {base}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["16", "RAND"]:
            minimum = int(input("Enter the minimum integer range: "))
            maximum = int(input("Enter the maximum integer range: "))
            result = f"Random Integer: {operations.random_int_gen(minimum, maximum)}"
            utils.add_to_history(result)
            print(result)

        elif choice in ["3", "RH"]:
            print("Recent history: ")
            print(utils.show_recent())
            if not history:
                print("No calculations yet, User!")

        elif choice in ["4", "FH"]:
            print(utils.show_history())
            if not history:
                print(f"No calculations yet, User!")
            else:
                print(f"Total calculations: {len(history)}")

        elif choice in ["1", "M", "H"]:
            print(menu)

        elif choice in ["2", "Q"]:
            final_choice = (
                input("Are you sure to quit, User? (Y/N)\n>> ").replace(" ", "").upper()
            )
            if final_choice in ["Y", "YES", "Q"]:
                print("Calculator closed by User.")
                break

        elif choice in ["17", "18", "19", "SIN", "COS", "TAN"]:
            angle = float(input("Enter the angle (in degrees): "))
            if choice in ["17", "SIN"]:
                result = f"sin({angle}\N{DEGREE SIGN}) = {operations.sin_deg(angle)}"
            elif choice in ["18", "COS"]:
                result = f"cos({angle}\N{DEGREE SIGN}) = {operations.cos_deg(angle)}"
            else:
                try:
                    result = (
                        f"tan({angle}\N{DEGREE SIGN}) = {operations.tan_deg(angle)}"
                    )
                except ValueError as e:
                    print(e)
                    result = ""
            utils.add_to_history(result)
            print(result)

        elif choice in ["20", "21", "22", "ASIN", "ACOS", "ATAN"]:
            ratio = float(input("Enter the ratio (value): "))
            if choice in ["20", "ASIN"]:
                try:
                    result = (
                        f"arcsin({ratio}) = {operations.asin_deg(ratio)}\N{DEGREE SIGN}"
                    )
                except ValueError as e:
                    print(e)
                    result = ""
            elif choice in ["21", "ACOS"]:
                try:
                    result = (
                        f"arccos({ratio}) = {operations.acos_deg(ratio)}\N{DEGREE SIGN}"
                    )
                except ValueError as e:
                    print(e)
                    result = ""
            else:
                result = (
                    f"arctan({ratio}) = {operations.atan_deg(ratio)}\N{DEGREE SIGN}"
                )

        else:
            print("Did you mean something else, User?")

    except ValueError:
        print(f"Invalid input, User!")
    except KeyboardInterrupt:
        print(f"Calculator closed by user.")
        break
