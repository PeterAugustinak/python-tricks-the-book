"""4.7: Class vs Instance Variable Pitfalls"""

"""Defining class and instance vars"""
class Dog:

    num_legs = 4  # class var

    def __init__(self, name):
        self.name = name #  instance var

jack = Dog('Jack')
jill = Dog('Jill')
print(jack.name, jill.name)
print(jack.num_legs, jill.num_legs)
print(Dog.num_legs)
try:
    print(Dog.name)
except AttributeError as err:
    print(err)

"""Changing class var"""
print()
Dog.num_legs = 6
print(jack.num_legs, jill.num_legs)

Dog.num_legs = 4
jack.num_legs = 6
print(jack.num_legs, jill.num_legs, Dog.num_legs)

# after above changes, jack's instance var is shadowing Dog's class var
print(jack.num_legs, jack.__class__.num_legs)


"""Class counter example"""
print()

class CounterObject:

    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

# every time object is created, num_instances counter goes + 1
print(CounterObject.num_instances)
print(CounterObject().num_instances)
print(CounterObject().num_instances)
print(CounterObject().num_instances)
print(CounterObject.num_instances)

# incorrect implementation example
class BuggyCounterObject:

    num_instances = 0

    def __init__(self):
        self.num_instances += 1  # this will shadow class instance

# class var counter is never raised as self.num_instances shadows class var
# and creates new instance var
print(BuggyCounterObject.num_instances)
print(BuggyCounterObject().num_instances)
print(BuggyCounterObject().num_instances)
print(BuggyCounterObject().num_instances)
print(BuggyCounterObject.num_instances)
