# Program to randomly generate a list with 5 numbers, which are divisible by 5 and 7, between 1 and 1000 inclusive
import random

l1 = []
while True:
    a = random.randint(1, 1000)
    if a % 5 == 0 and a % 7 == 0:
        l1.append(a)
    if len(l1) == 5:
        break
print("The list is", l1)
