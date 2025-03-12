# demo 1
# class circle:
#     PI = 3.14
    
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return circle.PI*self.radius**2

# circle1 = circle(5)
# circle2 = circle(10)

# print(circle1.PI)
# print(circle2.PI)
# print(circle1.area())
# print(circle2.area())

# demo 2

# class rectangle:

#     def __init__(self,breath,length):
#         self.length = length
#         self.breath = breath

#     def area(self):
#         return self.length*self.breath


# rectangle1 = rectangle(1,10)
# rectangle2 = rectangle(2,40)

# print(rectangle1.area())
# print(rectangle2.area())

# demo 3

# class student:
#     def __init__(self,Name,age):
#         self.name = Name
#         self.age = age
#         self.marks={}
#     def add_marks(self,subject,mark):
#         self.marks[subject] = mark
#     def get_avg(self):
#         return sum(self.marks.values())
#     def display_student(self):
#         return f"Student: {self.name} , Age: {self.age} , Marks : {self.marks}"
    

# ramesh = student("Ramesh",14)
# ramesh.add_marks("maths",55)
# ramesh.add_marks("english",66)
# ramesh.add_marks("science",77)

# print(ramesh.display_student())
# print(f"Average Marks : {ramesh.get_avg()}")

# demo 4

class Library:
    # Class attributes
    total_books = 5
    all_books = ["The Great Gatsby", "1984", "Moby Dick", "War and Peace", "Hamlet"]

    def __init__(self, name):
        # Instance attributes
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        # Check if the book is available
        if book in Library.all_books:
            Library.all_books.remove(book)  # Remove the book from the library
            self.borrowed_books.append(book)  # Add it to the member's borrowed list
            Library.total_books -= 1  # Decrease the total number of books
            return f"{self.name} borrowed '{book}'"
        else:
            return "Book not available"

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)  # Remove it from the member's borrowed list
            Library.all_books.append(book)  # Add it back to the library
            Library.total_books += 1  # Increase the total number of books
            return f"{self.name} returned '{book}'"
        else:
            return f"{self.name} hasn't borrowed '{book}'"

    @classmethod
    def view_library_books(cls):
        print(f"Total books in the library: {cls.total_books}")
        print("Available books:", cls.all_books)

# Example usage:
# Creating a library member
member = Library("Alice")

# Borrowing a book
print(member.borrow_book("The Great Gatsby"))  # Output: Alice borrowed 'The Great Gatsby'

# Viewing available books in the library
Library.view_library_books()

# Returning a book
print(member.return_book("The Great Gatsby"))  # Output: Alice returned 'The Great Gatsby'

# Viewing available books after returning
Library.view_library_books()