"""6.1 Writing Pythonic loops"""

my_items = ['a', 'b', 'c']

# C style
i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

# using range
for i in range(len(my_items)):
    print(my_items[i])

# Pythonic
for item in my_items:
    print(item)

# with counter
for i, item in enumerate(my_items, 1):
    print(f'{i}: {item}')

# looping over dicts
emails = {
    'Bob': 'bob@example.com',
    'Alice': 'alice@example.com',
}

for name, email in emails.items():
    print(f'{name} -> {email}')
