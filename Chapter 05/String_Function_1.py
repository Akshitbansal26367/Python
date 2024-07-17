# len() function returns the number of character in a string
# count() function returns the number of times a substring has appeared in the string
# lower() function returns a string where all characters are lower case
# upper() function returns a string where all characters are upper case
# capitalize() function returns a string where the first character is upper case and rest is lower case
# title() function returns a string where the first character in every word is upper case
# find() function finds the first occurrence of the specified substring. The method will return -1 if the value is not
# found
# index() function finds the first occurrence of the specified substring. The method raises an exception if the value is
# not found
# strip() removes spaces at the beginning and at the end of the string
# lstrip() removes spaces to the left of the string
# rstrip() removes any white spaces of the string
# split a string into a list where each word is a list item. You can specify the seperator, default seperator
# is any whitespaces

w = "Welcome to Wscubetech"
print("Length of string is", len(w))
print("Occurrence of e in the string is", w.count('e'))
print("String in lower characters is", w.lower())
print("String in Upper characters is", w.upper())
print("String in Capitalised form is", w.capitalize())
print("String in Titled form is", w.title())
print("First Occurrence of t in string is", w.find('t'))
print("First Occurrence of t in string is", w.index('t'))

z = "                   Welcome to my class    "
print("Strip() function use", z.strip())
print("lStrip() function use", z.lstrip())

print("rStrip() function use", end="")
s = z.rstrip()
print(s, end="")
print("Hello")
print("List is", w.split())
print("List is", w.split('e'))
