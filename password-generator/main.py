import secrets
import string


def generate_password(min_length, include_numbers=True, include_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    characters = letters
    if include_numbers:
        characters += digits
    if include_symbols:
        characters += symbols

    password = ""
    meets_criteria = False
    has_number = False
    has_symbol = False

    while not meets_criteria or len(password) < min_length:
        new_char = secrets.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in symbols:
            has_symbol = True

        meets_criteria = True
        if include_numbers:
            meets_criteria = has_number
        if include_symbols:
            meets_criteria = meets_criteria and has_symbol

    return password


print("=" * 35)
print("Password Generator")
print("=" * 35)

while True:
    while True:
        try:
            min_length = int(input("\nEnter the minimum length (minimum 8): "))

            if min_length < 8:
                print("Password length must be at least 8 characters.\n")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    while True:
        include_numbers = input("Include numbers? (y/n): ").lower()

        if include_numbers in ("y", "n"):
            include_numbers = include_numbers == "y"
            break

        print("Please enter 'y' for yes or 'n' for no.\n")

    while True:
        include_symbols = input("Include special characters? (y/n): ").lower()

        if include_symbols in ("y", "n"):
            include_symbols = include_symbols == "y"
            break

        print("Please enter 'y' for yes or 'n' for no.\n")

    password = generate_password(min_length, include_numbers, include_symbols)

    print("=" * 35)
    print("Your generated password:")
    print(password)
    print("=" * 35)

    while True:
        generate_again = input("Generate another password? (y/n): ").lower()

        if generate_again in ("y", "n"):
            break

        print("Please enter 'y' for yes or 'n' for no.\n")

    if generate_again == "n":
        print("\nThank you for using Password Generator!")
        break
