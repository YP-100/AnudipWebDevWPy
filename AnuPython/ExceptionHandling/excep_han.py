
# demo 1

def diveidebyzero(x ,y):
    try:
        result = x/y
        print(result)
    except:
        print("cannot divide by zero")

num = 78
den = 0
diveidebyzero(num,den)

# demo 2

def get_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("error : invalid input")

num = get_input("input an integer : ")

print("input value : ",num)

# demo 3

def get_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("error : invalid input")

num1 = get_input("input an integer : ")
num2 = get_input("input secound integer : ")
result = num1*num2

print("product of the numbers: ", result)