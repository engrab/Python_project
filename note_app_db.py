import sqlite3

con = sqlite3.connect('note_app.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS note(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            desc TEXT NOT NULL
            )

''')

def show_all_notes():
    cur.execute("SELECT * FROM note")
    for row in cur.fetchall():
        print(row)

def add_note():
    title = input("Enter the Title: ")
    desc = input("Enter the Description: ")
    cur.execute("INSERT INTO note(title, desc) VALUES (?, ?)", (title, desc))
    con.commit()

def update_note():
    show_all_notes()
    id = input("Enter the ID for Update: ")
    title = input("Enter New Title: ")
    desc = input("Enter New Description: ")
    cur.execute("UPDATE note SET title=?, desc = ? WHERE id = ?", (title, desc, id))
    con.commit()

def delete_note():
    show_all_notes()
    id = input("Enter the Note ID for Delete: ")
    cur.execute("DELETE FROM note WHERE id = ?", (id,))
    con.commit()
    

def main():
    print("Note App with DB \n")
    while True:
        print("1. Show all Notes")
        print("2. Add Note")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit app")
        choice = input("Enter Number from 1 to 5: ")
        match choice:
            case '1':
                show_all_notes()
            case '2':
                add_note()
            case '3':
                update_note()
            case '4':
                delete_note()
            case '5':
                break
            case _:
                print("Invalid Choice - TRY AGAIN - ")
    con.close()

if __name__ == "__main__":
    main()
