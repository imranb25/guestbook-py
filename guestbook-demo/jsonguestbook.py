import sys
import json

notes = []

if len(sys.argv) > 1:
    if sys.argv[1] == 'new':
        if len(sys.argv) > 2:
            note = ' '.join(sys.argv[2:])
            notes.append(note)
            print(f"Note '{note}' added.")
    elif sys.argv[1] == 'list':
        if len(notes) == 0:
            print("No entries found.")
        else:
            for index, note in enumerate(notes):
                print(f"{index+1}) {note}")
    elif sys.argv[1] == 'edit':
        if len(sys.argv) > 3:
            index = int(sys.argv[2])
            if index > 0 and index <= len(notes):
                new_note = ' '.join(sys.argv[3:])
                notes[index-1] = new_note
                print(f"Note {index} edited to '{new_note}'.")
    elif sys.argv[1] == 'delete':
        if len(sys.argv) > 2:
            index = int(sys.argv[2])
            if index > 0 and index <= len(notes):
                deleted_note = notes.pop(index-1)
                print(f"Note {index} '{deleted_note}' deleted.")
    elif sys.argv[1] == 'export':
        if len(notes) == 0:
            print("No entries found.")
        else:
            json_data = json.dumps(notes)
            print(json_data)
