# Program to count number of vowels and consonants in the string
s1 = str(input("Enter the string : "))
v = "aeiouAEIOU"
vCount = 0
cCount = 0
for i in s1:
    if i in v:
        vCount += 1
    elif i.isalpha() and i not in v:
        cCount += 1
print("Vowels are     :", vCount)
print("Consonants are :", cCount)
