import FreeSimpleGUI as Gui

with open("files/points.txt","r") as file:
    score = file.read()

with open("files/tasks.txt","r") as file:
    tasks = file.readlines()

Gui.theme("DarkPurple4")
score_text = Gui.Text("Your score is: ",)
main_score = Gui.Text(score,font="B")
items  = Gui.Listbox(values=tasks,key="tasks",enable_events=True,size=(45,7))


window = Gui.Window("My To-Do App", layout=[[score_text,main_score],[items]],font=("Helvetica",10))

while True:
    event,value = window.read()
    print(event)
    print(value)

    match event:

        case Gui.WIN_CLOSED:
            break