"""7.3 Emulating Switch/Case Statements With Dicts"""

# storing functions in list for later use
def myfunc(a, b):
    return a + b

func = [myfunc]
print(func[0])
print(func[0](2, 3))


# storing functions as dict values
def handle_a(): print("Handling a")
def handle_b(): print("Handling b")
def handle_default(): print("Handling default")

func_dict = {
    'cond_a': handle_a,
    'cond_b': handle_b,
}

cond = 'cond_a'
func_dict[cond]()

# handling default case
cond = 'cond_d'
func_dict.get(cond, handle_default)()

# another approach
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x -y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y

print(dispatch_if('mul', 2, 8))
print(dispatch_if('unknown', 2, 8)) # it returns None as default case

# same solution using lambdas
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict('mul', 2, 8))
print(dispatch_dict('unknown', 2, 8))

# question - why not to use directly x * y without lambda?
