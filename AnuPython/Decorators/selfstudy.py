def counts(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1   
        print(f"Function 'greet' was called {count} times")
        return func(*args, **kwargs) 
    return wrapper  

@counts
def greet(name):
    print(f"Hello, {name}!")

greet("Yash")
greet("nitin")
greet("shivam")



