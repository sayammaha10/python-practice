import random

print("\n=== Number Guessing Game ===")
print("Choose the maximum number, and I'll pick a number between 1 and that maximum.")
print("Your goal is to guess the number in as few attempts as possible.\n")


while True:
    top_of_range = input("Enter the maximum number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range > 1:
            break
        else:
            print("The maximum number must be greater than 1.")
    else:
        print("Invalid input. Please enter a number greater than 1.")

random_number = random.randint(1, top_of_range)
guesses = 0

print(f"\nGreat! I've chosen a number between 1 and {top_of_range}.")
print("Let's see if you can guess it!\n")

while True:
    guesses += 1
    user_guess = input("Guess the number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess < 1 or user_guess > top_of_range:
            print(f"Please enter a number between 1 and {top_of_range}.")
            continue
    else:
        print("Invalid input. Please enter a valid number.")
        continue

    if user_guess == random_number:
        print("\nCongratulations! You guessed the correct number!")
        break
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

print(
    f"\nYou guessed the number in {guesses} {'guess' if guesses == 1 else 'guesses'}!")
print("Thanks for playing!")
