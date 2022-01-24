"""Fun with *args and ** kwargs"""
import functools

"""Function level"""
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

# print(foo())
foo("Hello")
foo("Hello", 1, 2, 3)
foo("Hello", 1, 2, 3, key1="value", key2=999)


"""Class level"""
class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

car = AlwaysBlueCar('green', 49343)
print(car.color)


"""Decorators level"""
def trace(func):
    @functools.wraps(func)
    def decorated_function(*args, **kwargs):
        print(func, args, kwargs)
        result = func(*args, **kwargs)
        print(result)
    return decorated_function

@trace
def greet(greeting, name):
    return f'{greeting} {name}'

greet('Hello', 'Bob')
