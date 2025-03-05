NOTES_FILE = 'notes.txt'

def read_notes():
    try:
        with open(NOTES_FILE, 'r', encoding='utf-8') as file:
            return file.read().strip().split('---\n')
    except FileNotFoundError:
        return []

def write_notes(notes):
    with open(NOTES_FILE, 'w', encoding='utf-8') as file:
        file.write('\n---\n'.join(notes) + '\n' if notes else '')

def append_note(note):
    with open(NOTES_FILE, 'a', encoding='utf-8') as file:
        file.write(note + '\n---\n')
