import queue
import time
import curses
from curses import wrapper

maze = [
    ["#", "#", "#", "#", "#", "O", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    # Store the current position and the path taken to reach it.
    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = {start_pos}

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        # Stop when the destination is reached.
        if maze[row][col] == end:
            return path

        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r, c = neighbour
            if maze[r][c] == "#":
                continue

            # Add the new position and its path to the queue.
            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)


def find_neighbours(maze, row, col):
    neighbours = []

    # Check the cell above.
    if row > 0:
        neighbours.append((row - 1, col))

    # Check the cell below.
    if row + 1 < len(maze):
        neighbours.append((row + 1, col))

    # Check the cell to the left.
    if col > 0:
        neighbours.append((row, col - 1))

    # Check the cell to the right.
    if col + 1 < len(maze):
        neighbours.append((row, col + 1))

    return neighbours


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()


wrapper(main)
