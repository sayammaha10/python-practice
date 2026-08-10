try:
    with open("story.txt", "r") as f:
        story = f.read()
except FileNotFoundError:
    print(
        "The story file could not be found.\n"
        "Please make sure 'story.txt' is in the same folder as the program."
    )
    exit()

words = []
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]

        if word not in words:
            words.append(word)

        start_of_word = -1

print("\nWelcome to Mad Libs!")
print("Fill in the blanks to create your story.\n")

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print("\nYour completed story:\n")
print(story)
