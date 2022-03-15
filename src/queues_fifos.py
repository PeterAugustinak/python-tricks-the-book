"""5.6 Queues (FIFOs)"""


"""list - Terribly Slow Queues"""
q = []
q.append('eat')
q.append('sleep')
q.append('code')

print(q)

# Careful: This is slow
q1 = q.pop(0)
print(q1)

"""collections.deque - Fast & Robust Queues"""
print()

from collections import deque
d = deque()
d.append('eat')
d.append('sleep')
d.append('code')

print(d)

d1 = d.popleft()
print(d1)
d2 = d.popleft()
print(d2)
d2 = d.popleft()
print(d2)
try:
    d.popleft()
except IndexError as e:
    print(e)

"""queue.Queue - Locking Semantics for Parallel Computing"""
print()

from queue import Queue
q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')

print(q)

q1 = q.get()
print(q1)
q2 = q.get()
print(q2)
q3 = q.get()
print(q3)

# q.get_nowait()

"""multiprocessing.Queue - Shared Job Queues"""
print()

from multiprocessing import Queue
mq= Queue()
mq.put('eat')
mq.put('sleep')
mq.put('code')

print(q)

mq1 = mq.get()
print(mq1)
mq2 = mq.get()
print(mq2)
mq3 = mq.get()
print(mq3)
