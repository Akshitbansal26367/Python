# Program to count the number of even and odd numbers from a series of numbers
even_count = 0
odd_count = 0
a = int(input("Enter total terms to be added : "))

for i in range(a):
    n = int(input("Enter the number : "))
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("\nTotal Even numbers are", even_count)
print("Total Odd numbers are ", odd_count)
