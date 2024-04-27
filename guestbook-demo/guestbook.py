import sys
import json

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file)

def main():
    if len(sys.argv) < 2:
        print("Usage: guestbook.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    notes = load_notes()

    if command == 'new':
        if len(sys.argv) > 2:
            note = ' '.join(sys.argv[2:])
            notes.append(note)
            save_notes(notes)
            print(f"Note '{note}' added.")
    elif command == 'list':
        if len(notes) == 0:
            print("No entries found.")
        else:
            for index, note in enumerate(notes):
                print(f"{index+1}) {note}")
    elif command == 'edit':
        if len(sys.argv) > 3:
            index = int(sys.argv[2])
            if index > 0 and index <= len(notes):
                new_note = ' '.join(sys.argv[3:])
                notes[index-1] = new_note
                save_notes(notes)
                print(f"Note {index} edited to '{new_note}'.")
    elif command == 'delete':
        if len(sys.argv) > 2:
            index = int(sys.argv[2])
            if index > 0 and index <= len(notes):
                deleted_note = notes.pop(index-1)
                save_notes(notes)
                print(f"Note {index} '{deleted_note}' deleted.")

if __name__ == "__main__":
    main()
