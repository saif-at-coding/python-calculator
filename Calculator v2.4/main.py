from commands import *

handle_menu()
print(f"Choose a command (use shortcuts listed in the menu)")

while True:
    try:
        command = input("> ").replace(" ", "").upper()

        if command in commands:
            commands[command]()
        else:
            print("Incorrect command, User!")

    except KeyboardInterrupt:
        handle_exit()
    except Exception as e:
        print(e)
