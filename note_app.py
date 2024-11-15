import json

file_name = 'note.txt'


def load_notes():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def show_all_notes(notes):
    print("\n")
    print("#"*50)
    for index, note in enumerate(notes, start=1):
        print(f"{index} - {note['title']} : {note['desc']}")
    print("\n")
    print("#"*50)

def add_note(notes):
    title = input("Enter the Note Title: ")
    desc = input("Enter the Note Description: ")
    notes.append({'title': title, 'desc': desc})
    save_note_helper(notes)

def update_note(notes):
    show_all_notes(notes)
    index = int(input("Enter the Note Number: "))
    if 1<= index <= len(notes):
        title = input("Enter the New Note Title: ")
        desc = input("Enter the New Description of Note: ")
        notes[index-1] = {'title': title, 'desc': desc}
        save_note_helper(notes)
    else:
        print("Invalid Note Number - Try again - ")

def delete_note(notes):
    show_all_notes(notes)
    index = int(input("Enter the Note Number to Delete: "))
    if 1 <= index <= len(notes):
        del notes[index-1]
    else:
        print("Invalid for Delete Note ")

def save_note_helper(notes):
    with open(file_name, 'w') as file:
        json.dump(notes, file)
        print("Successfully Operation")


def main():
    print("\n")
    notes = load_notes()
    while True:
        print("1. Show All Notes")
        print("2. Add Note")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit app")
        choice = input("Enter the Number from 1 to 5 -> ")
        match choice:
            case '1':
                show_all_notes(notes)
            case '2':
                add_note(notes)
            case '3':
                update_note(notes)
            case '4':
                delete_note(notes)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()

    

