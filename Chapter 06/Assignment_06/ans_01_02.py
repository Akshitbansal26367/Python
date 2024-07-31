# Sum all items in the list
# Multiply all items in the list
lst = []
n = int(input("Enter the number of elements in the list : "))
print()
for i in range(n):
    a = int(input(f"Enter element at index {i} : "))
    lst.append(a)
print()
print("The list is", lst)
sumList = 0
mulList = 1
for a in lst:
    sumList += a
    mulList *= a
print()
print("Sum of all list elements are", sumList)
print("Multiplication of all list elements are", mulList)
