from library import Library
from book import Book, EBook

library = Library()

library.add_book(Book("Atomic Habits", "James Clear"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(EBook("Python Crash Course", "Eric Matthes", 5))

def menu():
    print("\n===== Library Menu =====")
    print("1. View Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Search a Book")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        library.list_available_books()

    elif choice == "2":
        title = input("Enter book title to borrow: ")
        book = library.search_book(title)
        if book:
            print(book.borrow())
        else:
            print("Book not found.")

    elif choice == "3":
        title = input("Enter book title to return: ")
        book = library.search_book(title)
        if book:
            print(book.return_book())
        else:
            print("Book not found.")

    elif choice == "4":
        title = input("Enter book title to search: ")
        book = library.search_book(title)
        print(book if book else "Book not found.")

    elif choice == "5":
        print("Exiting…")
        break

    else:
        print("Invalid choice!")
