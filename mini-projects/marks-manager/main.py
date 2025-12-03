from helpers import (
    add_mark,
    update_mark,
    delete_mark,
    calculate_average,
    highest_mark,
    lowest_mark
)

def main():
    student_marks = {}

    while True:
        print("\n=== Marks Manager ===")
        print("1. Add mark")
        print("2. Update mark")
        print("3. Delete mark")
        print("4. Calculate average")
        print("5. Highest mark")
        print("6. Lowest mark")
        print("7. View all marks")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "1":
            name = input("Enter student name: ")
            mark = float(input("Enter mark: "))
            add_mark(student_marks, name, mark)
            print("Mark added!")

        elif choice == "2":
            name = input("Enter student name: ")
            mark = float(input("Enter new mark: "))
            if update_mark(student_marks, name, mark):
                print("Mark updated!")
            else:
                print("Student not found!")

        elif choice == "3":
            name = input("Enter student name: ")
            if delete_mark(student_marks, name):
                print("Mark deleted!")
            else:
                print("Student not found!")

        elif choice == "4":
            avg = calculate_average(student_marks)
            print(f"Average mark = {avg:.2f}")

        elif choice == "5":
            name, mark = highest_mark(student_marks)
            if name:
                print(f"Highest mark: {name} → {mark}")
            else:
                print("No marks available")

        elif choice == "6":
            name, mark = lowest_mark(student_marks)
            if name:
                print(f"Lowest mark: {name} → {mark}")
            else:
                print("No marks available")

        elif choice == "7":
            print("\n--- All Marks ---")
            for name, mark in student_marks.items():
                print(f"{name}: {mark}")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
