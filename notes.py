notes = []

while True:
    print("=== Guestbook Menu ===")
    print("1) Add a note")
    print("2) List all notes")
    print("3) Edit a note")
    print("4) Delete a note")
    print("5) Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")
        notes.append(note)
        print(f"Note '{note}' added.")
c
    elif choice == "2":
        print("=== All Guestbook Entries ===")
        if len(notes) == 0:
            print("No entries found.")
        else:
            for index, note in enumerate(notes):
                print(f"{index+1}) {note}")

    elif choice == "3":
        index = int(input("Enter the index of the note to edit: "))
        if index > len(notes):
            print("Invalid index.")
        else:
            new_note = input("Enter the new note: ")
            notes[index - 1] = new_note
            print(f"Note {index} edited to '{new_note}'.")

    elif choice == "4":
        index = int(input("Enter the index of the note to delete: "))
        if index > len(notes):
            print("Invalid index.")
        else:
            deleted_note = notes.pop(index - 1)
            print(f"Note {index} '{deleted_note}' deleted.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
