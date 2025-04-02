# 1.Write a decorator that counts the number of times a function has been called.

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1  # adding one to local count
        print(f"Function '{func.__name__}' has been called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0 #defining count locally for wrapper
    return wrapper 

@count_calls
def greet(name):
    print(f"Hello, {name}")

greet("Yash")
greet("nitin")
greet("shivam")

# 2..Write a decorator that repeats the execution of a function a specified number of times.

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator

num = int(input("enter the no of times to repeat:  "))
@repeat(num)
def greet1(name):
    print(f"hello , {name}")

greet1("yash")