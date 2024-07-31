# Program to check if a given key already exists in a dictionary
d = {1: 1, 2: 4, 3: 9, 4: 16}
n = int(input("Enter the key : "))
# Method 1
if n in d:
    print("\nKey already exists")
else:
    print("\nKey does not exists")

# Method 2
flag = False
for a in d:
    if a == n:
        flag = True
        break
if flag:
    print("Key already exists")
else:
    print("Key does not exists")
