from tkinter import *

root = Tk()
root.title('To Do List')
root.geometry("400x650+400+100")
root.config(bg='black')
root.iconbitmap('logo.ico')

task_list=[]

value=1
def add():
    global value
    text=addingEntry.get()
    addingEntry.delete(0, END)
    lab=Label(root, width=18, text=str(value)+". "+text, font=("Arial", 25))

    del_btn = Button(root, text="-", height=1, width=3, font=("Arial", 16, 'bold'), bg="#ff0000", fg='#ffffff')
    lab.grid(row=1 + value, column=0)
    del_btn.grid(row=1 + value, column=1)
    value+=1

heading=Label(root, text="Lista zadań", font=("Arial", 20, 'bold'), fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame=Frame(root, width=400, height=50, bg="white")
frame.place(x=0,y=100)

addingEntry=StringVar()
addingEntry = Entry(frame, bg="#FFF", width=18, font=("Arial", 25), bd=0)
addingEntry.place(x=10, y=7)
addingEntry.focus()


add_btn=Button(frame, text="+", width=6, font=("Arial", 16, 'bold'), bg="#00ff00", fg='#ffffff')
add_btn.place(x=300,y=4)


root.mainloop()
