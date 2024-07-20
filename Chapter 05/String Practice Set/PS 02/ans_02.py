# Program to remove duplicate characters from the string
str1 = str(input("Enter the string : "))
f = ""
for a in str1:
    if str1.count(a) >= 1 and a not in f:
        f = f + a
print("The unique characters string is", f)
