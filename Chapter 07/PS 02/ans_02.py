# Program to concatenate following dictionary to create a new one
d1 = {1: 10, 2: 20}
print("Dictionary d1 is", d1)

d2 = {5: 50, 6: 60}
print("Dictionary d2 is", d2)

d1.update(d2)
print("Updated Dictionary d1 is", d1)
