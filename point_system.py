import FreeSimpleGUI as Gui
import edit_function,functions


def point_system():
    score = functions.get_point()


    tasks = functions.get_tasks()

    Gui.theme("DarkPurple4")
    score_text = Gui.Text("Your score is: ",font=("",12))
    main_score = Gui.Text(score,font=("black",20),key="score")
    items  = Gui.Listbox(values=tasks,key="tasks",enable_events=True,size=(45,7))
    notice = Gui.Text("NOTE: relapse or failure in completion of goals will result in -10 points",font=("",7))
    minus_button = Gui.Button("deduct 10 points", key="minus")
    edit_items_button = Gui.Button("edit items", key="edit")


    window = Gui.Window("Discipline app", layout=[[score_text,main_score],[items,edit_items_button],[notice],[minus_button]],font=("Helvetica",10))

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

            case "minus":
                int_score -= 10
                functions.write_point(str(int_score))
                window["score"].update(str(int_score))


            case "edit":
                window.close()
                edit_function.edit_function()


    window.close()