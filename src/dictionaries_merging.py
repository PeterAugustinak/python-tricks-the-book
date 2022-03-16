"""7.5 So many ways to Merge Dictionaries"""

xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

# by update
zs = {}
zs.update(xs)
zs.update(ys)
print(zs)

# implementation of above:
def update(dict1, dict2):
    for key , value in dict2.items():
        dict1[key] = value
    return dict1

zs2 = update(xs, ys)
print(zs2)

# by unpacking objects - works only for 2 dicts)
zs3 = dict(xs, **ys)
print(zs3)

# by unpacking objects - for arbitrary no. of dicst (Python 3.5 and higher)
zs4 = {**xs, **ys}
print(zs4)
