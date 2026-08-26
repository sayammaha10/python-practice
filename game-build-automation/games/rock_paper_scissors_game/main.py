import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    print()
    user_input = input(
        "Choose rock, paper, or scissors (or 'q' to quit): ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("The computer chose", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
    elif user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

print("\nGame Over!")
print("You won", user_wins, "game(s).")
print("The computer won", computer_wins, "game(s).")
print("Thanks for playing!")
