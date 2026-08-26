import json
import shutil
import sys
from pathlib import Path
from subprocess import run

GAME_PATTERN = "_game"
PYTHON_EXTENSION = ".py"
PYINSTALLER_COMMAND = [
    sys.executable,
    "-m",
    "PyInstaller",
    "--onefile",
    # "--noconsole"
]


def find_games(source):
    games = []

    for path in source.rglob("*"):
        if path.is_dir() and GAME_PATTERN in path.name.lower():
            games.append(path)

    return games


def get_game_names(paths):
    names = []

    for path in paths:
        name = path.name.replace(GAME_PATTERN, "")
        names.append(name)

    return names


def create_directory(path):
    path.mkdir(parents=True, exist_ok=True)


def copy_game(source, destination):
    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)


def find_entry_file(game_path):
    for file in game_path.iterdir():
        if file.suffix == PYTHON_EXTENSION:
            return file.name

    return None


def compile_game(game_path, entry_file):
    command = PYINSTALLER_COMMAND + [
        "--name",
        game_path.name,
        entry_file
    ]

    result = run(
        command,
        cwd=game_path,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"Built: {game_path.name}")
    else:
        print(f"Failed: {game_path.name}")
        print(result.stderr)

    return result.returncode == 0


def create_metadata(path, games):
    data = {
        "numberOfGames": len(games),
        "games": games
    }

    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def build_games(source, target):
    game_paths = find_games(source)
    game_names = get_game_names(game_paths)

    create_directory(target)

    metadata_games = []

    for source_path, game_name in zip(game_paths, game_names):
        destination = target / game_name

        copy_game(source_path, destination)

        entry_file = find_entry_file(destination)

        if entry_file is None:
            print(f"No python file found in {game_name}")
            continue

        if compile_game(destination, entry_file):
            metadata_games.append({
                "name": game_name,
                "executable": f"{game_name}.exe"
            })

    create_metadata(target / "metadata.json", metadata_games)

    print("Build complete!")


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python builder.py <source> <target>"
        )
        return

    source = Path(sys.argv[1])
    target = Path(sys.argv[2])

    if not source.exists():
        print("Source folder does not exist")
        return

    build_games(source, target)


if __name__ == "__main__":
    main()
