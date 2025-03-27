# 1: Create a program that greets the user based on the current time (e.g., "Good Morning" before noon, "Good Afternoon" in the afternoon, and "Good Evening" in the evening). Use the datetime module to retrieve the current time and conditionally display a greeting. Output:1

import datetime

def greet_user():
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        greeting = "Good Morning"
    elif current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    print(greeting)

greet_user()

# 2: Write a Python program that asks the user to input two dates (in YYYY-MM-DD format) and calculates the number of days between the two dates. Use the datetime module to perform the calculation

def days_between_dates():
    dateinformat = "%Y-%m-%d"
    
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")

    # use try because if usere doesnot give input in YYYY-MM-DD it will not throw valueerror

    try:
        d1 = datetime.datetime.strptime(date1, dateinformat)
        d2 = datetime.datetime.strptime(date2, dateinformat)

        difference = abs((d2 - d1).days)
        print(f"The number of days between {date1} and {date2} is {difference} days.")
    
    except ValueError:
        print("Invalid date format! Please enter dates in YYYY-MM-DD format.")

days_between_dates()
