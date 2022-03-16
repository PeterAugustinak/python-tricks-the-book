"""6.7 Iterator Chains"""

def integers():
    for i in range(1, 9):
        yield i

chain = integers()
print(list(chain))

def squared(seq):
    for i in seq:
        yield i * i

chain = squared(integers())
print(list(chain))

def negated(seq):
    for i in seq:
        yield -i

chain = negated(squared(integers()))
print(list(chain))

# the processing happens one element at a time
for i in negated(squared(integers())):
    print(i)

# above is the same as:
integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)
print(negated)
print(list(negated))
