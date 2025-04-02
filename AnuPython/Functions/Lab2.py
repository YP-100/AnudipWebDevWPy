

# Accept a name from the user and display that in lower case using lower() function

def low(name):
    return name.lower()


name = input("Enter your name: ")
print(low(name))

# Write a function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. 

def stat(num):
    if(num>0):
        return "Positive"
    elif(num<0):
        return "Negative"
    else:
        return "Zero"
num = int(input("Enter a number: "))
print(stat(num))