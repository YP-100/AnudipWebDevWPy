# 1. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 

try:
    file = open("123.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")


# 2. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if not num1.isdigit() or not num2.isdigit():
        raise TypeError("Inputs must be numerical.")
    print("first number is : ",num1)
    print("secound number is : ",num2)
except TypeError as e:
    print("Both values must be numerical")
