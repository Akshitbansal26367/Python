# Program to find perfect number
# Program to make a simple calculator
def perfect_number(num):
    sum_factor = 0
    for i in range(1, num):
        if num % i == 0:
            sum_factor += i
    if sum_factor == num:
        print("Yes, it is perfect number")
    else:
        print("No, it is not a perfect number")


def simple_calc(num1, num2, operation):
    if operation == "+":
        print("Sum is", num1 + num2)
    elif operation == "-":
        print("Subtraction of", num1, "and", num2, "is", num1 - num2)
    elif operation == "*":
        print("Multiplication is", num1 * num2)
    elif operation == "/":
        print("Division is", num1 / num2)
    else:
        print("Not Valid Operation...")


n1 = int(input("Enter the number : "))
perfect_number(n1)

n1 = int(input("\nEnter the number1 : "))
n2 = int(input("Enter the number2 : "))
opr = input("Select the operation(+, -, *, /) : ")
simple_calc(n1, n2, opr)
