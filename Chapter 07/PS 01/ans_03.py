# Program to get the key, value and item in a dictionary
d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("The keys are ", d.keys())
print("The keys are ", end="\t")

for i in d.keys():
    print(i, end="\t")
print()

print("\nThe values are ", d.values())
print("The values are ", end="\t")

for j in d.values():
    print(j, end="\t")

print("\n\nThe key:value pair are ", d.items())
print("The key:value pair are ", end="\t")

for i, j in d.items():
    print(i, ":", j, end="\t")
