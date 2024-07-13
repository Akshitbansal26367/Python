# Program to read 10 numbers from keyboard and find their sum and average
sum1 = 0
for i in range(1, 11):
    a = int(input("Enter number : "))
    sum1 = sum1 + a
print("Sum     :", sum1)
print("Average :", sum1 / 10)
