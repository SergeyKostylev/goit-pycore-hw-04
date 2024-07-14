import re
import definitions
from pathlib import Path
from modules.helpers.helpers import handle_error, get_lines_from_file

def total_salary(path: str):
    valid_salaries_amount = 0
    sum = 0
    try:

        for line in get_lines_from_file(path):
            curren_salary = get_salary_from_line(line)

            if curren_salary is None:
                continue

            valid_salaries_amount += 1
            sum += curren_salary

    except FileNotFoundError:
        handle_error(f"File '{path}' not found.")
    except IOError as err:
        handle_error(f"File error '{path}'.\nError: {err.strerror}")

    return (
        sum,
        round(sum / valid_salaries_amount, 2)
    )


def get_salary_from_line(line: str):
    line = line.rstrip()

    if line == '':
        handle_error(f"Data in the a line is empty")
        return None

    salary_value = re.findall('.*\,(\d+)$', line)

    if len(salary_value) != 1:
        handle_error(f"Salary was not found be found in line '{line}'")

    return int(salary_value[0])




if __name__ == '__main__':
    path_as_string = Path.joinpath(definitions.ROOT_DIR, 'src', 'file_task1.txt')

    total, average = total_salary(path_as_string)

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")