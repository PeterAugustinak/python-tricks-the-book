"""2.5 A shocking truth about String formatting"""

errno = 50159747054
name = 'Bob'

"""'Old style' string formatting"""
string = "Hello %s!" %name
print(string)

string1 = "Hey %s, there is a 0x%x error!" % (name, errno)
print(string1)

string2 = "Hey %(name)s, there is a 0x%(errno)x error!" % {"name": name,
                                                           "errno": errno}
print(string2)

"""'New style' string formatting"""
string3 = "Hello, {}!".format(name)
print(string3)

string4 = "Hey {name}, there is a 0x{errno:x} error!".format(name=name,
                                                             errno=errno)
print(string4)

"""Literal String interpolation"""
string5 = f"Hello, {name}!"
print(string5)

string6 = f"Hey {name}, there is a {errno:#x} error!"
print(string6)

"""Template strings -> use for user input"""
from string import Template
t = Template("Hey, $name!")
string7 = t.substitute(name=name)
print(string7)

string = "Hey $name, there is a $error error!"
string8 = Template(string).substitute(name=name, error=hex(errno))
print(string8)

"""Why to use Template?"""
SECRET = "this-is-a-secret"

# problem
class Error:
    def __init__(self):
        pass

err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))

# solution
user_input = '${error.__init__.__globals__[SECRET]'
print(Template(user_input).substitute(error=err))
