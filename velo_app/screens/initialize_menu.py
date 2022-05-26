def show_menu():
    message = """Saved data has been found, what do you want to do?\n
    1. Load data
    2. Start fresh"""
    print(message)

def get_user_choice() -> str:
    show_menu()

    user_input = input("Give the number of your choice >>> ")
    return user_input