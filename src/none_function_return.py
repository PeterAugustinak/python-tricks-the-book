"""3.6: Nothing to return here"""

# explicit None return -> best to use this to clear and concise definition
def foo1(value):
    if value:
        return value
    else:
        return None

# bare None return
def foo2(value):
    if value:
        return value
    else:
        return

# implicit None return
def foo3(value):
    if value:
        return value

# all three functions return the same -> None
print(f'Explicit: {type(foo1(0))}')
print(f'Bare: {type(foo2(0))}')
print(f'Implicit: {type(foo3(0))}')
