class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.borrowed = False

    def borrow_book(self,title,author):
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
        if len(self.books) > 0:
            for book in self.books:
                print(book)
                print(f" {book.title} by {book.author}")
        else:
            print("Library is Empty!")

# create library
library = Library()

print("Hello, Welcome to the most efficient Library Management System!")
print("You can do the following: \n 1. List of Books Available \n 2. Add A book \n 3. Borrow a book \n 4. Return a book")
anss = "Y"
while True:    
    if anss in "yY":
        ans = int(input("enter what you want to do"))

        # list books in library
        if ans == 1:
            library.list_books()
        elif ans == 2:
            # create books
            btitle = input("enter title")
            bauthor = input("enter author")
            bnumber = input("enter number")
            book1 = Book(btitle,bauthor,bnumber)
            # add books to library
            library.add_book(book1)
        elif ans == 3:
            # borrow books
            btitle = input("enter title of book to be borrowed")
            bauthor = input("enter author")
            for book in library.books:
                if btitle == book
                book1.borrow_book()
        elif ans == 4:
            # return books
            btitle = input("enter title of book to be returned")
            bauthor = input("enter author")
            book1.return_book()
    else:
        break
    anss= input("do you want to continue? enter Y for yes, N for no")


