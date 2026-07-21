class History:
    history = []


menu = """
Available Operations:

1.  Main menu/Help (M/?) 2. Quit (Q)                 
3.  Last 5 Entries (H/rH)  4. Full History (fH)
5.  Addition (+)         6. Subtraction (-)          7. Multiplication (*)  
8.  Division (/)         9. Square (SQ)             10. Cube (CB)
11. Root (ROOT)         12. Cube Root (CBRT)        13. Power (P)            
14. Percentage (%)      15. Absolute (ABS)          16. Random Integer (RAND)       
17. Sine (SIN)          18. Cosine (COS)            19. Tangent (TAN)          
20. arcSine (aSIN)      21. arcCosine (aCOS)        22. arcTangent (aTAN)
23. Logarithm with any base (LOG)                  24. Logarithm Natural base (LN)
25. Base-10 Logarithm (LOG10)                       26. Base-2 Logarithm (LOG2)

"""


def show_menu():
    print(menu)


def user_exit():
    print("Calculator closed by User.")
    quit()


def show_history():
    for entry in History.history:
        print(entry)
    if History.history:
        print(f"Total calculations: {len(History.history)}")
    else:
        print(f"No calculation yet, User!")


def add_to_history(entry: str) -> None:
    if bool(entry):
        History.history.append(entry)


def show_recent():
    for entry in History.history[-5:]:
        print(entry)
    if not History.history:
        print(f"No calculation yet, User!")
