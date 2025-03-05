from notes_manager import NotesManager

def main():
    manager = NotesManager()

    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Просмотреть все заметки")
        print("3. Удалить заметку")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название заметки: ")
            text = input("Введите текст заметки: ")
            manager.add_note(title, text)
        elif choice == '2':
            manager.show_notes()
        elif choice == '3':
            title = input("Введите название заметки для удаления: ")
            manager.delete_note(title)
        elif choice == '4':
            print("Выход...")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

# Просто сразу вызываем main() без дополнительных условий
print("Запуск программы 'Заметки'")
main()
