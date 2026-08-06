import time

# fmt: off
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
# fmt: on

CLEAR = "\033[2J"
RETURN = "\033[H"
CLEAR_LINE = "\033[K"


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


def timer(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed <= seconds:
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{RETURN}=== Countdown Timer ===")
        print(f"Time Remaining: {minutes_left:02d}:{seconds_left:02d}")

        time.sleep(1)
        time_elapsed += 1

    print(f"{RETURN}=== Countdown Timer ===")
    print(f"{CLEAR_LINE}Time's up!")

    play_sound()


while True:
    try:
        print("\n=== Countdown Timer ===")

        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))

        if minutes < 0 or seconds < 0:
            print("\nMinutes and seconds cannot be negative.")
            continue

        break
    except ValueError:
        print("\nPlease enter whole numbers only.")

total_seconds = minutes * 60 + seconds
timer(total_seconds)
