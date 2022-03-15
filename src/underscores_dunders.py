"""2.4 Underscores, Dunders and more"""

_var = ''  # value for internal use (by convention)
__var = '' # name mangling within class usage (enforced by Python interpreter)
var_ = '' # to avoid conflicts with Python keywords
__var__ = '' # special methods defined by Python language
_ = ''  # temporary name for variables (loops, unpacking)

"""Trailing underscores"""
class Test:
    def __init__(self):
        self.foo = 11  # public
        self._bar = 23  # private by convention
        self.__baz = 42  # protected

t = Test()
print(t.foo)
print(t._bar)
print(t.__baz)

"""Single underscore usage - when we do not need to use it"""
for _ in range(10):
    print('hello world')

"""only some values unpacked to be used"""
car = ('red', 'auto', 12, 28.2)
color, _, _, miles = car

# in REPL _ = last value
# [1, 2, 3]
# _
# [1, 2, 3]
