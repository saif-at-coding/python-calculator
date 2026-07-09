from math import sqrt
from math import cbrt
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
    return sqrt(x)


def cube_root(x: float) -> float:
    return cbrt(x)


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
