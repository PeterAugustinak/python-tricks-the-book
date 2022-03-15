"""5.7 Priority Queues"""

"""list - Maintaining a Manually Sorted Queue"""

q = []
q.append((2, 'code'))
q.append((1, 'eat'))
q.append((3, 'sleep'))

# NOTE: Remember to re-sort every time a new element is inserted
q.sort()

while q:
    next_item = q.pop()
    print(next_item)

"""heapq - List-Based Binary Heaps"""
print()

import heapq

h = []
heapq.heappush(h, (2, 'code'))
heapq.heappush(h, (1, 'eat'))
heapq.heappush(h, (3, 'sleep'))

while h:
    next_item = heapq.heappop(h)
    print(next_item)

"""PREFERRED: queue.PriorityQueue - Beautiful Priority Queues"""
print()

from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2, 'code'))
pq.put((1, 'eat'))
pq.put((3, 'sleep'))

while not pq.empty():
    next_item = pq.get()
    print(next_item)
