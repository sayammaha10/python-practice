import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 6,
    "C": 9,
    "D": 12
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def display_slot_machine(columns):
    print("┌───┬───┬───┐")

    for row in range(len(columns[0])):
        print("│", end=" ")
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" │ ")
            else:
                print(column[row], end=" │")
        print()

        if row != len(columns[0]) - 1:
            print("├───┼───┼───┤")

    print("└───┴───┴───┘")


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit must be greater than $0.")
        else:
            print("Invalid input. Please enter a whole number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f"How many lines would you like to bet on? (1-{MAX_LINES}): ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please choose between 1 and {MAX_LINES} lines.")
        else:
            print("Invalid input. Please enter a whole number.")

    return lines


def get_bet():
    while True:
        amount = input("Enter your bet per line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a whole number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Insufficient balance. You have ${balance}, but your total bet is ${total_bet}."
            )
        else:
            break

    print("\n=== Bet Summary ===")
    print(f"Lines      : {lines}")
    print(f"Bet / Line : ${bet}")
    print(f"Total Bet  : ${total_bet}")

    input("\nPress Enter to spin...")

    print("\n=== Slot Machine ===")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    display_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print("\n=== Results ===")

    if winnings > 0:
        print(f"Congratulations! You won ${winnings}.")
        print("Winning line(s):", *winning_lines)
    else:
        print("No winning lines this round.")

    return winnings - total_bet


def main():
    print("=" * 35)
    print("PYTHON SLOT MACHINE")
    print("=" * 35)
    print(f"Bet on up to {MAX_LINES} lines.")
    print(f"Minimum bet: ${MIN_BET}")
    print(f"Maximum bet: ${MAX_BET}\n")

    balance = deposit()

    while True:
        print("\n" + "=" * 35)
        print(f"Current Balance: ${balance}")
        print("=" * 35)

        play = input(
            "Press Enter to play or type 'q' to quit: ").strip().lower()

        if play == "q":
            break

        balance += spin(balance)

    print("\nThanks for playing!")
    print(f"You cashed out with ${balance}.")


main()
