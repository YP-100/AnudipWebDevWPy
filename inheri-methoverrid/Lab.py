# question 1

class Staff:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    # calculate_salary method will be overridden in all other child classes
    def calculate_salary(self):
        return f"calculate salary according to your department....."
    # this will also be overridden in all other child classes
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Department: {self.department}")

class Doctor(Staff):
    def __init__(self, name, id, department, specialization, salary_per_month):
        super().__init__(name, id, department)
        self.specialization = specialization
        self.salary_per_month = salary_per_month

    def calculate_salary(self):
        return self.salary_per_month

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")

class Nurse(Staff):
    def __init__(self, name, id, department, shift, salary_per_month):
        super().__init__(name, id, department)
        self.shift = shift
        self.salary_per_month = salary_per_month

    def calculate_salary(self):
        return self.salary_per_month

    def display_info(self):
        super().display_info()
        print(f"Shift: {self.shift}")

class AdministrativeStaff(Staff):
    def __init__(self, name, id, department, role, salary_per_month):
        super().__init__(name, id, department)
        self.role = role
        self.salary_per_month = salary_per_month

    def calculate_salary(self):
        return self.salary_per_month

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

doc1 = Doctor("Dr. Amit Pal", 102, "Neurology", "Neurologist", 120000)
nurse1 = Nurse("shilpa sharma", 202, "ICU", "Day", 45000)
admin1 = AdministrativeStaff("Rahul pawar", 789, "HR", "Manager", 12000)

print("Doctor Information:")
doc1.display_info()
print(f"Salary: {doc1.calculate_salary()}")

print("Nurse Information:")
nurse1.display_info()
print(f"Salary: {nurse1.calculate_salary()}")

print("Administrative Staff Information:")
admin1.display_info()
print(f"Salary: {admin1.calculate_salary()}")

#question 2

class Vehicle:
    def __init__(self, registration_number, brand, rental_price_per_day):
        self.registration_number = registration_number
        self.brand = brand
        self.rental_price_per_day = rental_price_per_day

    def calculate_rental_cost(self, days_rented):
        return self.rental_price_per_day * days_rented

class Car(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, insurance_fee_per_day):
        #using super to access common attributes
        super().__init__(registration_number, brand, rental_price_per_day)
        self.insurance_fee_per_day = insurance_fee_per_day

    def calculate_rental_cost(self, days_rented):
        #using super to access common attributes
        return super().calculate_rental_cost(days_rented) + (self.insurance_fee_per_day * days_rented)

class Bike(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day):
        #using super to access common attributes
        super().__init__(registration_number, brand, rental_price_per_day)

class Truck(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, heavy_load_fee_per_day):
        #using super to access common attributes
        super().__init__(registration_number, brand, rental_price_per_day)
        self.heavy_load_fee_per_day = heavy_load_fee_per_day

    def calculate_rental_cost(self, days_rented):
        #using super to access common attributes
        return super().calculate_rental_cost(days_rented) + (self.heavy_load_fee_per_day * days_rented) # will add price for heavy load in rent


car = Car("CAR123", "Toyota", 50, 10)
bike = Bike("BIKE456", "Honda", 20)
truck = Truck("TRUCK789", "VOLVO", 100, 20)

print(f"Car Rental Cost for 15 days: {car.calculate_rental_cost(15)}")
print(f"Bike Rental Cost for 10 days: {bike.calculate_rental_cost(10)}")
print(f"Truck Rental Cost for 30 days: {truck.calculate_rental_cost(30)}")
