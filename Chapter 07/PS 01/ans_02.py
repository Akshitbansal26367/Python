# Program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square
# of keys
print("Dictionary is ", end="")
d = {a: a * a for a in range(1, 16)}
print(d)

print("\nDictionary is ", end="")
for a in d:
    d[a] = a * a
print(d)
