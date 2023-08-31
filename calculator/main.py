from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")
root.overrideredirect(True)

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

def btn_proc():
    global number_one
    number_two = float(e_result.get())
    resul = (number_one*number_two)/100
    e_result.delete(0, END)
    e_result.insert(0, str(resul))

def btn_multi():
    global equation
    global number_one
    equation = "*"
    number_one = float(e_result.get())
    e_result.delete(0, END)

def btn_result():
    global number_one
    number_two = e_result.get()
    e_result.delete(0, END)
    if equation == "+":
        e_result.insert(0, str(round(number_one + float(number_two), 13)))
    elif equation == "-":
        e_result.insert(0, str(round(number_one - float(number_two), 13)))
    elif equation == "*":
        e_result.insert(0, str(round(number_one * float(number_two), 13)))
    elif equation == "/":
        e_result.insert(0, str(round(number_one / float(number_two), 13)))


# Define Element
e_result = Entry(root, bg="#FFF", width=5, font=("Arial", 25))

# Define Styles
button_style = {
    "height": 2,
    "width": 5,
    "font": ("Arial", 16),
    "bg": "#E0E0E0",
    "activebackground": "#C0C0C0",
    "borderwidth": 1,
    "relief": "solid"
}

# Define Element
btn_1 = Button(root, text="1", command=lambda: onClick(1), **button_style)
btn_2 = Button(root, text="2", command=lambda: onClick(2), **button_style)
btn_3 = Button(root, text="3", command=lambda: onClick(3), **button_style)
btn_4 = Button(root, text="4", command=lambda: onClick(4), **button_style)
btn_5 = Button(root, text="5", command=lambda: onClick(5), **button_style)
btn_6 = Button(root, text="6", command=lambda: onClick(6), **button_style)
btn_7 = Button(root, text="7", command=lambda: onClick(7), **button_style)
btn_8 = Button(root, text="8", command=lambda: onClick(8), **button_style)
btn_9 = Button(root, text="9", command=lambda: onClick(9), **button_style)
btn_0 = Button(root, text="0", command=lambda: onClick(0), **button_style)
btn_00 = Button(root, text="00", command=lambda: onClick("00"), **button_style)
btn_add = Button(root, text="+", command=btn_add, **button_style)
btn_sub = Button(root, text="-", command=btn_sub, **button_style)
btn_div = Button(root, text="/", command=btn_div, **button_style)
btn_multi = Button(root, text="*", command=btn_multi, **button_style)
btn_clear = Button(root, text="C", command=Clear, **button_style)
btn_off = Button(root, text="OFF", command=root.quit, **button_style)
btn_result = Button(root, text="=", command=btn_result, **button_style)
btn_proc = Button(root, text="%", command=btn_proc, **button_style)
btn_dot = Button(root, text=",", command=lambda: onClick("."), **button_style)

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
