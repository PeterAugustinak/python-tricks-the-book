"""4.2 String conversion (Every class needs a __repr__)"""

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # repr (mostly for debugging for devs) - should be defined always
    def __repr__(self):
        # using !r ensures that it uses repr(self.attr) instead of str(
        # self.attr)
        return (f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})')

    # str (mostly for users) - can be defined (if it's not, repr is called
    def __str__(self):
        return f'a {self.color} car'

# Usage:
car = Car('blue', 10200)
# try in REPL
repr(car)
str(car)
print(car)
car
