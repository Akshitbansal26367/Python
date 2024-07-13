# Printing patterns
n = int(input("Enter the value of n : "))
for i in range(0, n):
    for j in range(0, n):
        if i >= j:
            print("*", end="")
    print()

print()
n1 = int(input("Enter the value of n : "))
for i in range(1, n1 + 1):
    for j in range(1, n1 + 1):
        if i >= j:
            print(j, end="")
    print()

print()
n2 = int(input("Enter the value of n : "))
for i in range(0, n2):
    for j in range(0, n2):
        if i + j < n2:
            print(n2 - j, end="")
    print()

print()
for r in range(1, 6):
    for c in range(5, r - 1, -1):
        print(c, end="")
    print()

print()
for r in range(1, 6):
    for c in range(1, r + 1):
        print(c, end="")
    print()

print()
for r in range(1, 6):
    for c in range(r):
        print("*", end="")
    print()
