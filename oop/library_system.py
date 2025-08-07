class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __def__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"{super().get_details()} [EBook, {self.file_size}MB]"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"{super().get_details()} [Print Book, {self.page_count} pages)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added book: {book}")
        else:
            print("Error: can only add Book objects to the library")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                print(f"- {book.get_details()}")

from library_system import Book, EBook, PrintBook, Library

def main():
    my_library = Library()
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

    if __name__ == "__main__":
    main()




   

