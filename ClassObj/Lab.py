# Q.1 --> 
# Create a class Employee that manages employee details:
# 1. Instance Attributes: ○ name: The employee's name. ○ salary: The employee's salary. ○ position: The employee's position. 
# 2. Methods: ○ promote(self, new_position): Updates the employee's position. ○ update_salary(self, new_salary): Updates the employee's salary. ○ display_info(self): Displays the employee's name, position, and salary

# class Employee that manages employee details:

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        
    # Methods: promote(self, new_position): Updates the employee's position. update_salary(self, new_salary): Updates the employee's salary. display_info(self): Displays the employee's name, position, and salary

    #promote(self, new_position) : updates self.position to new_position
    def promote(self, new_position):
        self.position = new_position
        print(f"{self.name} has been promoted to {self.position}.")

    # update_salary(self, new_salary) : updates self.salary to new_salary
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to {self.salary}.")

    # display_info(self) : displays latest information

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")

emp1 = Employee("Rakesh", 50000, "H.R")
emp1.display_info()

emp1.promote("H.R director")
emp1.update_salary(70000)
emp1.display_info()

# Q.2-->
# Create a class MovieLibrary that manages a collection of movies:
# 1. Class Attribute: ○ available_movies: A list of all movies available in the library. 
# 2. Instance Attributes: ○ member_name: The name of the library member. ○ borrowed_movies: A list of movies borrowed by the member. 
# 3. Methods: ○ borrow_movie(self, movie): Borrows a movie from the library if available. ○ return_movie(self, movie): Returns a movie to the library. ○ view_borrowed_movies(self): Prints a list of movies borrowed by the member


# a class MovieLibrary that manages a collection of movies:

class MovieLibrary:
    # Class Attribute: available_movies: A list of all movies available in the library. 
    available_movies = ["Chaava", "Interstellar", "Pushpa 2", "Avatar", "Jumanji"]

    def __init__(self, member_name):
        #Instance Attributes: member_name: The name of the library member. borrowed_movies: A list of movies borrowed by the member 
        self.member_name = member_name
        self.borrowed_movies = []
    #  Methods: borrow_movie(self, movie): checks if movie is available and if yes then lets the user borrow
    def borrow_movie(self, movie):
        if movie in MovieLibrary.available_movies:
            MovieLibrary.available_movies.remove(movie)
            self.borrowed_movies.append(movie)
            print(f"{self.member_name} borrowed '{movie}'.")
        else:
            print(f"Sorry, '{movie}' is not available.")

    # return_movie(self, movie): Returns a movie to the library,by updating the self.borrowed_movies and moving it to available_movie
    def return_movie(self, movie):
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            print(f"{self.member_name} returned '{movie}'.")
        else:
            print(f"{self.member_name} hasn't borrowed '{movie}'.")
    #view_borrowed_movies(self): Prints the list of movies borrowed by the member
    def view_borrowed_movies(self):
        print(f"{self.member_name}'s Borrowed Movies: {self.borrowed_movies}")

member1 = MovieLibrary("Rakesh")

member1.borrow_movie("Chaava")
member1.view_borrowed_movies()
MovieLibrary.available_movies

member1.return_movie("Chaava")
MovieLibrary.available_movies

member2 = MovieLibrary("Raj")
member2.borrow_movie("Kantara")  #will  print not available
member2.view_borrowed_movies()
