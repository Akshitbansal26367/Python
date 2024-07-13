h = "Hello"
# h[1] = "H" invalid because string data type is immutable i.e. variable value cannot be changed
print(h)

l1 = [10, 20, 30]
l1[0] = 50  # valid because list is mutable i.e. variable value can be changed
print(l1, type(l1))
