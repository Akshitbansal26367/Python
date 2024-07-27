# zip() function is used to combine two or more lists into a single iterable, where elements from corresponding
# positions are paired together

l1 = [10, 20, 40, 50]
l2 = [3, 4, 77, 88]
t = len(l1)
for a, b in zip(l1, l2):
    print("Element of list l1 is", a, "and element of list l2 is", b)

print()
for i in range(t):
    print("Element of list l1 is", l1[i], "and element of list l2 is", l2[i])
