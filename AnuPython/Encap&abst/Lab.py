from abc import ABC, abstractmethod

#using abstract class
class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_employee_details(self):
        pass

    @abstractmethod
    def raise_salary(self, percentage):
        pass

# Subclass for full-time employees
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def get_employee_details(self):
        return f"Full-Time Employee: {self.name}, ID: {self.emp_id}, Salary: {self.calculate_salary()}"

    def raise_salary(self, percentage):
        self.monthly_salary += self.monthly_salary * (percentage / 100)

# Subclass for part-time employees
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_employee_details(self):
        return f"Part-Time Employee: {self.name}, ID: {self.emp_id}, Salary: {self.calculate_salary()}"

    def raise_salary(self, percentage):
        self.hourly_rate += self.hourly_rate * (percentage / 100)

full_time_emp = FullTimeEmployee("Yash", 101, 50000)
part_time_emp = PartTimeEmployee("Siddharth", 102, 200, 80)

print(full_time_emp.get_employee_details())
print(part_time_emp.get_employee_details())

# Raising salaries
full_time_emp.raise_salary(10)  # 10% raise
part_time_emp.raise_salary(5)  # 5% raise

print("After Salary Raise:")
print(full_time_emp.get_employee_details())
print(part_time_emp.get_employee_details())
