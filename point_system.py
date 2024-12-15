import FreeSimpleGUI as Gui
import edit_function,functions
import os, time


def point_system():
    score = functions.get_point()


    tasks = functions.get_tasks()

    Gui.theme("DarkPurple4")
    score_text = Gui.Text("Your score is: ",font=("",12))
    main_score = Gui.Text(score,font=("black",20),key="score")
    items  = Gui.Listbox(values=tasks,key="tasks",enable_events=True,size=(45,7))
    notice = Gui.Text("NOTE: relapse or failure in completion of goals will result in -10 points",font=("",7))
    minus_button = Gui.Button("Deduct 10 points", key="minus")
    edit_items_button = Gui.Button("Edit items", key="edit")
    lobs_button = Gui.Button("Logs", key="logs")


    window = Gui.Window("Discipline app", layout=[[score_text,main_score],[items,edit_items_button],[notice],[minus_button,lobs_button]],font=("Helvetica",10))

    while True:
        score = functions.get_point()
        int_score = int(score)


        event,value = window.read()
        print(event)
        print(value)

        match event:

            case Gui.WIN_CLOSED:
                break

            case "tasks":
                point = int(value["tasks"][0][-3:])
                int_score += point
                functions.write_point(str(int_score))
                window["score"].update(str(int_score))

                current_logs = functions.get_logs()
                new_log = f"log: {time.strftime("%b %d %Y, %H:%M:%S")} : {value["tasks"][0]}"
                current_logs.append(new_log)
                functions.write_logs(current_logs)

            case "minus":
                int_score -= 10
                functions.write_point(str(int_score))
                window["score"].update(str(int_score))


            case "edit":
                window.close()
                edit_function.edit_function()

            case "logs":
                filepath = "files/logs.txt"
                os.system(f"notepad {filepath}")


    window.close()