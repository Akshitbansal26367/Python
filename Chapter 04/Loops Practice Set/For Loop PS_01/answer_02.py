# Program to count the occurrences of any word in a given sentence
s1 = str(input("Enter the main string : "))
l1 = s1.split()  # Will convert string into list with splitting " "
print("List is", l1)
s2 = str(input("Enter the string to be searched: "))
count = 0
"""for s1 in range(1, len(s1)):
    if s1 == s2:
        count += 1
print("The occurrence of the word", s2, "is", count, "times")"""
for a in l1:
    if a == s2:
        count += 1
print("Occurrence of", s2, "is", count, "times")
