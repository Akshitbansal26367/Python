# Program to count the occurrences of each word in a given sentence
main_string = str(input("Enter the string : "))
str1 = str(input("Enter string to be found : "))
count = 0

words = main_string.split()

for i in words:
    if i == str1:
        count += 1
print("The total occurrences of", str1, "in", main_string, "is", count, "times")
