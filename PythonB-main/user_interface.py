# user_interface.py
from file_operations import add_text_to_file, edit_text_in_file, delete_text_from_file, view_file_contents

def show_menu():
    """Отображает меню действий для пользователя"""
    print("\n1. Добавить текст")
    print("2. Редактировать текст")
    print("3. Удалить текст")
    print("4. Просмотреть содержимое")
    print("5. Выход")

def get_user_choice():
    """Получает выбор пользователя"""
    return input("\nВыберите действие: ")

def handle_user_choice(action):
    """Обрабатывает выбор пользователя"""
    if action == "1":
        text = input("Введите текст для добавления: ")
        add_text_to_file(text)
    elif action == "2":
        old_text = input("Введите текст, который хотите заменить: ")
        new_text = input("Введите новый текст: ")
        edit_text_in_file(old_text, new_text)
    elif action == "3":
        text_to_delete = input("Введите текст для удаления: ")
        delete_text_from_file(text_to_delete)
    elif action == "4":
        view_file_contents()
    elif action == "5":
        return False  # Выход
    else:
        print("Неверный выбор. Пожалуйста, выберите правильное действие.")
    return True
