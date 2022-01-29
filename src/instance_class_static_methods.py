"""4.8: Instance, Class and Static Methods demystified"""


class MyClass:

    def method(self):
        return 'Instance method called', self

    @classmethod
    def classmethod(cls):
        return 'Class method called', cls

    @staticmethod
    def staticmethod():
        return 'Static method called'


obj = MyClass()

"""Calling methods via instance"""

# instance method
print(obj.method())
# same as:
MyClass.method(obj)

# class method
print(obj.classmethod())

# static method
print(obj.staticmethod())

"""Calling methods via class"""
print()

# class method
print(MyClass.classmethod())
# static method
print(MyClass.staticmethod())
# instance method - impossible to call via class itself
try:
    MyClass.method()
except TypeError as err:
    print(err)


"""Class methods as an alternative constructor"""
print()

class Pizza:

    def __init__(self, ingredients, name="Your own"):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.__class__.__name__} "{self.name}" ' \
               f'{self.ingredients}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.ingredients!r}, ' \
               f'{self.name!r})'

    # follow 'alternative constructor' classmethods
    @classmethod
    def margherita(cls):
        return cls(['vegan mozzarella', 'tomatoes'], "Vegan Margherita")

    @classmethod
    def mushroomsy(cls):
        return cls(['mushrooms', 'pepper'], "Mushroomy")


print(Pizza(['vegan cheese', 'tomatoes']))
print(Pizza.margherita())
mushroomsy_pizza = Pizza.mushroomsy()
print(repr(mushroomsy_pizza))


"""Usage of static methods"""
print()

import math
class PizzaStatic:

    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, {self.ingredients!r}')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return round(math.pi * r ** 2 , 2)

pizza = PizzaStatic(4, ['vegan cheese', 'pepper'])
print(pizza)
print(pizza.area())
# static method can be called from instance or directly from class object
pizza.circle_area(4)
PizzaStatic.circle_area(4)
