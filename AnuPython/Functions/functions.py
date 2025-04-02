
# function demo 1***********************************************

def div(x,y):                                          #function definition
    print(x/y)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
div(a,b)                                               #function call


c = int(input("Enter a number: "))
d = int(input("Enter another number: "))
div(c,d)


# function demo 2***********************************************

def square(first):                                   #function definition
    print(first*first)

demo = int(input("Enter a number: "))
square(demo)                                         #function call


# function demo 3***********************************************
def cube(secound):                                    #function definition
    print(secound*secound*secound)

demo = int(input("Enter a number: "))
cube(demo)                                           #function call


# function demo 4***********************************************

print("Maximum of the numbers 4,12,43,19,100 is : ",end="")
print(max(4,12,43,19,100))
print("Minimum of the numbers 4,12,43,19,100 is : ",end="")
print(min(4,12,43,19,100))