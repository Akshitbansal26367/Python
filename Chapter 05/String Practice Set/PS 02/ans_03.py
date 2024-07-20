# Program to swap comma and dot in a string
str1 = str(input("Enter the string : "))
print("The new string is ", end="")
for a in str1:
    if a == '.':
        a = ','
    elif a == ',':
        a = '.'
    else:
        a = a
    print(a, end="")
