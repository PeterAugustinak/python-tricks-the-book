"""5.1: Dictionaries, Maps and Hashtables"""

import collections


"""Standard built-in dict class"""
phonebook = {
    'bob': 7373,
    'alice': 44353,
    'jack': 434233,
}

squares = {x: x * x for x in range(6)}

print(phonebook['alice'])
print(squares)


"""Remember the insertion order dict"""
print()

ordered_dict = collections.OrderedDict(one=1, two=2, three=3)
print(ordered_dict)

ordered_dict['four'] = 4
print(ordered_dict)
print(ordered_dict.keys())


"""Return default values for missing keys"""
print()

default_dict = collections.defaultdict(list)
# accessing non-existing keys creates it and initializes with default fact (
# list in this case)
default_dict['dogs'].append('Rufus')
default_dict['dogs'].append('Rex')

print(default_dict)
print(default_dict['dogs'])


"""Search multiple dictionary as a single mapping"""
print()

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain_dict = collections.ChainMap(dict1, dict2)

print(chain_dict)
print(chain_dict['three'])
print(chain_dict['two'])

try:
    print(chain_dict['missing'])
except KeyError as err:
    print(err)


"""Wrapper for making read only dictionaries"""
print()

from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

print(read_only['one'])

try:
    read_only['one'] = 23
except TypeError as err:
    print(err)

# Updates to original dict are reflected to proxy dict
writable['one'] = 42
print(read_only)

