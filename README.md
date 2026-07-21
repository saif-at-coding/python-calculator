# Python Calculator v2.4

A beginner-friendly command-line calculator written in Python.

## Features

- Arithmetic (+, -, *, /)
- Powers (Square, Cube, Roots, Exponents)
- Percentage
- Absolute Value
- Random Integer Generator
- Trigonometry (sin, cos, tan)
- Inverse Trigonometry (arcsin, arccos, arctan)
- Logarithm (any base, natural base, base-10, base-2)
- Calculation History (Full, Recent)
- Input Validation
- Exception Handling

## Requirements

- Python 3.12+ (Recommended)
- Python 3.6 (minimum)

## Run

python "Calculator v2.4"\main.py

## Test

python "Calculator v2.4"\tests.py

## Project Structure

Calculator v2.4/
- main.py
- operations.py
- utils.py
- commands.py
- tests.py
- WHATS-NEW.md

## Latest Version
Version 2.4

## What's New in v2.4

- Refactored command handling into a separate `commands.py` module.
- Simplified `main.py` by moving operation logic out of it.
- Reworked the history system to use a dedicated `History` class.
- Improved negative-base exponent handling in `power()`.
- Added a comprehensive test suite.

See `tests.py` for all current tests.

## Archive Versions

- version 2.3
- version 2.2
- version 2.1
- version 2.0
- version 1.0

## Author

Md Saifuddin
(saif-at-coding @ Github)

## Future Plans

- Save history to a file
- Scientific functions (currently working on)
- GUI version
- Memory register
