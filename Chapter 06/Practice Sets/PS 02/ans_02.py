# Program to create a list by concatenating a given list which ranges goes from 1 to n
n = int(input("Enter the number of elements : "))
newList = []

for a in range(n + 1):
    newList.append("p" + str(a))
    newList.append("q" + str(a))
print("The list is", newList)
