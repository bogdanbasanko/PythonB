import file_handler

class NotesManager:
    def __init__(self):
        self.notes = file_handler.read_notes()

    def add_note(self, title, text):
        note = f"Название: {title}\nТекст: {text}"
        self.notes.append(note)
        file_handler.append_note(note)
        print("Заметка добавлена!")

    def show_notes(self):
        if not self.notes or (len(self.notes) == 1 and self.notes[0].strip() == ""):
            print("Заметок пока нет.")
            return

        for note in self.notes:
            print(note)
            print("---")

    def delete_note(self, title):
        updated_notes = []
        found = False

        for note in self.notes:
            if note.startswith(f"Название: {title}\n"):
                found = True
                continue
            updated_notes.append(note)

        if found:
            self.notes = updated_notes
            file_handler.write_notes(updated_notes)
            print(f"Заметка '{title}' удалена.")
        else:
            print(f"Заметка '{title}' не найдена.")
