import time
import curses
from curses import wrapper
from text import get_random_text


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Test!")
    stdscr.addstr("\nPress any key to begin typing!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)

        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def type_text(stdscr):
    target_text = get_random_text()
    current_text = []

    wpm = 0
    start_time = time.time()

    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except curses.error:
            continue

        if ord(key) == 27:
            stdscr.nodelay(False)
            exit()
        elif key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            if len(current_text) < len(target_text):
                current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        type_text(stdscr)

        stdscr.addstr(3, 0, "Test completed!")
        stdscr.addstr(4, 0, "Press any key to try again or Esc to quit.")

        key = stdscr.getkey()

        if ord(key) == 27:
            exit()


wrapper(main)
