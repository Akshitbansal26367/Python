# Program to replace the last element in a list with another list
l1 = []
l2 = [5, "Hello", "Love"]
n = int(input("Enter number of elements : "))
print()
for i in range(0, n):
    a = int(input(f"Enter element at index {i} : "))
    l1.append(a)
print("\nThe given list is", l1)

'''del l1[-1]
l1.extend(l2)
print("\nThe new list is", l1)'''

l1[-1:] = l2
print("The new list is", l1)
