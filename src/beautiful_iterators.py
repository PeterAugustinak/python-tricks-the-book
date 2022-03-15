"""6.4 Beautiful Iterators"""

"""Iterating forever"""
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater("Hello")
# for item in repeater:
#     print(item)


""""How do for-in loops work in Python?"""
print()

repeater2 = Repeater("Hello")
iterator2 = repeater2.__iter__()
# while True:
#    item = iterator2.__next__()
#    print(item)


repeater3 = Repeater('Hello')
iterator3 = iter(repeater3)
print(next(iterator3))
print(next(iterator3))
print(next(iterator3))


"""A Simpler Iterator Class"""
print()

class RepeaterSimpler:

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

repeater4 = Repeater("Hello Simple")
# for item in repeater4:
#     print(item)


"""Who wants to Iterate Forever"""
print()

my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration as e:
    print(e)


class BoundedRepeater:

    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater5 = BoundedRepeater('Bounder', 3)
for item in repeater5:
    print(item)

print()

repeater6 = BoundedRepeater("Bounder2", 3)
iterator6 = iter(repeater6)
while True:
    try:
        item = next(iterator6)
    except StopIteration:
        break
    print(item)
