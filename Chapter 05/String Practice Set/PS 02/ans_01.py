# Program to print first non - repeated character from string
s1 = str(input("Enter the string : "))
for i in s1:
    if s1.count(i) == 1:
        print("The first non repeated character is", i)
        break
