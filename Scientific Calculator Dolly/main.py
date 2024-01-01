from tkinter import *
from tkinter import messagebox
import math

class Calculator:
    def __init__(self,window):
        self.window=window
        self.text_value = StringVar()
        self.textoperator = StringVar()
        self.textoperator2 = StringVar()
        self.fact = 1
        self.widget()

    def widget(self):
        Label(self.window,text="Scientific Calculator Dolly",font=("arial",25,"bold","italic"),fg="orange",bg="#141414").place(x=100,y=5)

        self.result_name = Label(self.window, text="Result: ", width=8, font=("arial", 16, "bold", "italic"),
                                  fg="#00FF00",bg="#141414")
        self.result_name.place(x=40, y=65)

        self.result = Entry(self.window,font=("Helvetica",20,"bold","italic"),textvar=self.text_value, bd=5, relief=SUNKEN, disabledbackground="#3d3d3d", disabledforeground="gold", state=DISABLED)
        self.result.place(x=140,y=55)

        self.butn()
        self.take_input()
if __name__ == '__main__':
    window = Tk()
    window.title("Smart Scientific Calculator")
    window.config(bg='#141414')
    window.iconbitmap("calculator.ico")
    window.geometry("600x620")
    window.maxsize(600,620)
    window.minsize(600,620)
    Calculator(window)
    window.mainloop()