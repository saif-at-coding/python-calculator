history = []
HISTORY = f""
menu = """
Available Operations:

1. Addition (+)         2. Subtraction (-)
3. Multiplication (*)   4. Division (/)
5. Square (SQ)          6. Cube (CB)
7. Root (ROOT)          8. Cube Root (CBRT)
9. Power (P)            10. Percentage (%)
11. Absolute (ABS)      12. Random Integer (RAND)
13. Last 5 Entries (rH) 14. Full History (fH)
15. Main menu (M)       16. Quit (Q)
"""


def show_history():
    global history
    global HISTORY
    for entry in history:
        HISTORY += f"\n{entry}"
    return HISTORY


def add_to_history(entry):
    global history
    history.append(entry)


def show_recent():
    global history
    global HISTORY
    for entry in history[-5:]:
        HISTORY += f"\n{entry}"
    return HISTORY
