""""Decorators"""

"""Abstract example of decorator"""
def null_decorator(func):
    return func

def greet():
    return "Hello!"

greet = null_decorator(greet)
print(greet())

@null_decorator
def greet_decorated_null():
    return "Hello!"

print(greet())

# greet = null_decorator(greet) == @null_decorator

"""Working decorator with wrapper"""
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet_decorated_upper():
    return "Hello!"

print(greet())

print(greet)
print(null_decorator(greet_decorated_null))
print(uppercase(greet_decorated_upper))

"""Multiple decorators"""
print()
def strong(func):
    def wrapper():
        return f'<strong>{func()}</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper

@strong
@emphasis
def greet_multiply_decorated():
    return "Hello!"

print(greet_multiply_decorated())

# means order of decorators is from bottom to up, same as:
#strong(emphasis(greet_multiply_decorated)

"""Decorators with arguments"""
print()

def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}() with {args}, {kwargs}")
        original_result = func(*args, **kwargs)
        print(f"TRACE: {func.__name__}() returned {original_result!r}")
        return original_result
    return wrapper

@trace
def say(name, line):
    return f"{name}: {line}"

print(say("Jane", "Hello world!"))

"""Debugging decorators"""
print()
def greet_deb():
    """Returns a friendly greeting"""
    return "Hello!"

decor_greet_deb = uppercase(greet_deb)

print(greet_deb.__name__)
print(greet_deb.__doc__)

# once func is decorated, it does not return metadata from this func,
# but from wrapper
print(decor_greet_deb.__name__)
print(decor_greet_deb.__doc__)

# it can be solved by using functools - best practice to use it like this
# for every wrapper
import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet_debug_functools():
    """Return a friendly greeting (functool)"""
    return "Hello!"

print(greet_debug_functools.__name__)
print(greet_debug_functools.__doc__)
