# Program to check whether a given key already exists in a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
a = int(input("Enter the key : "))

if a in d:
    print("Key already exists in dictionary")
else:
    print("Key does not exists in dictionary")
