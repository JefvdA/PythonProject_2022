class Menu:
    def __init__(self, options: list[str]) -> None:
        message = "What do you want to do?\n"
        for i in range(len(options)):
            message += f'{str(i+1)}. {options[i]}\n'
        message += "Give the number of your choice:"

        self.message = message

    def show_menu(self):
        print(self.message)

    def get_user_input(self) -> str:
        self.show_menu()

        user_input = input(">>> ")
        return user_input