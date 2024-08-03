# The math.ceil() method rounds a number upto the nearest integer.
# The math.floor() method rounds a number down to the nearest integer.
# The math.fabs() method returns the absolute value of a number, as a float.
# math.factorial() method returns the factorial of a number. This method only accepts positive integers.
# math.fsum() method returns the floating sum of all items in any iterable (tuples, arrays, lists, etc.).
# math.sqrt() method returns the square root of a number.
import math

x = 10.1
print("The ceil value of", x, "is", math.ceil(x))
print("The floor value of", x, "is", math.floor(x))

x = -30
print("The absolute value of", x, "is", abs(x))
print("The absolute value of", x, "is", math.fabs(x))
print("Factorial of number 6 is", math.factorial(6))

l1 = [10, 20, 30, 40]
print("Sum of the list elements is", int(math.fsum(l1)))
print("The square root of number 9 is", math.sqrt(9))
