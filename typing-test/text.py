import random

TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect, so keep typing every day.",
    "Python is a powerful and easy to learn programming language.",
    "Typing faster comes with consistency and accuracy.",
    "Small improvements every day lead to big results over time.",
    "Learning by building projects is one of the best ways to improve.",
    "Debugging is an important part of every programmer's journey.",
    "Success is the sum of small efforts repeated day after day."
]


def get_random_text():
    return random.choice(TEXTS)
