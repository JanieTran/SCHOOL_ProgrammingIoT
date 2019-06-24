# Reference: https://realpython.com/primer-on-python-decorators/#decorating-classes
def my_decorator(func):
    def wrapper():
        print("--- Before calling the function ---")
        func()
        print("--- After calling the function ---")

    return wrapper


@my_decorator
def hello_world():
    print("Hello World!")


hello_world()
