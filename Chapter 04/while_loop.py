# Table of any number
table = int(input("Enter the value : "))

a = 1
while a <= 10:
    print(table, "x", a, "=", table * a)
    a += 1

# Sum of all even numbers from 1 to 100 including both
i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total = total + i
    i = i + 1
print("\nSum of even numbers from 1 to 100 including both is", total)

# Print a particular pattern
k = 1
while k <= 10:
    if k == 2:
        print(k, "WsCube Tech")
    elif k == 3:
        print(k, "IIP Academy")
    else:
        print(k, "IIP")
    k += 1
