from book import Book, EBook

class Library:
    def __init__(self):
        self.books = []  # List of book objects

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        print("\n--- Available Books ---")
        for book in self.books:
            if getattr(book, "_is_available", True):
                print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
