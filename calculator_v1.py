def calculator():

    menu = """\nAvailable Operations: 
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Square (SQ)
    6. Cube (CB)
    7. Square Root (SQRT)
    8. Cube Root (CBRT)
    9. Exit Calculator (Q)
    10. View History (H)"""
    print(menu)

    history = []

    while True:
        try:
            choice = input(
                "\nYou can enter 'help' or 'M' for menu.\nChoose Operation (1-10 or symbols): "
            ).upper()

            if choice in ["1", "+", "2", "-", "3", "*", "4", "/"]:
                num1 = float(input("\nEnter the first number: "))
                num2 = float(input("Enter the second number: "))

                try:
                    if choice in ["1", "+"]:
                        calculation = f"{num1} + {num2} = {num1 + num2}"
                    elif choice in ["2", "-"]:
                        calculation = f"{num1} - {num2} = {num1 - num2}"
                    elif choice in ["3", "*"]:
                        calculation = f"{num1} * {num2} = {num1 * num2}"
                    elif choice in ["4", "/"]:
                        calculation = f"{num1}/{num2} = {num1/num2}"

                    print(f"\n{calculation}")
                    history.append(calculation)
                    history_count += 1

                except ZeroDivisionError:
                    print("Division by Zero is not allowed, User!")

            elif choice in ["5", "SQ", "6", "CB", "7", "SQRT", "8", "CBRT"]:
                num = float(input("\nEnter the number: "))

                if choice in ["5", "SQ"]:
                    calculation = f"{num} ^2 = {num ** 2}"
                elif choice in ["6", "CB"]:
                    calculation = f"{num} ^3 = {num ** 3}"
                elif choice in ["7", "SQRT"]:
                    if num < 0:
                        print("Square Root of Negatives not allowed, User!")
                        continue
                    else:
                        calculation = f"Square root of {num} is {num ** 0.5}"
                elif choice in ["8", "CBRT"]:
                    if num >= 0:
                        calculation = f"Cube root of {num} = {num ** (1/3)}"
                    else:
                        num_positive = abs(num)
                        cube_root = num_positive ** (1 / 3)
                        calculation = f"Cube root of {num} = {-abs(cube_root)}"

                print(f"\n{calculation}")
                history.append(calculation)
                history_count += 1

            elif choice in ["9", "Q"]:
                print("\nCalculator closed by User.")
                break

            elif choice in ["HELP", "M"]:
                print(menu)

            elif choice in ["10", "H"]:
                print("\nCalculator History Below: ")
                for entry in history:
                    print(entry)
                if history:
                    print(f"Total calculations: {len(history)}")
                else:
                    print(f"No calculations yet, User!")

            else:
                print("\nInvalid input, User!")

        except ValueError:
            print("\nInvalid input, User!")
        except TypeError:
            print("Invalid input, User!")
        except KeyboardInterrupt:
            print("\nCalculator closed by User.")
            break


calculator()
