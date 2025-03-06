# file_operations.py

def add_text_to_file(text):
    """Добавляет текст в файл"""
    with open("example.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print("Текст добавлен в файл.")

def edit_text_in_file(old_text, new_text):
    """Редактирует текст в файле (заменяет старый текст на новый)"""
    with open("example.txt", "r+", encoding="utf-8") as file:
        content = file.read()
        if old_text in content:
            content = content.replace(old_text, new_text)
            file.seek(0)
            file.write(content)
            file.truncate()
            print(f"Текст '{old_text}' был заменен на '{new_text}'.")
        else:
            print(f"Текст '{old_text}' не найден в файле.")

def delete_text_from_file(text):
    """Удаляет текст из файла"""
    with open("example.txt", "r+", encoding="utf-8") as file:
        content = file.read()
        if text in content:
            content = content.replace(text, "")
            file.seek(0)
            file.write(content)
            file.truncate()
            print(f"Текст '{text}' был удален из файла.")
        else:
            print(f"Текст '{text}' не найден в файле.")

def view_file_contents():
    """Просматривает содержимое файла"""
    try:
        with open("example.txt", "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print("\nСодержимое файла:")
                print(content)
            else:
                print("Файл пуст.")
    except FileNotFoundError:
        print("Файл не найден.")

