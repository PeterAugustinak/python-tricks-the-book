"""7.2 Sorting Dictionaries for Fun and Profit"""

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

# by keys
by_keys = sorted(xs.items())
print(by_keys)

# by values using lambda
by_values = sorted(xs.items(), key=lambda x: x[1])
print(by_values)

# by values using operator
import operator
by_operator = sorted(xs.items(), key=operator.itemgetter(1))
print(by_operator)

# sorted by custom
xs = {'a': -4, 'c': 2, 'b': -3, 'd': 1}
by_custom = sorted(xs.items(), key=lambda x: abs(x[1]))
print(by_custom)

# with reverse
reverse = sorted(xs.items(), key=lambda x: x[1], reverse=True)
print(reverse)
