# Program to count occurrence of a given character in String
s = str(input("Enter the string : "))
s1 = str(input("Enter the character whose occurrence to be searched : "))
count = 0
for a in s:
    if a == s1:
        count += 1
print("The occurrence of character", s1, "in the string is", count, "times")
print("The occurrence of character", s1, "in the string is", s.count(s1), "times")
