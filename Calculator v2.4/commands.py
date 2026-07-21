from utils import *
from operations import *


def handle_menu():
    show_menu()


def handle_history():
    show_history()


def handle_recent():
    show_recent()


def handle_exit():
    user_exit()


def handle_add():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = f"{num1} + {num2} = {add(num1, num2)}"
    add_to_history(result)
    print(result)


def handle_subtract():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = f"{num1} - {num2} = {subtract(num1, num2)}"
    add_to_history(result)
    print(result)


def handle_multiply():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = f"{num1} * {num2} = {multiply(num1, num2)}"
    add_to_history(result)
    print(result)


def handle_divide():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = f"{num1} / {num2} = {divide(num1, num2)}"
    add_to_history(result)
    print(result)


def handle_square():
    num = float(input("Number: "))
    result = f"{num} ^2 = {square(num)}"
    add_to_history(result)
    print(result)


def handle_cube():
    num = float(input("Number: "))
    result = f"{num} ^3 = {cube(num)}"
    add_to_history(result)
    print(result)


def handle_root():
    num = float(input("Number: "))
    result = f"Root of {num} = {root(num)}"
    add_to_history(result)
    print(result)


def handle_cbrt():
    num = float(input("Number: "))
    result = f"Cube root of {num} = {cube_root(num)}"
    add_to_history(result)
    print(result)


def handle_power():
    base = float(input("Base: "))
    exponent = float(input("Exponent: "))
    result = f"{base} ^{exponent} = {power(base, exponent=exponent)}"
    add_to_history(result)
    print(result)


def handle_percentage():
    base = float(input("Base value: "))
    new_val = float(input("New value: "))
    result = f"{new_val} is {percentage(new_val, base=base)} of {base}"
    add_to_history(result)
    print(result)


def handle_absolute():
    num = float(input("Number: "))
    result = f"|{num}| = {absolute(num)}"
    add_to_history(result)
    print(result)


def handle_rand():
    minimum = int(input("Minimum: "))
    maximum = int(input("Maximum: "))
    result = f"Random: {random_int_gen(minimum, maximum)}"
    add_to_history(result)
    print(result)


def handle_sin():
    angle = float(input("Angle (in degrees): "))
    result = f"sin({angle}\N{DEGREE SIGN}) = {sin_deg(angle)}"
    add_to_history(result)
    print(result)


def handle_cos():
    angle = float(input("Angle (in degrees): "))
    result = f"cos({angle}\N{DEGREE SIGN}) = {cos_deg(angle)}"
    add_to_history(result)
    print(result)


def handle_tan():
    angle = float(input("Angle (in degrees): "))
    result = f"tan({angle}\N{DEGREE SIGN}) = {tan_deg(angle)}"
    add_to_history(result)
    print(result)


def handle_asin():
    value = float(input("Value: "))
    result = f"arcSin({value}) = {asin_deg(value)}\N{DEGREE SIGN}"
    add_to_history(result)
    print(result)


def handle_acos():
    value = float(input("Value: "))
    result = f"arcCos({value}) = {acos_deg(value)}\N{DEGREE SIGN}"
    add_to_history(result)
    print(result)


def handle_atan():
    value = float(input("Value: "))
    result = f"arcTan({value}) = {atan_deg(value)}\N{DEGREE SIGN}"
    add_to_history(result)
    print(result)


def handle_log():
    value = float(input("Value: "))
    base = float(input("Log base: "))
    result = f"log({value}, {base}) = {log(value, base=base)}"
    add_to_history(result)
    print(result)


def handle_logn():
    value = float(input("Value: "))
    result = f"log({value}, e) = {logn(value)}"
    add_to_history(result)
    print(result)


def handle_log10():
    value = float(input("Value: "))
    result = f"log({value}, 10) = {log10(value)}"
    add_to_history(result)
    print(result)


def handle_log2():
    value = float(input("Value: "))
    result = f"log({value}, 2) = {log2(value)}"
    add_to_history(result)
    print(result)


commands = {
    "M": handle_menu,
    "?": handle_menu,
    "Q": handle_exit,
    "H": handle_recent,
    "RH": handle_recent,
    "FH": handle_history,
    "+": handle_add,
    "-": handle_subtract,
    "*": handle_multiply,
    "/": handle_divide,
    "SQ": handle_square,
    "CB": handle_cube,
    "ROOT": handle_root,
    "CBRT": handle_cbrt,
    "P": handle_power,
    "%": handle_percentage,
    "ABS": handle_absolute,
    "RAND": handle_rand,
    "SIN": handle_sin,
    "COS": handle_cos,
    "TAN": handle_tan,
    "ASIN": handle_asin,
    "ACOS": handle_acos,
    "ATAN": handle_atan,
    "LOG": handle_log,
    "LN": handle_logn,
    "LOGN": handle_logn,
    "LOG10": handle_log10,
    "LOG2": handle_log2,
}
