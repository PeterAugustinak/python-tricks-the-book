"""8.3 Peeking Behind the Bytecode Curtain"""

def greet(name):
    return "Hello, " + name + "!"

print(greet("Guido"))

co_code = greet.__code__.co_code
print(co_code)

co_const = greet.__code__.co_consts
print(co_const)

co_vars = greet.__code__.co_varnames
print(co_vars)

# bytecode disassembler
import dis
dis_code = dis.dis(greet)
print(dis_code)
