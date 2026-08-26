import random


def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value, max_value)

    return value


print("=" * 30)
print("Welcome to The Game of Pig!")
print("=" * 30)

while True:
    players = input("Enter the number of players (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("The number of players must be between 2 and 4.")
    else:
        print("Please enter a valid number.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn!")
        print("Current total score:", player_scores[player_index])
        current_score = 0

        while True:
            should_roll = input("\nRoll the die? (y/n): ").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1! Your turn is over.")
                break
            else:
                current_score += value
                print(f"You rolled a {value}.")

            print("Current turn score:", current_score)

        player_scores[player_index] += current_score
        print("Total score:", player_scores[player_index])

winning_score = max(player_scores)

if player_scores.count(winning_score) > 1:
    print(f"\nIt's a tie! Each tied player scored {winning_score}!")
else:
    winning_index = player_scores.index(winning_score)
    print(
        f"\nPlayer {winning_index + 1} wins with a total score of {winning_score}!")
