x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))
z = int(input("Enter value of z : "))
n = int(input("Enter value of n : "))

print("\nThe list elements are ", end=" ")
lst = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(lst)

# Using Nested Loops
print("The list elements are ", end=" ")
lst = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                lst.append([i, j, k])
print(lst)
