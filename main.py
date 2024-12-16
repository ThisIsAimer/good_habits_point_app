import point_system
import  FreeSimpleGUI as Gui
import os, functions

try:
    if not os.path.exists("files for discipline app/logs.txt"):
        with open("files for discipline app/logs.txt", "w") as file:
            pass
    if not os.path.exists("files for discipline app/points.txt"):
        with open("files for discipline app/points.txt", "w") as file:
            pass
    if not os.path.exists("files for discipline app/tasks.txt"):
        with open("files for discipline app/tasks.txt", "w") as file:
            pass

except FileNotFoundError:
    os.makedirs("files for discipline app")

    if not os.path.exists("files for discipline app/logs.txt"):
        with open("files for discipline app/logs.txt", "w") as file:
            pass
    if not os.path.exists("files for discipline app/points.txt"):
        with open("files for discipline app/points.txt", "w") as file:
            pass
    if not os.path.exists("files for discipline app/tasks.txt"):
        with open("files for discipline app/tasks.txt", "w") as file:
            pass

if functions.get_point() == "":
    functions.write_point(str(0))
    functions.write_logs("Starting power level: 0 \n")
    functions.write_tasks("this is example: 20\n")
else:
    pass

Gui.set_global_icon("icon.png")
point_system.point_system()


# run the command
# pyinstaller --onefile --windowed --clean .\main.py
# after installing pyinstaller