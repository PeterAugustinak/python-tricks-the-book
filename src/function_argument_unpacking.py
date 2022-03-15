"""3.5 Function argument unpacking"""

def print_vector(x, y, z):
    print('<%s, %s, %s>' %(x, y, z))
    # or
    print(f'<{x}, {y}, {z}>')

print_vector(0, 0, 1)

"""Tuple and list unpacking"""
tuple_vector = (0, 1, 1)
list_vector = [1, 1, 1]

# instead of: print_vector(tuple_vector[0], tuple_vector[1], tuple_vector[2]):
print_vector(*tuple_vector)
print_vector(*list_vector)

"""Generator unpacking"""
genexpr = (x * x for x in range(3))
print_vector(*genexpr)

"""Dictionary unpacking"""
dict_vector = {'y': 0, 'z': 1, 'x': 2}
# keys will be user in random order
print_vector(*dict_vector)
# values will be associated with arguments in func definition
print_vector(**dict_vector)
