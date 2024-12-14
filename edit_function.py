import functions
import FreeSimpleGUI as Gui
import point_system

def edit_function():
    Gui.theme("DarkPurple4")
    tasks = functions.get_tasks()
    label = Gui.Text("Edit your activities")
    input_box = Gui.InputText(tooltip="Enter task",key="task")
    add_button = Gui.Button("Add")
    list_box = Gui.Listbox(values=tasks,key="tasks",enable_events=True,size=(45,7))
    edit_button = Gui.Button("Edit")
    complete_button = Gui.Button("remove")
    done_button = Gui.Button("Done")

    window = Gui.Window("Discipline app", layout=[[label], [input_box, add_button],[list_box,edit_button,complete_button],[done_button]],font=("Helvetica",10))
    while True:
        tasks = functions.get_tasks()

        event,value = window.read()



        match event:

            case Gui.WIN_CLOSED:
                break

            case "Add":
                new_task = value["task"] + "\n"
                tasks.append(new_task)
                functions.write_tasks(tasks)
                window['tasks'].update(tasks)

            case "Edit":
                try:
                    edited_task = value["tasks"][0]
                    index = tasks.index(edited_task)
                    new_task = value["task"]
                    tasks[index] = new_task
                    functions.write_tasks(tasks)
                    window['tasks'].update(tasks)
                except IndexError:
                    Gui.popup("please select an item to edit",font=("Helvetica",10))

            case "tasks":
                window["task"].update(value= value["tasks"][0])

            case "remove":
                try:
                    complete_task = value["tasks"][0]
                    tasks.remove(complete_task)
                    functions.write_tasks(tasks)
                    window["tasks"].update(tasks)
                    window["task"].update(value="")
                except IndexError:
                    Gui.popup("please select an item to complete",font=("Helvetica",10))

            case "Done":
                window.close()
                point_system.point_system()