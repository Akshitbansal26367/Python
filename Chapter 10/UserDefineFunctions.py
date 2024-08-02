# A function is a block of statement which can be used repetitively in a program. It saves the time of developer.
# Functions that we define ourselves to do certain specific task are referred to as user - defined functions.
# Functions that readily come with python are called built-in functions.
def show_data():
    print("My name is Akshit Bansal")


def sum_data(a, b):
    print("Sum of", a, "and", b, "is", a + b)


def multiply(a, b):
    return a * b


def add(a, b=1):
    print("Sum is", a + b)


show_data()
sum_data(10, 20)
result = multiply(10, 20)
print("Multiplication is", result)
add(12)
add(19, 20)
