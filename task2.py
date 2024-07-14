import definitions
from pathlib import Path
from modules.helpers.helpers import handle_error, get_lines_from_file

DATA_SEPARATOR = ','


def get_cats_info(path: str):
    cats_data = []
    try:
        for line in get_lines_from_file(path, 'utf-8'):

            cat = get_prepared_cat_info(line)
            cats_data.append(cat) if cat is not None else None # I don't know it is good idea to use ternary here

    except FileNotFoundError:
        handle_error(f"File '{path}' not found.")
    except IOError as err:
        handle_error(f"File error '{path}'.\nError: {err.strerror}")

    return cats_data


def get_prepared_cat_info(raw_str: str):
    parts = raw_str.split(DATA_SEPARATOR)
    if len(parts) != 3:
        handle_error("Invalid data in raw line.")
        return None

    return {
        'id': parts[0],
        'name': parts[1],
        'age': int(parts[2].replace("\n", "")),  # we can don't use replace
    }


if __name__ == '__main__':
    path_as_string = Path.joinpath(definitions.ROOT_DIR, 'src', 'file_task2.txt')

    res = get_cats_info(path_as_string)
    print(res)
