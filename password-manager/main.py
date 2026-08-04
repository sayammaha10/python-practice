import os
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("key.key", "rb") as file:
        return file.read()


if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)


def view():
    if not os.path.exists("passwords.txt"):
        print("\nNo passwords have been saved yet.\n")
        return

    print("\nSaved Passwords")
    print("-" * 40)

    with open("passwords.txt", "r") as f:
        for line in f:
            data = line.rstrip()
            user, pwd = data.split("|")
            print(
                f"Account: {user}\nPassword: {fer.decrypt(pwd.encode()).decode()}\n")


def add():
    print("\nAdd a New Password")
    print("-" * 40)

    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

    print("\nPassword saved successfully.\n")


while True:
    print("-" * 40)
    mode = input(
        "Choose an option:\n"
        "  • add  - Save a new password\n"
        "  • view - View saved passwords\n"
        "  • q    - Quit\n\n"
        "Enter your choice: "
    ).lower()

    if mode == "q":
        print("\nGoodbye!")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("\nInvalid option. Please enter 'add', 'view', or 'q'.\n")
