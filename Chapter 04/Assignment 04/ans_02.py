# Program that accepts a word from the user and reverse it
a = str(input("Enter the string : "))
print("The reversed string is :", end=" ")
for i in range(len(a) - 1, -1, - 1):
    print(a[i], end="")
