import json
from datetime import datetime
import os

FILE = "notes.json"


# ------------------------------
# Load notes from the JSON file
# ------------------------------
def load_notes():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: notes.json is corrupted. Starting with an empty list.")
        return []
    except Exception as e:
        print("Error reading file:", e)
        return []


# ------------------------------
# Save notes back into JSON file
# ------------------------------
def save_notes(notes):
    try:
        with open(FILE, "w") as f:
            json.dump(notes, f, indent=4)
    except Exception as e:
        print("Error saving notes:", e)


# ------------------------------
# Add a new note
# ------------------------------
def add_note():
    notes = load_notes()
    text = input("Enter your note: ").strip()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_id = len(notes) + 1

    new_note = {
        "id": note_id,
        "timestamp": timestamp,
        "note": text
    }

    notes.append(new_note)
    save_notes(notes)
    print("Note added successfully!")


# ------------------------------
# View all notes
# ------------------------------
def view_notes():
    notes = load_notes()

    if not notes:
        print("No notes found.")
        return

    print("\n--- All Notes ---")
    for n in notes:
        print(f"{n['id']}. [{n['timestamp']}] {n['note']}")


# ------------------------------
# Search notes
# ------------------------------
def search_notes():
    notes = load_notes()
    keyword = input("Search for: ").strip().lower()

    results = [n for n in notes if keyword in n["note"].lower()]

    if results:
        print("\n--- Search Results ---")
        for r in results:
            print(f"{r['id']}. [{r['timestamp']}] {r['note']}")
    else:
        print("No matching notes found.")


# ------------------------------
# Clear all notes
# ------------------------------
def clear_notes():
    confirm = input("This will delete ALL notes. Continue? (y/n): ").lower()

    if confirm == "y":
        save_notes([])  # overwrite with empty list
        print("All notes cleared!")
    else:
        print("Cancelled.")


# ------------------------------
# Main menu loop
# ------------------------------
def menu():
    while True:
        print("\n===== NOTES MANAGER =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Clear All Notes")
        print("5. Quit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            clear_notes()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# Run the app
menu()
