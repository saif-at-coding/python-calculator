import math
from random import randint


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError(f"Division by zero not allowed, User!")
    return x / y


def square(x: float) -> float:
    return x**2


def cube(x: float) -> float:
    return x**3


def root(x: float) -> float:
    if x < 0:
        raise ValueError(f"Square root of negatives is imaginary, User!")
    return math.sqrt(x)


def cube_root(x: float) -> float:
    return math.cbrt(x)


def power(x: float, exponent: float) -> float:
    if x == 0 and exponent < 0:
        raise ZeroDivisionError(f"Cannot power zero by negatives, User!")
    if x < 0 and not exponent.is_integer():
        raise ValueError(f"{x} ** {exponent} is imaginary, User!")
    return (x) ** exponent


def percentage(x: float, base: float) -> float:
    if base == 0:
        raise ZeroDivisionError(f"Division by zero not allowed, User!")
    return (x / base) * 100


def absolute(x: float) -> float:
    return abs(x)


def random_int_gen(x: int, y: int) -> int:  # generating random integer
    if x > y:
        raise ValueError(f"Maximum cannot be less than minimum, User!")
    return randint(x, y)


def sin_deg(x: float) -> float:
    x = math.radians(x)
    value = math.sin(x)
    if math.isclose(value, 0.0, abs_tol=1e-12):
        return 0.0
    elif math.isclose(value, 1.0, abs_tol=1e-12):
        return 1.0
    elif math.isclose(value, -1.0, abs_tol=1e-12):
        return -1.0
    else:
        return value


def cos_deg(x: float) -> float:
    x = math.radians(x)
    value = math.cos(x)
    if math.isclose(value, 0.0, abs_tol=1e-12):
        return 0.0
    elif math.isclose(value, 1.0, abs_tol=1e-12):
        return 1.0
    elif math.isclose(value, -1.0, abs_tol=1e-12):
        return -1.0
    else:
        return value


def tan_deg(x: float) -> float:
    if math.isclose((x % 180.0), 90.0, abs_tol=1e-12):
        raise ValueError(f"tan({x}) is Undefined, User!")
    x = math.radians(x)
    return math.tan(x)


def asin_deg(x: float) -> float:
    if x < -1 or x > 1:
        raise ValueError(f"Input must be between -1 and 1, User!")
    x = math.asin(x)
    return math.degrees(x)


def acos_deg(x: float) -> float:
    if x < -1 or x > 1:
        raise ValueError(f"Input must be between -1 and 1, User!")
    x = math.acos(x)
    return math.degrees(x)


def atan_deg(x: float) -> float:
    x = math.atan(x)
    return math.degrees(x)


def logn(x: float) -> float:
    if x <= 0:
        raise ValueError(f"Logarithm is only defined for positive numbers, User!")
    return math.log(x)


def log10(x: float) -> float:
    if x <= 0:
        raise ValueError(f"Logarithm is only defined for positive numbers, User!")
    return math.log10(x)


def log2(x: float) -> float:
    if x <= 0:
        raise ValueError(f"Logarithm is only defined for positive numbers, User!")
    return math.log2(x)


def log(x: float, base: float) -> float:
    if x <= 0:
        raise ValueError(f"Logarithm is only defined for positive numbers, User!")
    if not (base > 0 and base != 1):
        raise ValueError(f"Base must be positive and not equal to 1, User!")
    return math.log(x, base)
