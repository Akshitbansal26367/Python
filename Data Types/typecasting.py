a = "10"
n = int(a)  # explicit type conversion from str to int
print(a, "is of type", type(a))
b = int(20.5)  # explicit type conversion from float to int
print(b, "is of type", type(b))

a = 20
print(a, "is of type", type(a))
a = float(20)  # explicit type conversion from int to float
print(a, "is of type", type(a))

n1 = eval("20.5")
print(n1, "is of type", type(n1))

str1 = 20
str2 = "Hello"
print(str(str1) + str2)  # explicit type conversion from int to string
print("List is ", list(str2))  # explicit type conversion from string to list

t = (10, 20, 30, 40)
l1 = list(t)
print("List is", l1)  # explicit type conversion from tuple to list

l1[1] = 50
print("List is", l1)

t = tuple(l1)  # explicit type conversion from list to tuple
print("Tuple is", t)

d = dict(a=10, b=20, c=30)
print("Dictionary is", d)

s = [10, 20, 30, 40, 50, 10, 30, 40, 10]
l3 = set(s)  # explicit type conversion from list to set
print("Set is", l3)
print("List is", list(l3))
