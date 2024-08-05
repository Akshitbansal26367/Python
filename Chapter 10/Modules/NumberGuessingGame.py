import random

computer_number = random.randint(1, 100)
count = 0
flag = False
while not flag:
    n = int(input("Guess the number between 1 and 100 : "))
    count += 1
    if n > computer_number:
        print("Your guess is too high!!!\n")
    elif n < computer_number:
        print("Your guess is too low!!!\n")
    else:
        print("\nYou guessed the right number in", count, "attempts")
        flag = True
