history = []
HISTORY = f""
menu = """
Available Operations:

1.  Main menu/Help (M/H) 2. Quit (Q)                 
3.  Last 5 Entries (rH)  4. Full History (fH)
5.  Addition (+)         6. Subtraction (-)          7. Multiplication (*)   
8.  Division (/)         9. Square (SQ)             10. Cube (CB)
11. Root (ROOT)         12. Cube Root (CBRT)        13. Power (P)            
14. Percentage (%)      15. Absolute (ABS)          16. Random Integer (RAND)       
17. Sine (SIN)          18. Cosine (COS)            19. Tangent (TAN)          
20. arcSine (aSIN)      21. arcCosine (aCOS)        22. arcTangent (aTAN)
23. Lorgarithm with any base (LOG)                  24. Logarithm Natural base (LOGN)
25. Base-10 Logarithm (LOG10)                       26. Base-2 Logarithm (LOG2)
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
