"""List Slicing Tricks and the Sushi Operator"""

# [start:stop:step]
lst = [1, 2, 3, 4, 5]
print(lst)

print(lst[1:4:1])
print(lst[1:3])
print(lst[::2])

# list reverse
print(lst[::-1])
r = list(reversed(lst))
print(r)
lst.reverse()
print(lst)

# del / clear
del lst[:]
print(lst)
lst = [1, 2, 3, 4, 5]
lst.clear()
print(lst)

# create new list
lst = [1, 2, 3, 4, 5]

original_lst = lst
lst[:] = [7, 8, 9]
print(lst)
print(original_lst)
print(original_lst is lst)

# list copy
copied_lst = lst[:]
print(copied_lst)
print(copied_lst is lst)
