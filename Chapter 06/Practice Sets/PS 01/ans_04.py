# Program to remove duplicates from a list
l1 = []
newList = []
n = int(input("Enter number of items in list : "))
print()

for i in range(n):
    a = int(input(f"Enter element at index {i} : "))
    l1.append(a)
print("\nThe list is", l1)

for a in l1:
    if a not in newList:
        newList.append(a)
print("The unique elements list is", newList)
