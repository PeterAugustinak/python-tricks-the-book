"""7.4 The Craziest Dict Expression in the West"""

crazy = {True: 'yes', 1: 'no', 1.0: 'maybe'}
print(crazy)
# {True: 'maybe'}

# what is happening?
xs = dict()
xs[True] = 'yes'
xs[1] = 'no'
xs[1.0] = 'maybe'
print(xs)

# why?
print(True == 1 == 1.0)

# using bools as indexes
print(['no', 'yes'][True])
print(['no', 'yes'][False])
print(['no', 'yes'][1])

# when new value is added, dict don't update the keys (if they are the same),
# only values
ys = {1.0: 'no'}
ys[True] = 'yes'
print(ys)

class AlwaysEquals:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)

print(AlwaysEquals() == AlwaysEquals())
print(AlwaysEquals() == 42)
print(AlwaysEquals() == 'what?')

objects = [AlwaysEquals(),
           AlwaysEquals(),
           AlwaysEquals()]

print([hash(obj) for obj in objects])

# keys are not getting overwritten again
print({
    AlwaysEquals(): 'yes',
    AlwaysEquals(): 'no',
})

class SameHash:
    def __hash__(self):
        return 1

a = SameHash()
b = SameHash()
print(a == b)
print(hash(a), hash(b))
print({a: 'a', b: 'b'})

# keys have same hash
print(hash(True), hash(1), hash(1.0))
