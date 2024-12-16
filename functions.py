def get_tasks():
    with open("files for discipline app/tasks.txt", "r") as _file:
        _items = _file.readlines()
        return _items


def write_tasks(items_):
    with open("files for discipline app/tasks.txt", "w", ) as _file:
        _file.writelines(items_)


def get_point():
    with open("files for discipline app/points.txt", "r") as _file:
        _items = _file.read()
        return _items


def write_point(items_):
    with open("files for discipline app/points.txt", "w") as _file:
        _file.write(items_)


def get_logs():
    with open("files for discipline app/logs.txt", "r") as _file:
        _items = _file.readlines()
        return _items

def write_logs(items_):
    with open("files for discipline app/logs.txt", "w", ) as _file:
        _file.writelines(items_)