import operations
import utils

commands = {
    "M": utils.show_menu,
    "H": utils.show_menu,
    "FH": utils.show_history,
    "RH": utils.show_recent,
    "Q": utils.user_exit,
    "+": operations.add,
    "-": operations.subtract,
    "*": operations.multiply,
    "/": operations.divide,
    "SQ": operations.square,
    "CB": operations.cube,
    "ROOT": operations.root,
    "CBRT": operations.cube_root,
    "P": operations.power,
    "%": operations.percentage,
    "ABS": operations.absolute,
    "RAND": operations.random_int_gen,
    "SIN": operations.sin_deg,
    "COS": operations.cos_deg,
    "TAN": operations.tan_deg,
    "ASIN": operations.asin_deg,
    "ACOS": operations.acos_deg,
    "ATAN": operations.atan_deg,
    "LOG": operations.log,
    "LN": operations.logn,
    "LOG10": operations.log10,
    "LOG2": operations.log2,
}

utility_operations = ["M", "H", "FH", "RH", "Q"]
arithemtic_operations = ["+", "-", "*", "/"]
trigonometry_operations = ["SIN", "COS", "TAN"]
inverse_trigonometry_operations = ["ASIN", "ACOS", "ATAN"]
unary_input_operations = ["SQ", "CB", "ROOT", "CBRT", "ABS", "LN", "LOG10", "LOG2"]
# others require misc input messages

utils.show_menu()
print(f"Choose an operation (use shortcuts listed in the menu)")
while True:
    try:
        command = input(f">> ").replace(" ", "").upper()

        if command in utility_operations:
            commands[command]()
        else:
            if command in arithemtic_operations:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = f"{num1} {command} {num2} = {commands[command](num1, num2)}"

            elif command in trigonometry_operations:
                angle = float(input("Enter the angle (in degrees): "))
                result = f"{command.lower()}({angle}\N{DEGREE SIGN}) = {commands[command](angle)}"

            elif command in inverse_trigonometry_operations:
                value = float(input("Enter the value: "))
                result = f"{command.lower()}({value}) = {commands[command](value)}\N{DEGREE SIGN}"

            elif command in unary_input_operations:
                num = float(input("Enter the number: "))
                result = f"{command.lower()} {num} = {commands[command](num)}"

            elif command == "%":
                original = float(input("Enter the original value: "))
                value = float(input("Enter the new value: "))
                result = (
                    f"{value} is {commands[command](value, original)}% of {original}"
                )

            elif command == "P":
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                result = f"{base}^{exponent} = {commands[command](base, exponent)}"

            elif command == "LOG":
                value = float(input("Enter the value: "))
                base = float(input("Enter the log base: "))
                result = f"log_{value}_{base} = {commands[command](value, base)}"

            elif command == "RAND":
                minimum = int(input("Enter the minimum range: "))
                maximum = int(input("Enter the maximum range: "))
                result = f"Random: {commands[command](minimum, maximum)}"

            else:
                print("Invalid input, User!")
                result = ""

            utils.add_to_history(result)
            print(result)

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except NameError as e:
        print(e)
    except KeyboardInterrupt:
        utils.user_exit()
