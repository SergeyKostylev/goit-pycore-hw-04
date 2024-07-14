import sys

import definitions
from pathlib import Path
from colorama import Fore

DIR_COLOR = Fore.GREEN
FILE_COLOR = Fore.BLUE
LEVEL_TREE_SPACE = ' '


def write_tree(path: Path):
    check_dir_exists(path)
    render_line(path, [])  # Render requested directory
    process_folder(path, [])


def process_folder(path: Path, level_signs):
    sortedList = sorted(path.iterdir(),
                        key=lambda x: (not x.is_dir(), x.name))  # I think need to show folders before files

    length = len(sortedList)
    for num, objectTree in enumerate(sortedList):
        isLastFile = num == length - 1

        render_line(objectTree, level_signs + [isLastFile])

        if objectTree.is_dir():
            process_folder(objectTree, level_signs + [isLastFile])


def render_line(path_object: Path, level_signs):
    color = DIR_COLOR if path_object.is_dir() else FILE_COLOR
    postfix = "/" if path_object.is_dir() else ''

    prefix = ""
    length = len(level_signs)

    if length == 1:
        prefix = " ┗ " if level_signs[0] is True else " ┣ "

    elif length > 1:
        for num, boolValue in enumerate(level_signs):
            if num == length - 1:
                part = " ┗ " if boolValue is True else " ┣ "
                prefix += part
            elif boolValue is True:
                prefix = prefix + "   "
            else:
                prefix = prefix + " ┃ "

    prefix = Fore.RESET + prefix
    file_str = f"{path_object.name}{postfix}"

    print(f"{prefix}{color}{file_str}")


def is_directory_without_files(path: Path) -> bool:
    if not path.is_dir():
        raise ValueError(f"Logic Exception. Path '{path}' is not a directory")

    for file in path.iterdir():
        if file.is_file():
            return True

    return False


def check_dir_exists(path):
    if not path.is_dir():
        raise ValueError(f"Given path {path} is not a directory.")


if __name__ == '__main__':
    path = definitions.ROOT_DIR.joinpath('src').absolute()
    if len(sys.argv) >= 2:
        path = Path(sys.argv[1]).absolute()
    write_tree(path)
