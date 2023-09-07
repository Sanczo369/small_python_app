from tkinter import *

root = Tk()
root.title('To Do List')
root.geometry("400x400")
root.config(bg='black')

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

addingEntry = Entry(root, bg="#FFF", width=19, font=("Arial", 25))
add_btn=Button(root, text="+", height=1, width=3, font=("Arial", 16, 'bold'), bg="#00ff00", fg='#ffffff')
addingEntry.grid(row=1, column=0)
add_btn.grid(row=1, column=1, padx=4)
root.mainloop()
