l1 = [10, 20, 30, 50, 60]
print("The given list is ", end="")
for n in range(len(l1)):
    print(l1[n], end=" ", sep=" ")

print("\nThe given list is ", end="")
for i in l1:
    print(i, end=" ", sep=" ")

# Printing list in reverse
print("\nThe reversed list is ", end="")
for n in range(len(l1) - 1, -1, -1):
    print(l1[n], end=" ", sep=" ")
