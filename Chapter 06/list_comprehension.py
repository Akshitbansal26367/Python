# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
l1 = []
for a in range(1, 11):
    l1.append(a)
print("l1 list is", l1)

# List Comprehension
n = [m for m in range(1, 11) if m % 2 == 0]
print("n list is ", n)

s = "Hello"
d = [g for g in s]
print("d list is", d)
