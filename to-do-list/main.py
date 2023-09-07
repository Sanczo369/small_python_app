from tkinter import *

root = Tk()
root.title('To Do List')
root.geometry("400x400")
root.config(bg='black')

addingEntry = Entry(root, bg="#FFF", width=19, font=("Arial", 25))
add_btn=Button(root, text="+", height=1, width=3, font=("Arial", 16, 'bold'), bg="#00ff00", fg='#ffffff')
addingEntry.grid(row=1, column=0)
add_btn.grid(row=1, column=1, padx=4)
root.mainloop()
