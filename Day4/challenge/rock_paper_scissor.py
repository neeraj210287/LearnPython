import random


valid_choices = ["Rock", "Paper", "Scissor"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 <= user_choice <= 2 :
    print(valid_choices[user_choice])
    computer_choice = random.randint(0,2)
    print(f"Computer chose:\n{valid_choices[computer_choice]}")
    if user_choice == 0:
        if computer_choice == 2:
            print("You win")
        elif computer_choice == 1:
            print("You lose")
        else:
            print("It's a draw")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win")
        elif computer_choice == 2:
            print("You lose")
        else:
            print("It's a draw")
    else:
        if computer_choice == 1:
            print("You win")
        elif computer_choice == 0:
            print("You lose")
        else:
            print("It's a draw")
else:
    print("Invalid User Input")

