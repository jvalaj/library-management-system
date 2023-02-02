class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    def borrow_book(self):
            print(book.borrowed)
            if not book.borrowed:
                book.borrowed = True
                print(f"Success! Book {book.title} by {book.author} has been borrowed.")
            else:
                print(f"Book {book.title} by {book.author} is already borrowed.")
    def return_book(self):
        if book.borrowed:
            book.borrowed = False
            print(f" Book {book.title} by {book.author} has been returned.")
        else:
            print(f"Book {book.title} by {book.author} is not currently borrowed.")


class Library:
    def __init__(self):
        self.books = [Book("a","a"),Book("b","b")]
    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} by {book.author} has been added to the library.")

    def list_books(self):
        print("List of books in the library:")
        if len(self.books) > 0:
            for book in self.books:
                print(f" '{book.title}' - {book.author}")
        else:
            print("Library is Empty!")

    
    
# create library
library = Library()
print("Hello, Welcome to the most efficient Library Management System!")
print("You can do the following: \n 1. List of Books Available \n 2. Add A book \n 3. Borrow a book \n 4. Return a book")
anss = "Y"
while True:    
    if anss in "yY":
        ans = int(input("Enter number: "))

        # list books in library
        if ans == 1:
            library.list_books()
        elif ans == 2:
            # create books
            btitle = input("enter title")
            bauthor = input("enter author")
            bnumber = input("enter number")
            # add books to library
            library.add_book(Book(btitle,bauthor))
        elif ans == 3:
            # borrow books
            bbtitle = input("Enter title of book to be borrowed")
            bbauthor = input("Enter author of the book to be borrowed")
            val1=False
            for book in library.books:
                if book.title == bbtitle:
                    val1 = True
                    break
                else:
                    val1 = False
            if val1 == True:
                book1 = Book(bbtitle,bbauthor)
                Book.borrow_book(book1)
            else:
                print("Book isn't in the library, consider adding it!")
        elif ans == 4:
            # return books
            brtitle = input("enter title of book to be returned")
            brauthor = input("enter author of book to be returned")
            val1=False
            for book in library.books:
                if book.title == brtitle:
                    val1 = True
                    break
                else:
                    val1 = False
            if val1 == True:
                book1 = Book(brtitle,brauthor)
                Book.return_book(book1)
            else:
                print("Book isn't in the library, consider adding it!")
    else:
        break
    anss= input("do you want to continue? enter Y for yes, N for no: ")


