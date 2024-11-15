import pymongo
import bson

client = pymongo.MongoClient("Your_database_url", tlsAllowInvalidCertificates=True)

note_db = client["NoteApp"]
note_collection = note_db["notes"]

def show_all_notes():
    print("\n")
    print("*" * 50)
    for row in note_collection.find():
        print(f"{row['_id']} - {row['title']} - {row['desc']}")
    print("\n")
    print("*" * 50)

def add_note():
    title = input("Enter the title of Note: ")
    desc = input("Enter the Description of note: ")
    note_collection.insert_one({'title': title, 'desc': desc})
    print("Note Insert Successfully")

def update_note():
    show_all_notes()
    id = input("Enter the Id of Note to Update: ")
    title = input("Enter the title of Note")
    desc = input("Enter the Description of Note: ")
    note_collection.update_one({'_id': bson.ObjectId(id)}, {'$set':{'title': title, 'desc': desc}})
    print("Note update succesfully")

def delete_note():
    show_all_notes()
    id = input("Enter the Id of Note to delete: ")
    note_collection.delete_one({'_id': bson.ObjectId(id)})
    print("Note Delete Successfully")


def main():
    print("Note App Using MongoDb\n")
    while True:
        print("1. Show all Notes")
        print("2. Add Note")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit App")
        choice = input("Enter Numbe from 1...5: ")
        if choice == '1':
            show_all_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
            

if __name__ == "__main__":
    main()
