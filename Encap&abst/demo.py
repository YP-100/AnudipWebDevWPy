# demo **************************

class Myclass:
    def __init__(self, value):
        self.protected_value = value

    def protected_method(self):
        return self.protected_value
    

m1 = Myclass(10)
print(m1.protected_method())


# demo 1 **************************
class bankaccount:
    def __init__(self, owner,balance = 0):
        self.owner = owner
        self.balance = balance    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful. New balance:", self.balance)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. New balance:", self.balance)
        else:
            print("Invalid amount or insufficient balance")

    def getbalance(self):
        return self.balance



account = bankaccount("Amar Kumar", 10000)
account.deposit(5000)

account.withdraw(8000)

print(account.getbalance())
print(account.balance)    # can do but not recommended


# demo 2 **************************

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary cannot be negative")
        
    @salary.deleter
    def salary(self):
        del self._salary
        print(f"Salary for {self.name} has been deleted.")


emp = Employee("Amit", 5000)

print(emp.salary)

emp.salary = 6000

print(emp.salary)

del emp.salary