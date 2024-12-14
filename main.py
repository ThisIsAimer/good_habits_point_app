import FreeSimpleGUI as Gui

with open("files/points.txt","r") as file:
    score = file.read()
    int_score = int(score)

with open("files/tasks.txt","r") as file:
    tasks = file.readlines()

Gui.theme("DarkPurple4")
score_text = Gui.Text("Your score is: ",)
main_score = Gui.Text(score,font="B",key="score")
items  = Gui.Listbox(values=tasks,key="tasks",enable_events=True,size=(45,7))


window = Gui.Window("Discipline app", layout=[[score_text,main_score],[items]],font=("Helvetica",10))

while True:
    with open("files/points.txt", "r") as file:
        score = file.read()
        int_score = int(score)


    event,value = window.read()
    print(event)
    print(value)

    match event:

        case Gui.WIN_CLOSED:
            break

        case tasks:
            point = int(value["tasks"][0][-3:])
            int_score += point
            with open("files/points.txt", "w") as file:
                file.write(str(int_score))
            window["score"].update(str(int_score))
