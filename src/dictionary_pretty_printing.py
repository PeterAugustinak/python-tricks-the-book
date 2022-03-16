"""7.6 Dictionary Pretty-Printing"""

# using string repr
mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(mapping)
print(str(mapping))

# using json
import json
d = json.dumps(mapping, indent=4, sort_keys=True)
print(d)

# json does not work if keys are not primitive data type
try:
    b = json.dumps({all: 'no'})
except TypeError as e:
    print(e)

# json does not work with complex data type like sets as values
mapping['d'] = {1, 2, 3}
try:
    c = json.dumps(mapping)
except TypeError as e:
    print(e)

# using pprint
import pprint
pprint.pprint(mapping)
