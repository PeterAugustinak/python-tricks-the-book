"""6.6 Generator Expressions"""

# generator comprehension
# genexpr = (expression for item in collection)
iterator = ('Hello comprehension' for i in range(3))
for item in iterator:
    print(item)

# this is the same as above:
# def generator():
#    for item in collection:
#        yield expression
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

iterator = bounded_repeater('Hello bounded', 3)
for item in iterator:
    print(item)


"""Generator Expression vs List Comprehension"""
print()
listcomp = ['Hello' for i in range(3)]
genexprt = ('Hello' for i in range(3))

print(listcomp)
print(genexprt)

print(next(genexprt))
print(next(genexprt))
print(next(genexprt))
try:
    print(next(genexprt))
except StopIteration as e:
    print(e)

# converting to list
genexprt = ('Hello' for i in range(3))
print(list(genexprt))


"""Filtering values"""
print()

# genexpr = (expression for item in collection if condition)
even_squares = (x * x for x in range(10) if not x % 2)
for x in even_squares:
    print(x)

# same as:
# def generator():
#    for item in collection:
#        if condition:
#            yield expression


"""In-line Generator Expressions"""
print()
for x in ('Bom dia' for i in range(3)):
    print(x)

print(sum(x * 2 for x in range(10)))
