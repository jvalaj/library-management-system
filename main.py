class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.borrowed = False

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"Book {self.title} by {self.author} has been borrowed.")
        else:
            print(f"Book {self.title} by {self.author} is already borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"Book {self.title} by {self.author} has been returned.")
        else:
            print(f"Book {self.title} by {self.author} is not currently borrowed.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} by {book.author} has been added to the library.")

    def list_books(self):
        print("List of books in the library:")
        for book in self.books:
            print(f"{book.title} by {book.author}")

print("Hello, Welcome to the most efficient Library Management System! You can do the following: \n 1. List of Books Available \n 2. Return A book \n 3. Add a book")
ans = input("enter what you want to do")

# create library
library = Library()

# create books
book1 = Book("War and Peace", "Leo Tolstoy", "123456789")
book2 = Book("Moby Dick", "Herman Melville", "987654321")
book3 = Book("Pride and Prejudice", "Jane Austen", "555666777")

# add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# list books in library
library.list_books()

# borrow books
book1.borrow_book()
book2.borrow_book()

# try to borrow already borrowed book
book2.borrow_book()

# list books in library
if ans == 1:
    library.list_books()

# return books
book1.return_book()
book2.return_book()

