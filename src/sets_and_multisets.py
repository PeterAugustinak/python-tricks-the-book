"""5.4 Sets and Multisets"""

vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x * x for x in range(10)}

"""set - Your Go-To Set"""

print('e' in vowels)

letters = set('alice')
print(letters.intersection(vowels))

vowels.add('x')
print(vowels)

print(len(vowels))


"""frozenset - Immutable Sets"""
print()

vowels = frozenset(vowels)
try:
    vowels.add('p')
except AttributeError as e:
    print(e)

# Frozensets are hashable and can be used as dictionary keys:
d = {frozenset({1, 2, 3}): "Hello"}
print(d[frozenset({1, 2, 3})])

"""collections.Counter - Multisets"""
print()

from collections import Counter
inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)

more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
print(inventory)

# unique elements
print(len(inventory))
# total no. of elements
print(sum(inventory.values()))
