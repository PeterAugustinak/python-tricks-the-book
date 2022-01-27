"""4.5: Abstract Base Classes Keep Inheritance in check"""

"""Approach with no Abstract class"""
class Base:

    def foo(self):
        raise NotImplementedError("foo not implemented")

    def bar(self):
        raise NotImplementedError("bar not implemented")

class Concrete(Base):
    def foo(self):
        return 'foo() called'

# it is possible to instantiate Base even when there is no implementation =
# useless
b = Base()
try:
    b.foo()
except NotImplementedError as err:
    print(err)

# it is possible to instantiate from Child class, even there is missing some
# method implementations
c = Concrete()
print(c.foo())
# the problem appears only after when some not implemented method is called
try:
    c.bar()
except NotImplementedError as err:
    print(err)

"""Abstract Base class approach"""
print()

from abc import ABCMeta, abstractmethod, ABC

class BaseAbc(metaclass=ABCMeta):
# ABC and ABCmeta appears to be the same in this case
# class BaseAbc(ABC):

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class ConcreteAbc(BaseAbc):

    def foo(self):
        return 'foo() called'

    # second abstractmethod forgotten to be implemented

# this will raise TypeError - it is not possible to instantiate Abstract class
try:
    b_abc = BaseAbc()
except TypeError as err:
    print(err)

# when trying to instantiate child class, error is raised right away
try:
    c_abc = ConcreteAbc()
except TypeError as err:
    print(err)
