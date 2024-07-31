# Program to get the largest number from a list
# Program to get the smallest number from a list
lst = []
n = int(input("Enter the number of elements in the list : "))
print()
for i in range(n):
    a = int(input(f"Enter element at index {i} : "))
    lst.append(a)
print()
print("The list is", lst)
largeList = lst[0]
smallList = lst[0]

for element in lst:
    if element > largeList:
        largeList = element
    elif element < smallList:
        smallList = element
print("The largest element is", largeList)
print("The smallest element is", smallList)
