# Write a program that accepts a word from the user and reverse it
s = str(input("Enter the string : "))
print("The reversed string is : ", end="")
for a in range(len(s) - 1, -1, -1):
    print(s[a], end="")
