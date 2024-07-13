# Program to find the factors of an integer number
num = int(input("Enter the number : "))
i = 1
print("Factors of", num, "are :", end=" ")
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i = i + 1
