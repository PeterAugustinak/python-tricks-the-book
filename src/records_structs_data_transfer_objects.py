"""5.4 Records, Structs and Data Transfer Objects"""

"""dict - Simple Data Objects"""

car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True,
}

car2 = {
    'color': 'blue',
    'mileage': 40231,
    'automatic': False,
}

# Dicts have a nice repr:
print(repr(car2))

# Get mileage:
print(car2['mileage'])

# Dicts are mutable
car2['mileage'] = 12
car2['windshield'] = 'broken'
print(car2)

# No protection against wrong field names or missing/extra fields:
car3 = {
    'colr': 'green',
    'automatic': False,
    'windshield': 'broken'
}

"""tuple - Immutable Groups of Objects"""
print()
import dis

print(dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval')))

# Fields: color, mileage, automatic
car4 = ('red', 3812.4, True)
car5 = ('blue', 42031.0, False)

# Tuple instances have a nice repr:
print(repr(car4))
print(car5)

# Get mileage
print(car5[1])

# Tuples are immutable
try:
    car5[1] = 12
except TypeError as e:
    print(e)

# No protection against missing/extra fields or a wrong order:
car6 = (3431.5, 'green', True, 'silver')


"""Writing a Custom class - More Work, More Control"""
print()

class Car:

    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic


car7 = Car('red', 3812.4, True)
car8 = Car('blue', 40231.0, False)

# Get the mileage
print(car8.mileage)

# Classes are mutable
car8.mileage = 12
car8.windshield = 'broken'

# String representation is not very useful
# (must add a manually written __repr__ method):
print(car1)


"""collections.namedtuple - Convenient Data Objects"""
print()

from collections import namedtuple
from sys import getsizeof

p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)

print(getsizeof(p1))
print(getsizeof(p2))

print()
Car = namedtuple('Car', 'color mileage automatic')
car9 = Car('red', 3812.4, True)

# Instance have a nice repr:
print(repr(car9))

# Accessing fields:
print(car9.mileage)

# Fields are immutable:
try:
    car9.mileage = 12
except AttributeError as e:
    print(e)

try:
    car9.windshield = 'broken'
except AttributeError as e:
    print(e)

"""typing.NamedTuple - improved Namedtuples"""
print()

from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car10 = Car('red', 3812.4, True)

# Instance have a nice repr:
print(repr(car10))

# Accessing fields:
print(car10.mileage)

# Fields are immutable:
try:
    car10.mileage = 12
except AttributeError as e:
    print(e)

try:
    car10.windshield = 'broken'
except AttributeError as e:
    print(e)

# Type annotations are not enforced without a separate type checking tool like
# mypy:
print(Car('red', 'NOT_A_FLOAT', 99))

"""struct.Struct - Serialized C Structs"""
print()

from struct import Struct
MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)

# All you get is a blob of data:
print(data)

# Data blobs can be unpacked again:
print(MyStruct.unpack(data))

"""types.SimpleNamespace - Fancy Attribute Access"""
from types import SimpleNamespace

car12 = SimpleNamespace(color='red', mileage=3812.4, automatic=True)

# The default repr:
print(repr(car12))

# Instances support attribute access and are mutable:
car12.mileage = 12
car12.windshields = 'broken'
del car12.automatic

print(car12)
