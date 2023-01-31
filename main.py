class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.borrowed = False

class Library:
    def __init__(self):
        self.books = [Book("Almanack","Naval Ravikant","123"),Book("Power","Hamza","122")]

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} by {book.author} has been added to the library.")

    def list_books(self):
        print("List of books in the library:")
        if len(self.books) > 0:
            for book in self.books:
                print(f" '{book.title}' - {book.author}, ISBN: {book.ISBN}")
        else:
            print("Library is Empty!")

    def borrow_book(self, book):
            if not book.borrowed:
                book.borrowed = True
                print(f"Book {book.title} by {book.author} has been borrowed.")
            else:
                print(f"Book {book.title} by {book.author} is already borrowed.")

    def return_book(self,book):
        if book.borrowed:
            book.borrowed = False
            print(f"Book {book.title} by {book.author} has been returned.")
        else:
            print(f"Book {book.title} by {book.author} is not currently borrowed.")

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
            # add books to library
            library.add_book(Book(btitle,bauthor,bnumber))
        elif ans == 3:
            # borrow books
            bbtitle = input("enter title of book to be borrowed")
            bbauthor = input("enter author of the book to be borrowed")
            bbnumber = input("enter number of book to be borrowed")
            for book in library.books:
                if book.title == bbtitle:
                    book1 = Book(bbtitle,bbauthor,bbnumber)
                    library.borrow_book(book1)
                else:
                    print("book isn't in the library, consider adding it!")
        elif ans == 4:
            # return books
            btitle = input("enter title of book to be returned")
            bauthor = input("enter author")
            library.return_book()
    else:
        break
    anss= input("do you want to continue? enter Y for yes, N for no")


