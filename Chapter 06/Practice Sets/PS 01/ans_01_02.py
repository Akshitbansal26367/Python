# Program to find the largest number in a list
# Program to find the smallest number in a list
l1 = []
n = int(input("Enter how many numbers in list : "))
print()
for i in range(n):
    a = int(input(f"Enter list item at index {i} : "))
    l1.append(a)
print("\nThe list is :", l1)
maxElement = l1[0]
minElement = l1[0]
for i in l1:
    if maxElement < i:
        maxElement = i
    elif minElement > i:
        minElement = i

print("\nThe maximum element in the list is", max(l1))
print("The maximum element in the list is", maxElement)
print("The minimum element in the list is", min(l1))
print("The minimum element in the list is", minElement)
