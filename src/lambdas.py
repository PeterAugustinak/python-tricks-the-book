"""3.2 Lambdas are single-expression functions"""

"""Using by adding to var"""
add = lambda x, y: x + y
print(add(5, 3))

"""Lambda expression"""
print((lambda x, y: x + y)(5, 3))

"""Real (only?) useful usage"""
tuples = [(1, 'd'), (2, 'b'), (3, 'a'), (4, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
# just playing here ..
for num, char in [tup for tup in sorted_tuples]:
    print(f'{char} -> {num}')

# another sorting example
print(sorted(range(-5, 6), key=lambda x: x * x))  # TODO: I don't get it

"""Usage as closures"""
def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(7))

# same thing once by filter, once by list comp
# bad idea - filter + lambda
print(list(filter(lambda x: x % 2 == 0, range(16))))
# better idea - list comprehension
print([x for x in range(16) if x % 2 ==0])
