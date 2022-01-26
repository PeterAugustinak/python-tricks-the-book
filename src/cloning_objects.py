"""4.4: Cloning objects for fun and profit"""

"""Copying standard collections"""
# SHALLOW copying of factory functions for existing (mutable) collection
original_list = [1, 2, 3]
original_dict = {'a': 1, 'b': 2, 'c': 3}
original_set = {1, 2, 3}

new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)

# SHALLOW copy example
xs = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
print(f'xs: {xs}')
print(f'ys: {ys}')

# append new list item into original list
xs.append(['new sublist'])
print(f'xs after append: {xs}')
print(f'ys after append into xs: {ys}')

# change item inside one of the nested list in original list - copied list
# affected
xs[1][0] = 'X'
print(f'xs after change of item in one of the list: {xs}')
print(f'ys after change in the xs : {ys}')

# deep copies
import copy
zs = copy.deepcopy(xs)
print(f'xs: {xs}')
print(f'zs: {zs}')

# change one item in the nested list after deepcopy - no affect of copied list
xs[1][1] = 'Y'
print(f'xs change in nested item: {xs}')
print(f'zs after change in xs : {zs}')


"""Copying arbitrary objects"""
print()

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

# shallow copy by copy.copy func
a = Point(23, 42)
b = copy.copy(a)

# as it contains only immutable collection, nothing can be wrong even with
# shallow copy is used
print(a)
print(b)
print(a is b)


class Rectangle:

    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f'Rectangle({self.topleft!r}, {self.bottomright!r})'

rect = Rectangle(Point(0, 1), Point(5, 6))
shallow_rect = copy.copy(rect)

print(rect)
print(shallow_rect)
print(rect is shallow_rect)

# but then by change in original, copied rect is affected as well
rect.topleft.x = 999
print(rect)
print(shallow_rect)

# so use deep copy
deep_rect = copy.deepcopy(rect)
rect.bottomright.y = 999

# deep copy rectangle not affected
print(rect)
print(deep_rect)
