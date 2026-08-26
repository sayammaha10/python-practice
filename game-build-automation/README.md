# Game Build Automation

A Python automation tool that finds Python game projects, copies them into a build directory, and packages them into standalone `.exe` files using PyInstaller.

## Features

- Automatically finds folders using the `_game` naming pattern
- Copies game projects into a separate build directory
- Builds Python games into executable files using PyInstaller
- Generates a `metadata.json` file containing build information
- Supports building multiple games in a single process

## Project Structure

Example:

```text
game-build-automation/
│
├── builder.py
├── games/
│   ├── number_guessing_game/
│   │   └── main.py
│   │
│   ├── pig_dice_game/
│   │   └── main.py
│   │
│   └── rock_paper_scissors_game/
│       └── main.py
│
└── builds/
```

## Installation

Install PyInstaller:

```bash
pip install pyinstaller
```

## Usage

Run the builder with:

```bash
python builder.py <source_folder> <target_folder>
```

Example:

```bash
python builder.py games builds
```

## How It Works

The builder:

1. Searches the source directory for folders containing `_game`
2. Copies each game into the target build directory
3. Finds the game's `main.py`
4. Runs PyInstaller to create an executable
5. Creates a `metadata.json` file with build details

## Output

After building:

```text
builds/
│
├── number_guessing/
│   └── dist/
│       └── number_guessing.exe
│
├── pig_dice/
│   └── dist/
│       └── pig_dice.exe
│
├── rock_paper_scissors/
│   └── dist/
│       └── rock_paper_scissors.exe
│
└── metadata.json
```

---

This project was created as a practice project to improve my Python skills and learn more about automation, file handling, and working with external tools. Building this helped me understand how Python can be used to automate repetitive tasks and create useful scripts.

Thanks for checking out this project!
