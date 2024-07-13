# Print table of any number
table = int(input("Enter the number : "))
for a in range(1, 11):
    print(table, "x", a, "=", table * a)

# Print even number from 1 to 11 including both
for a in range(2, 11, 2):
    print("Even number = ", a)

# Extracting each character from the string
h = "Welcome to WsCube Tech"
for a in h:
    print(a)

# Extracting each element from the list
l1 = [1, 2, 3, 4, 5]
for n in l1:
    print(n)

# Print square of 1 to 10 numbers including both
for i in range(1, 11):
    print(i, "x", i, "=", i * i)

# Find the count of sub_string in main_string
main_string = "Welcome to WsCube Tech,Jodhpur"
sub_string = "e"
count = 0
for a in main_string:
    if a == sub_string:
        count += 1
print("The count of", sub_string, "in", main_string, "is", count)
