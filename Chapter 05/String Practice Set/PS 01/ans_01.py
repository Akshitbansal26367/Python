# Program to check if a string is palindrome or not
str1 = str(input("Enter the string : "))
str2 = ""

for i in range(len(str1) - 1, -1, -1):
    str2 = str2 + str1[i]
if str1 == str2:
    print("String is palindrome")
else:
    print("String is not palindrome")

# another logic
"""s = str(input("Enter the string : "))
v = s[-1::-1]
if s == v:
    print("Yes")
else:
    print("No")"""
