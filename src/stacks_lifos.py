"""5.5 Stacks (LIFOs)"""

"""list - Simple, Build-In Stacks"""

s = []
s.append('eat')
s.append('sleep')
s.append('code')

print(s)
p1 = s.pop()
print(p1)
p2 = s.pop()
print(p2)
p3 = s.pop()
print(p3)
try:
    s.pop()
except IndexError as e:
    print(e)

"""collections.deque - Fast & Robust Stacks"""
print()

from collections import deque
d = deque()
d.append('eat')
d.append('sleep')
d.append('code')

print(d)
d1 = d.pop()
print(d1)
d2 = d.pop()
print(d2)
d3 = d.pop()
print(d3)
try:
    d.pop()
except IndexError as e:
    print(e)

"""queue.LifoQueue - Locking Semantics for Parallel Computing"""
print()

from queue import LifoQueue
l = LifoQueue()
l.put('eat')
l.put('sleep')
l.put('code')

print(l)
l1 = l.get()
print(l1)
l2 = l.get()
print(l2)
l3 = l.get()
print(l3)
l4 = l.get_nowait()
print(l4)
