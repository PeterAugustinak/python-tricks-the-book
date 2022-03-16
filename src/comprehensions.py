"""6.2 Comprehending Comprehensions"""

# comprehension
# values = [expression for item in collection]
squares = [x * x for x in range(10)]
print(squares)

# above is same as:
# values = []
# for item in collection:
#    values.append(expression)
squares = []
for x in range(10):
    squares.append(x * x)
print(squares)

# using condition
# values = [expression for item in collection if condition]
even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)

# same as above:
# values = []
# for item in collection:
#    if condition:
#        values.append(expression)
even_squares = []
for x in range(10):
    if not x % 2:
        even_squares.append(x * x)
print(even_squares)

# sets comprehension - NOT ORDERED
s = {x * x for x in range(-9, 10)}
print(s)

# dictionary comprehension
d = {x: x * x for x in range(5)}
print(d)
