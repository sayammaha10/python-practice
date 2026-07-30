from questions import questions

print("\nWelcome to my quiz!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    print("\nThat's too bad! Maybe next time. See you later!")
    quit()

print("\nOkay! Let's play :)")

score = 0

for question in questions:
    answer = input("\n" + question["question"] + " ")

    if answer.lower() == question["answer"]:
        print("\nCorrect!")
        score += 1
    else:
        print("\nIncorrect!")

print(f"\nYou got {score} out of {len(questions)} questions correct!")
print(f"Your score is {(score / len(questions)) * 100:.0f}%.")
