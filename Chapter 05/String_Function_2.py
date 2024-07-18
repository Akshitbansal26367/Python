# swapcase() function returns a string where all the uppercase letters are lower case and vice versa
# replace() function replaces a specified phrase with another specified phrase
# isalpha() function returns True if all the characters are alphabet letters (a-z)
# isdigit(), isnumeric() function returns True if all the characters are digits, otherwise False.
# isalnum() function returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and
# numbers (0-9).
# The isspace() function returns True if all the characters in a string are whitespaces, otherwise False.
# The islower() function returns True if all the characters are in lower case, otherwise False.
# The istitle() function returns True if all words in a text start with an upper case letter, AND the rest of the
# word are lower case letters, otherwise False.
# The isupper() function returns True if all the characters are in upper case, otherwise False.
# The startswith() function returns True if the string starts with the specified value, otherwise False.
# The endswith() function returns True if the string ends with the specified value, otherwise False.
w = "WeLCome tO WScuBeTeCh"
print("The swap case string is", w.swapcase())
print(w.replace('tO', "Python"))
print(w.isspace())  # False
print(w.islower())  # False
print(w.istitle())  # False
print(w.startswith('WeLCome'))  # True
print(w.endswith('WScuBeTeCh'))  # True
print(w.endswith('W', 10, 12))  # True

z = "WelcomeEveryone"
print(z.isalpha())  # True
print(z.isdigit())  # False
print(z.isalnum())  # True

a = "     "
print(a.isspace())  # True

b = "WELCOME EVERYONE"
print(b.isupper())  # True
