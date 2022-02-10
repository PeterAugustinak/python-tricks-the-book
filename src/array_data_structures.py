"""5.2: Array data structures"""

"""list - Mutable Dynamic Arrays"""
arr = ['one', 'two', 'three']
print(arr[0])

# repr
print(arr)
# lists are mutable
arr[1] = 'hello'
print(arr)

del arr[1]
print(arr)

# lists can hold arbitrary data types
arr.append(23)
print(arr)

"""tuple - Immutable Containers"""
print()

arr = 'one', 'two', 'three'
print(arr[0])

# repr
print(arr)
# tuples are immmutable
try:
    arr[1] = 'hello'
except TypeError as e:
    print(e)

try:
    del arr[1]
except TypeError as e:
    print(e)

# tuples can hold arbitrary data types - adding elements create copy of tuple
arr2 = arr + (23, )
print(arr2)

"""array.array - Basic Typed Arrays"""
print()

import array
arr = array.array('f', (1.0, 1.5, 2.5))
print(arr[1])

# repr
print(arr)

# arrays are mutable
arr[1] = 23.0
print(arr)

del arr[1]
print(arr)

arr.append(42.0)
print(arr)

# arrays are "typed"
try:
    arr[1] = 'hello'
except TypeError as e:
    print(e)

"""str - Immutable Arrays of Unicode Characters"""
print()

arr = 'abcd'
print(arr[1])

# repr? :)
print(arr)

# strings are immutable
try:
    arr[1] = 'e'
except TypeError as e:
    print(e)

try:
    del arr[1]
except TypeError as e:
    print(e)

# strings can be unpacked to a list to get a mutable representation
arr_l = list(arr)
print(arr_l)
# and "packed" back
arr = ''.join(arr_l)
print(arr)

# strings are recursive data structures
print(type('abc'))
print(type('abc'[0]))


"""bytes - Immutable Arrays of Single Bytes"""
print()

arr = bytes((0, 1, 2, 3))
print(arr[1])

# bytes literals have their own syntax
print(arr)
arr = b'\x00\x01\x02\x03'
print(arr)

# only valid "bytes" are allowed
try:
    bytes((0, 300))
except ValueError as e:
    print(e)

# bytes are immutable
try:
    arr[1] = 23
except TypeError as e:
    print(e)

try:
    del arr[1]
except TypeError as e:
    print(e)

"""bytearray - Mutable Arrays of Single Bytes"""
print()

arr = bytearray((0, 1, 2, 3))
print(arr[1])

# repr
print(arr)

# bytearrays are mutable
arr[1] = 23
print(arr)

# bytearrays can grow and shrink in size
del arr[1]
print(arr)

arr.append(42)
print(arr)

# bytearrays can only hold bytes (0 - 255)
try:
    arr[1] = 'hello'
except TypeError as e:
    print(e)

try:
    arr[1] = 257
except ValueError as e:
    print(e)

# bytearrays can be converted back into bytes objects (this will copy the data)
bytes(arr)
print(arr)
