"""4.1: - Object comparisons: 'is' vs '=='"""

# == example. Objects are the same
a = [1, 2, 3]
b = a

print(f'Object a: {a}')
print(f'Object b: {b}')
print(f'Objects a and b are equal: {a == b}')
print(f'Objects a and b are identical: {a is b}')

c = list(a)
print(f'Object c (made by copy of a: {c}')
print(f'Objects a and c are equal: {a == c}')
print(f'Objects a and c are identical: {a is c}')
