# 🚀 What's New in Calculator v2.0

Calculator v2.0 is a major upgrade from the original single-file calculator. While the first version focused on implementing basic functionality, this version improves the project structure, adds new features, and introduces better code organization.

---

## ✨ New Features

### 🧮 New Mathematical Operations

The following operations have been added:

- Power (`x^y`)
- Percentage
- Absolute Value
- Random Integer Generator

The calculator now supports a wider range of mathematical operations than the original version.

---

### 📜 Recent History

Besides viewing the complete calculation history, Calculator v2.0 can now display only the most recent calculations for quicker access.

---

### 📁 Multi-file Project Structure

The calculator is no longer a single Python file.

Project structure:

```text
Calculator v2.0/
│
├── main.py          # User interface
├── operations.py    # Mathematical operations
├── utils.py         # Helper functions
└── tests.py         # Automatic unit tests
```

Separating the project into modules makes the code easier to understand, maintain, and expand.

---

## 🛠 Code Improvements

### Separation of Concerns

Responsibilities are now separated:

- `main.py` handles user interaction.
- `operations.py` performs mathematical calculations.
- `utils.py` manages helper functionality.

This makes future updates much easier.

---

### Better Error Handling

Mathematical functions now raise exceptions directly instead of relying entirely on the user interface.

Examples include:

- Division by zero
- Square root of negative numbers
- Invalid powers (negative base with fractional exponent)
- Invalid random number ranges

---

### Improved Code Reusability

Every mathematical operation is implemented as its own reusable function.

This allows:

- Easier maintenance
- Cleaner code
- Unit testing
- Reuse in future projects

---

### Type Hints

Functions now include type hints, improving readability and making the code easier to understand.

Example:

```python
def add(x: float, y: float) -> float:
```

---

## ✅ Automated Testing

Calculator v2.0 introduces automated unit tests.

Current tests cover:

- Addition
- Subtraction
- Multiplication
- Division
- Square
- Cube
- Square Root
- Cube Root
- Power
- Percentage
- Absolute Value
- Random Integer Generator

Edge cases such as division by zero and invalid inputs are also tested.

---

## 📈 Overall Improvements

Compared to Version 1:

- Cleaner project structure
- More mathematical operations
- Modular codebase
- Better error handling
- Reusable functions
- Automated testing support
- Easier future expansion

---

## 🔮 Future Ideas

Possible future improvements include:

- Save history to a file
- Scientific calculator functions
- Memory operations (M+, M-, MR, MC)
- Expression parsing (`2 + 3 * 4`)
- Graphical User Interface (GUI)
- Themes and colored terminal output
- Configuration file for user preferences

---

Thank you for checking out Calculator v2.0!
