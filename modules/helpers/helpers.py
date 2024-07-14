import syslog


# TODO: separate methods to diffetern py files


def handle_error(message: str):
    # print(message)
    syslog.syslog(syslog.LOG_INFO, message)


def get_lines_from_file(file_path: str, format=None):
    with open(file_path, 'r', encoding=format) as fs:
        return fs.readlines()
