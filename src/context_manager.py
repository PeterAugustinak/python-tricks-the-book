# not using context manager - example with opening file

f = open('hello.txt', 'w')
try:
    f.write('hello world')
finally:
    f.close()

# using context manager
with open('hello.txt', 'w'):
    f.write()
# f.close() is called automatically leaving with block

# implementing context manager on class level
class ManagedFile:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# usage
with ManagedFile('hello.txt') as f:
    f.write('hello world')

# implementing context manager on function level with property
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

# usage
with managed_file('hello.txt') as f:
    f.write('hello world')


# another example
class Indenter:

    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print_text(self, text):
        print(' ' * self.level + text)

with Indenter() as indent:
    indent.print_text('level1')
    with indent:
        indent.print_text('level2')
        with indent:
            indent.print_text('level3')
    indent.print_text('back to level1')
