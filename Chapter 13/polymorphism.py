"""Polymorphism means same function name (but different signatures) being uses for different types"""
"""Polymorphism is of two types function overloading and function overriding"""

# The example of polymorphism is len() which calculates the length of various objects like string, list, tuple

str1 = "Hello"
print("The length of string is", len(str1))

lst = [10, 20, 30, 40, 50, 60]
print("The length of list is", len(lst))


def product(a, b, c=1):
    return a * b * c


class Child:
    def display_info(self):
        print("I am Child Class")


class Parent(Child):
    def display_info(self):
        # use super() to call the method from the Child class
        super().display_info()
        print("I am Parent Class")


# Here c is optional, so this works like overloading
print("The product of 2 and 3 is", product(2, 3))  # Call product(a, b)
print("The product of 2, 3 and 5 is", product(2, 3, 5))  # Call product(a, b, c)
print()

# Function Overriding
obj = Parent()
obj.display_info()
