class Book:
    total_books = 0
    def __init__(self ,title , author , isbn ):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.total_books += 1

    def update_title(self,new_title):
        self.title = new_title

    def update_author(self,new_author):
        self.author = new_author

    def display_info(self,user_type = "reader"):
        if user_type=="librarian":
            print(f"Title : {self.title}, Author : {self.author} , ISBN : {self.isbn}")
        else:
            print(f"Title : {self.title}, Author : {self.author}")

    @staticmethod
    def book_info():
        print(f"Books are the foundation of education")
    
    @classmethod
    def get_totalbooks(cls):
        return cls.total_books
    
class Author:
    total_authors = 0
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
        self.books = []
        Author.total_authors += 1

    def add_books(self,book):
        self.books.append(book)

    def remove_books(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                Book.total_books -= 1
                print(f"Book with {isbn} removed. Author name : {self.name}")
                return
        print(f"Book not available with ISBN : {isbn}")

    @staticmethod
    def author_info():
        print("Content creator")
    
    @classmethod
    def get_total_authors(cls):
        return cls.total_authors
    
class library:
    library_count=0

    def __init__(self):
        self.books = []
        self.authors = []
        library.library_count += 1

    def add_book(self,book):
        self.books.append(book)

    def remove_books(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                Book.total_books -= 1
                print(f"Book with {isbn} removed.")
                return
        print(f"Book not available with ISBN : {isbn}")

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    @classmethod
    def get_library_count(cls):
        return cls.library_count

    @staticmethod
    def library_info():
        print("Library is access to books and authors")

book1 = Book("Java Programming","abc",'123123123')
book2 = Book("Python Programming","pqr",'456456456')

author1 = Author("abc","1900-01-01")
author1.add_books(book1)

library1 = library()
library1.add_book(book1)
library1.add_book(book2)

library1.list_books()

book1.update_title("Advance Java Programming")

book1.display_info("librarian")

print(f"Total number of books : {Book.get_totalbooks()}")
print(f"Total Authors : {Author.get_total_authors()}")
print(f"Total library : {library.get_library_count()}")

library.library_info()
Book.book_info()
Author.author_info()
