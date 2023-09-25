from tkinter import *

root = Tk()
root.title('To Do List')
root.geometry("400x550+400+100")
root.config(bg='#32405b')
root.iconbitmap('logo.ico')

task_list=[]

def add():
    task=addingEntry.get()
    addingEntry.delete(0, END)
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'a') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open("tasklist.txt", "w")
        file.close()

heading=Label(root, text="Lista zadań", font=("Arial", 20, 'bold'), fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame=Frame(root, width=400, height=50, bg="white")
frame.place(x=0,y=100)

task=StringVar()
addingEntry = Entry(frame, bg="#FFF", width=18, font=("Arial", 25), bd=0)
addingEntry.place(x=10, y=7)
addingEntry.focus()


add_btn=Button(frame, text="+", width=6, font=("Arial", 16, 'bold'), bg="#00ff00", fg='#ffffff', command=add)
add_btn.place(x=300,y=4)

frame1=Frame(root,bd=3,  width=700, height=280, bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1, font=("arial",12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill= BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Delete_icon=PhotoImage(file="bin.png")
Button(root,text="Usuń", width=6, font=("Arial", 16, 'bold'), bg="#ff0000", fg='#ffffff', command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
