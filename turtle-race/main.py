import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow",
          "black", "purple", "pink", "brown", "cyan"]


def get_number_of_turtles():
    while True:
        turtles = input("\nEnter the number of turtles to race (2-10): ")
        if turtles.isdigit():
            turtles = int(turtles)
            if 2 <= turtles <= 10:
                return turtles
            else:
                print("Please choose a number between 2 and 10.")
        else:
            print("Invalid input. Please enter a whole number.")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")


print("=" * 35)
print("Welcome to the Turtle Race!")
print("=" * 35)
print("Choose how many turtles will compete.")
print("The first turtle to reach the finish line wins!")

turtles = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:turtles]

winner = race(colors)

print("=" * 35)
print(f"The winner is the {winner} turtle!")
print("=" * 35)

time.sleep(5)
