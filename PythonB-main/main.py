# main.py
from user_interface import show_menu, get_user_choice, handle_user_choice

def main():
    """Главная функция, которая управляет взаимодействием с пользователем"""
    while True:
        show_menu()
        action = get_user_choice()
        if not handle_user_choice(action):
            print("Выход из программы.")
            break


program_mode = "main_program"

if program_mode == "main_program":
    main()
