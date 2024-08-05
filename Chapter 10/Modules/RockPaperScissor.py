import random

print("Press 1 for Rock")
print("Press 2 for Scissor")
print("Press 3 for Paper")
print()
user_input = int(input("Do you want to play the game(1 for Yes, 0 for No) ? "))

lst = [1, 2, 3]
user_cnt = 0
cmp_cnt = 0

if user_input == 1:
    rounds = 5
    while rounds > 0:
        game = int(input("\nEnter the choice : (1 for Rock, 2 for Scissor, 3 for Paper) : "))
        if game not in [1, 2, 3]:
            print("Invalid Input. Please enter 1, 2, or 3")
            continue

        cmp_choice = random.choice(lst)
        print(f"Computer choice : {cmp_choice}")
        print(f"User choice     : {game}")

        if (game == 1 and cmp_choice == 2) or (game == 2 and cmp_choice == 3) or (game == 3 and cmp_choice == 1):
            user_cnt += 1
            print("User Won the round!!!")
        elif game == cmp_choice:
            print("This round is drawn!!!")
        else:
            cmp_cnt += 1
            print("Computer won this round!!!")
        rounds -= 1

    print(f"\nFinal Score - User : {user_cnt}, Computer : {cmp_cnt}")

    if user_cnt > cmp_cnt:
        print("User won the game!!!")
    elif user_cnt < cmp_cnt:
        print("Computer won the game!!!")
    else:
        print("This game is drawn!!!")
else:
    print("Thank you for playing!!!")
