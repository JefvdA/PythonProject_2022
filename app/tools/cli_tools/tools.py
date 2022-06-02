import os


def clear():
    command = 'clear' # If Machine is running on Unix, use clear
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def wait_for_enter():
    input("Press enter to continue...")
    clear()

def get_user_input(message: str):
    return input(f"{message} >>>")