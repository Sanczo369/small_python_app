from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")


def onClick(number):
    current = e_result.get()
    e_result.delete(0, END)
    e_result.insert(0, current+str(number))


def Clear():
    e_result.delete(0, END)

def btn_add():
    global equation
    global number_one
    equation = "+"
    number_one = float(e_result.get())
    e_result.delete(0, END)


def btn_sub():
    global equation
    global number_one
    equation = "-"
    number_one = float(e_result.get())
    e_result.delete(0, END)


def btn_div():
    global equation
    global number_one
    equation = "/"
    number_one = float(e_result.get())
    e_result.delete(0, END)


def btn_multi():
    global equation
    global number_one
    equation = "*"
    number_one = float(e_result.get())
    e_result.delete(0, END)

# Define Element
e_result = Entry(root, bg="#FFF", width=5, font=("Arial", 20))
btn_1 = Button(root, height=2, width=5, text="1")
btn_2 = Button(root, height=2, width=5, text="2")
btn_3 = Button(root, height=2, width=5, text="3")
btn_4 = Button(root, height=2, width=5, text="4")
btn_5 = Button(root, height=2, width=5, text="5")
btn_6 = Button(root, height=2, width=5, text="6")
btn_7 = Button(root, height=2, width=5, text="7")
btn_8 = Button(root, height=2, width=5, text="8")
btn_9 = Button(root, height=2, width=5, text="9")
btn_0 = Button(root, height=2, width=5, text="0")
btn_00 = Button(root, height=2, width=5, text="00")
btn_add = Button(root, height=2, width=5, text="+")
btn_sub = Button(root, height=2, width=5, text="-")
btn_div = Button(root, height=2, width=5, text="/")
btn_multi = Button(root, height=2, width=5, text="*")
btn_clear = Button(root, height=2, width=5, text="C")
btn_off = Button(root, height=2, width=5, text="OFF")
btn_result = Button(root, height=2, width=5, text="=")
btn_proc = Button(root, height=2, width=5, text="%")
btn_dot = Button(root, height=2, width=5, text=",")

# Element Position

e_result.grid(row=0, column=0, columnspan=5, sticky=W+E)

btn_off.grid(row=2, column=1)
btn_clear.grid(row=2, column=2)
btn_proc.grid(row=2, column=3)
btn_div.grid(row=2, column=4)

btn_7.grid(row=3, column=1)
btn_8.grid(row=3, column=2)
btn_9.grid(row=3, column=3)
btn_multi.grid(row=3, column=4)

btn_4.grid(row=4, column=1)
btn_5.grid(row=4, column=2)
btn_6.grid(row=4, column=3)
btn_sub.grid(row=4, column=4)

btn_1.grid(row=5, column=1)
btn_2.grid(row=5, column=2)
btn_3.grid(row=5, column=3)
btn_add.grid(row=5, column=4)

btn_0.grid(row=6, column=1)
btn_00.grid(row=6, column=2)
btn_dot.grid(row=6, column=3)
btn_result.grid(row=6, column=4)

if __name__ == '__main__':
    root.mainloop()
