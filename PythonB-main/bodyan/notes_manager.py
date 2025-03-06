import file_handler

def read_notes():
    return file_handler.read_notes()

def add_note(title, text, notes):
    note = f"Название: {title}\nТекст: {text}"
    notes.append(note)
    file_handler.append_note(note)
    print("Заметка добавлена!")

def show_notes(notes):
    if not notes or (len(notes) == 1 and notes[0].strip() == ""):
        print("Заметок пока нет.")
        return

    for note in notes:
        print(note)
        print("---")

def delete_note(title, notes):
    updated_notes = []
    found = False

    for note in notes:
        if note.startswith(f"Название: {title}\n"):
            found = True
            continue
        updated_notes.append(note)

    if found:
        notes[:] = updated_notes
        file_handler.write_notes(updated_notes)
        print(f"Заметка '{title}' удалена.")
    else:
        print(f"Заметка '{title}' не найдена.")

# Пример использования
notes = read_notes()

# Добавление новой заметки
add_note("Заметка 1", "Текст заметки 1", notes)

# Показать все заметки
show_notes(notes)

# Удалить заметку
delete_note("Заметка 1", notes)