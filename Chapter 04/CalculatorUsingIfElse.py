a = int(input("Enter a : "))
b = int(input("Enter b : "))
opr = input("Enter the operation (+, -, *, /) : ")

if opr == '+':
    print("Sum of a and b is", a + b)
elif opr == '-':
    print("Subtraction of a and b is", a - b)
elif opr == '*':
    print("Multiplication of a and b is", a * b)

elif opr == '/':
    print("Division of a and b is", a / b)
else:
    print("Operation not valid")
