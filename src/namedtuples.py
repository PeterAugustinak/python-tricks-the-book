"""4.6: What namedtuples are good for"""
import json

"""Standard tuples"""
tup = ('Hello', object(), 42)
print(tup)
print(tup[2])

# elements are immutable
try:
    tup[2] = 23
except TypeError as err:
    print(err)


"""Using namedtuple"""
print()

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
# behind the scenes: 'color mileage'.split() -> ['color', 'mileage']
# so it can be done as: Car = namedtuple('Car', ['color', 'mileage'])

# instantiate object from namedtuple
my_car = Car('red', 2323)

# attributes can be reached as follows:
print(my_car.color)
print(my_car.mileage)
print(my_car[0])
print(tuple(my_car))
color, mileage = my_car
print(color, mileage)
print(*my_car)

# repr is working
print(repr(my_car))

# attributes cannot be set of course
try:
    my_car.color = 'blue'
except AttributeError as err:
    print(err)

"""Adding methods into the namedtuple - such a"""
print()

class MyCarWithMethods(Car):

    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 1234)
print(c.hexcolor())

"""Adding fields"""
print()

ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge', ))
ec = ElectricCar('red', 1234, 45.0)
print(ec)

"""Helper methods"""
print()
# usually methods starting with _ are for internal use. This does not apply
# for namedtuples

# showing as a dict
dct = my_car._asdict()
print(type(dct), dct)

# this is good for avoid typos when generating json output
js = json.dumps(my_car._asdict())
print(type(js), js)

# actually changing fields
blue_car = my_car._replace(color='green')
print(blue_car)

# creating new instance from a sequence of iterable
new_car = Car._make(['brown', 235234])
print(new_car)
