"""Effective functions"""

def yell(text):
    return text.upper() + '!'

print(yell('hello'))

"""Adding function to another variable"""
bark = yell
print(bark("woof"))

# original variable can be deleted then, but function definition still
# existing in bark
del yell
try:
    print(yell("Hello?"))
except NameError:
    print("The 'yel' var does not exist anymore.")
    print(bark("Hey!"))

# but as the python adding name space into the function in time of creation:
print(bark.__name__)

"""Functions as items in lst"""
funcs = [bark, str.lower, str.capitalize]
for f in funcs:
    print(f, f('hey there'))

# you don't need to add func to var and you can cal; it directly
print(funcs[0]('called directly'))

"""Func inc func"""
"""HIGH-ORDER FUNC (for bark and whisper)"""
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

def whisper(text):
    return text.lower() + '...'

greet(bark)
greet(whisper)

# map (higher-order function)
g = [map(f, ['hello', 'hey', 'hi']) for f in [bark, whisper]]
for map in g:
    print(list(map))

"""INNER FUNC (nested)"""
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

print(speak('Hello world'))

# depending on arg, main function selects and return one of the inner
# functions to caller
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    # not call the inner func, just return them based on arg
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func(0.3))
print(get_speak_func(0.7))
speak_func = get_speak_func(0.3)
print(speak_func('Calling inner function returned'))

"""LEXICAL CLOSURES / CLOSURES - capturing local state"""
def get_speak_func_state(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func_state('Calling closure func with captured local state',
                           0.7)())

"""One arg captured"""
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))

"""Making callable object - instance of class behaves like callable func"""
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
print(plus_3(4))

"""Check if object is callable"""
print(callable(plus_3))
print(callable(4))

