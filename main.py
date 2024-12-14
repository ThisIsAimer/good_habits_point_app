import FreeSimpleGUI as Gui

with open("files/points.txt","r") as file:
    score = file.read()
    int_score = int(score)

with open("files/tasks.txt","r") as file:
    tasks = file.readlines()

Gui.theme("DarkPurple4")
score_text = Gui.Text("Your score is: ",font=("",12))
main_score = Gui.Text(score,font=("black",20),key="score")
items  = Gui.Listbox(values=tasks,key="tasks",enable_events=True,size=(45,7))
notice = Gui.Text("NOTE: relapse or failure in completion of goals will result in -10 points",font=("",7))
minus_button = Gui.Button("deduct 10 points", key="minus")


window = Gui.Window("Discipline app", layout=[[score_text,main_score],[items],[notice],[minus_button]],font=("Helvetica",10))

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

        case "tasks":
            point = int(value["tasks"][0][-3:])
            int_score += point
            with open("files/points.txt", "w") as file:
                file.write(str(int_score))
            window["score"].update(str(int_score))

        case "minus":
            int_score -= 10
            with open("files/points.txt", "w") as file:
                file.write(str(int_score))
            window["score"].update(str(int_score))