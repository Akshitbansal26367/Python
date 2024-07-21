# Program to find duplicate characters in a String
str1 = str(input("Enter the string : "))
str2 = ""
print("The duplicate characters are ", end="")
for i in str1:
    if str1.count(i) > 1 and i not in str2:
        str2 = str2 + i
print(str2, end=" ")
