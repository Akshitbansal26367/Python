import calculator


# Find the output of the above program
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


# function where keys in dictionary are from 1 to 20 (both included) and the values are square of keys
def dictionary():
    dic = {i: i ** 2 for i in range(1, 21)}
    return dic


print("The maximum number is", maximum(2, 3))
print()

# Module to make a simple calculator
print("Sum of 10 and 4 is", calculator.add(10, 4))
print("Multiply of 10 and 4 is", calculator.multiply(10, 4))
print("Subtraction of 10 and 4 is", calculator.subtract(10, 4))
print("Division of 10 and 4 is", calculator.divide(10, 4))
print()
print("The dictionary is", dictionary())
print("The value of dictionary is ", dictionary().values())
