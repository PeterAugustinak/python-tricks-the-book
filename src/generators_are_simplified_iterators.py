"""6.5 Generators Are Simplified Iterators"""

# iterator class as a generator
def repeater(value):
    while True:
        yield value

# for x in repeater('Hi'):
#     print(x)

print(repeater('Hi'))

generator_obj = repeater('Hi')
print(next(generator_obj))

# generator object -> iterator
iterator = repeater('Hi')
print(next(iterator))
print(next(iterator))
print(next(iterator))


"""Generators That Stop Generating"""
print()

def repeat_three_times(value):
    yield value
    yield value
    yield value

for x in repeat_three_times('Hey there'):
    print(x)

iterator = repeat_three_times('Hey there')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration as e:
    print(e)

def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value

for x in bounded_repeater('Hi', 4):
    print(x)


def bounded_repeater_final(value, max_repeats):
    for i in range(max_repeats):
        yield value

for x in bounded_repeater('Hi final', 4):
    print(x)
