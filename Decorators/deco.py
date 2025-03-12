# not good *******
# @my_decorator
# def my_course():
#     print("Python programming")

# my_course()


# demo 1

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("before function call")
        result = func(*args,**kwargs)
        print("after function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}")

greet("yash")

# demo 2

def decorator_one(func):
    def wrapper(*args,**kwargs):
        print("decorator one_before function execution")
        result = func(*args,**kwargs)
        print("decorator one-after function execution")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args,**kwargs):
        print("decorator two_before function execution")
        result = func(*args,**kwargs)
        print("decorator two-after function execution")
        return result
    return wrapper

def decorator_three(func):
    def wrapper(*args,**kwargs):
        print("decorator three_before function execution")
        result = func(*args,**kwargs)
        print("decorator three-after function execution")
        return result
    return wrapper

@decorator_one
@decorator_two
@decorator_three
def greet1(name):
    print(f"hello , {name}")

greet1("yash")

# demo 3

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator
    
@repeat(5)
def greet1(name):
    print(f"hello , {name}")

greet1("yash")