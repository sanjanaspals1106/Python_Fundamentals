class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_available = True  # Encapsulation

    def borrow(self):
        if self._is_available:
            self._is_available = False
            return f"You borrowed '{self.title}'."
        return f"'{self.title}' is currently not available."

    def return_book(self):
        self._is_available = True
        return f"You returned '{self.title}'."

    def __str__(self):
        status = "Available" if self._is_available else "Not Available"
        return f"{self.title} by {self.author} ({status})"


# Inheritance + Method Overriding
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def borrow(self):
        # Overridden: eBooks are always available
        return f"You downloaded the eBook '{self.title}' ({self.file_size}MB)."

    def __str__(self):
        return f"{self.title} by {self.author} [E-Book: {self.file_size}MB]"
