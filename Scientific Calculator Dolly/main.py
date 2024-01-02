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

    def butn(self):
        self.plus = Button(self.window, text="+", width=3, font=("arial", 15, "bold"), fg="red", bg="#262626",
                           activebackground="#262626",
                           command=lambda: self.opr("+"), relief=RAISED, bd=3)
        self.plus.place(x=535, y=240)

        self.subs = Button(self.window, text="-", width=3, font=("arial", 15, "bold"), fg="red", bg="#262626",
                           activebackground="#262626",
                           command=lambda: self.opr("-"), relief=RAISED, bd=3)
        self.subs.place(x=535, y=300)

        self.mul = Button(self.window, text="X", width=3, font=("arial", 15, "bold"), fg="red", bg="#262626",
                          activebackground="#262626",
                          command=lambda: self.opr("X"), relief=RAISED, bd=3)
        self.mul.place(x=535, y=360)

        self.div = Button(self.window, text="/", width=3, font=("arial", 15, "bold"), fg="red", bg="#262626",
                          activebackground="#262626",
                          command=lambda: self.opr("/"), relief=RAISED, bd=3)
        self.div.place(x=535, y=420)

        self.rad = Button(self.window, text="rad", width=3, font=("arial", 15, "bold"), fg="red", bg="#262626",
                          activebackground="#262626",
                          command=lambda: self.opr("Radian"), relief=RAISED, bd=3)
        self.rad.place(x=440, y=360)

        self.reci = Button(self.window, text="1/x", width=3, font=("arial", 15, "bold"), fg="red", bg="#262626",
                           activebackground="#262626",
                           command=lambda: self.opr("Reciprocal"), relief=RAISED, bd=3)
        self.reci.place(x=440, y=420)

    def widget(self):
        Label(self.window,text="Scientific Calculator Dolly",font=("arial",25,"bold","italic"),fg="orange",bg="#141414").place(x=100,y=5)

        self.result_name = Label(self.window, text="Result: ", width=8, font=("arial", 16, "bold", "italic"),
                                  fg="#00FF00",bg="#141414")
        self.result_name.place(x=40, y=65)

        self.result = Entry(self.window,font=("Helvetica",20,"bold","italic"),textvar=self.text_value, bd=5, relief=SUNKEN, disabledbackground="#3d3d3d", disabledforeground="gold", state=DISABLED)
        self.result.place(x=140,y=55)

        self.butn()
        self.take_input()

    def take_input(self):
        Label(self.window, text="Number 1 ", width=8, font=("arial", 15, "bold", "italic"), bg="#141414",
              fg="#00FF00").place(x=20, y=175)

        self.number1 = Entry(self.window, width=8, bg="#3d3d3d", font=("arial", 20, "bold", "italic"),
                             insertbackground="gold",
                             fg="gold", bd=3, relief=SUNKEN)
        self.number1.place(x=130, y=170)

        self.number1.focus()

        Label(self.window, text="Number 2 ", width=8, font=("arial", 16, "bold", "italic"),
              fg="#00FF00", bg="#141414").place(x=340, y=175)

        self.number2 = Entry(self.window, width=8, bg="#3d3d3d", font=("arial", 20, "bold", "italic"),
                             insertbackground="gold",
                             fg="gold", relief=SUNKEN, bd=4)
        self.number2.place(x=455, y=170)

        self.operator_name = Label(self.window, text="Operation ", width=12, font=("arial", 17, "bold", "italic"),
                                   bg="#141414", fg="#d96b6b")
        self.operator_name.place(x=100, y=120)

        self.operator = Entry(self.window, width=12, font=("arial", 20, "bold", "italic"), disabledbackground="#3d3d3d",
                              disabledforeground="gold",
                              state="disable", textvar=self.textoperator, bd=5, relief=SUNKEN)
        self.operator.place(x=250, y=117)

    def reset_now(self):
        self.textoperator.set(" ")
        self.text_value.set(" ")

    def tata(self):
        self.decision = messagebox.askyesno("Conformation","Do you want to exit right now?")
        if self.decision>0:
            window.destroy()
        else:
            pass

    def opr(self,work):
        self.work = work
        self.textoperator.set(self.work)
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