import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_colors():
    colors = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        colors.append(color)

    return colors


def guess_color():
    while True:
        guess = input("\nEnter your guess (e.g. R G B Y): ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Invalid guess. Please enter exactly {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Please use only: R G B Y W O.")
                break
        else:
            break

    return guess


def check_color(guess, current_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in current_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, current_color in zip(guess, current_code):
        if guess_color == current_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, current_color in zip(guess, current_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print("=" * 40)
    print("WELCOME TO MASTERMIND")
    print("=" * 40)
    print(f"Guess the {CODE_LENGTH}-color code.")
    print(f"You have {TRIES} attempts.")
    print("Colors: R G B Y W O")
    print("=" * 40)

    color_code = generate_colors()

    for attempts in range(1, TRIES + 1):
        guess = guess_color()
        correct_pos, incorrect_pos = check_color(guess, color_code)

        if correct_pos == CODE_LENGTH:
            print(f"\nCorrect! You cracked the code in {attempts} tries.")
            break

        print(
            f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")
    else:
        print("\nOut of tries! The code was:", *color_code)


if __name__ == "__main__":
    game()
