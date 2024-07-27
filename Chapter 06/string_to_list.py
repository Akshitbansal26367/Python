n = input("Enter any string : ")
print("The list is", n.split())  # This will convert the string into the list
print()
n = int(input("Enter the number of inputs : "))
l1 = []
for i in range(n):
    string_input = input("Enter the string : ")
    l1.append(string_input)
print("The string is", l1)
