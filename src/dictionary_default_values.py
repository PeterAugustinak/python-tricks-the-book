"""7.1 Dictionary default values"""

name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert'
}

def greeting(userid):
    return f'Hi {name_for_userid[userid]}'

print(greeting(382))
try:
    print(greeting(434343))
except KeyError as e:
    print(e)

# if else solution
def greeting(userid):
    if userid in name_for_userid:
        return f'Hi {name_for_userid[userid]}'
    else:
        return "Hi there"

print(greeting(382))
print(greeting(434343))

# try/except block
def greeting(userid):
    try:
        return f'Hi {name_for_userid[userid]}'
    except KeyError:
        return "Hi there"

print(greeting(382))
print(greeting(434343))

# using .get() with default argument
def greeting(userid):
    return f'Hi {name_for_userid.get(userid, "there")}'

print(greeting(382))
print(greeting(434343))
