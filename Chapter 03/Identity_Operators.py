"""
is
is not
"""
x = 5
print(type(x) is int)  # same as print(type(x) == int) True
print(type(x) is float)  # False

a = 5.2
b = 7.2
c = 5
print(type(a) is type(b))  # True
print(type(a) is not type(b))  # same as print(type(x) != type(b)) False
print(type(c) is not type(b))  # True

c = 10
d = 20
print(a is not b)  # True
