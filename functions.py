def get_tasks(filepath="files/tasks.txt"):
    with open(filepath, "r") as _file:
        _items = _file.readlines()
        return _items

def write_tasks(items_, filepath ="files/tasks.txt"):
    with open(filepath, "w", ) as _file:
        _file.writelines(items_)

def get_point(filepath="files/points.txt"):
    with open(filepath, "r") as _file:
        _items = _file.read()
        return _items
def write_point(items_, filepath ="files/points.txt"):
    with open(filepath, "w", ) as _file:
        _file.write(items_)