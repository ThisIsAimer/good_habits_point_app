import FreeSimpleGUI as Gui
import os, functions, point_system

from functions import write_logs

def set_points():
    Gui.theme("DarkPurple4")
    score = functions.get_point()
    score_text = Gui.Text("Your score is: ",font=("",12))
    main_score = Gui.Text(score,font=("black",20),key="score")
    input_box = Gui.InputText(tooltip="enter a value", key="value")
    set_button = Gui.Button("Set points")
    done_button = Gui.Button("Done")
    log_button = Gui.Button("Logs")
    reset_logs_button = Gui.Button("Reset logs")

    window = Gui.Window("Discipline app", layout=[[score_text,main_score], [input_box, set_button], [done_button, log_button, reset_logs_button]], font=("Helvetica", 10))

    while True:
        event, value = window.read()

        match event:
            case Gui.WIN_CLOSED:
                    break

            case "Set points":
                try:
                    int_val = int(value["value"])
                    functions.write_point(str(int_val))

                    logs = functions.get_logs()
                    new_log = f"Starting power level: {int_val}"+"\n"
                    logs.append(new_log)
                    functions.write_logs(logs)

                    window["score"].update(str(int_val))
                except ValueError:
                    Gui.popup("please enter a valid number", font=("Helvetica", 10))

            case "Logs":
                filepath = "files for discipline app/logs.txt"
                os.system(f"notepad {filepath}")

            case "Reset logs":
                log = ""
                write_logs(log)

            case "Done":
                window.close()
                point_system.point_system()
