from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")

# Define Element
frameCalc = LabelFrame(root, text="Calculator", padx=5, pady=5)
e_result = Entry(frameCalc, bg="#FFF", width=5, font=("Arial", 20))
btn_1 = Button(frameCalc, height=2, width=5, text="1")
btn_2 = Button(frameCalc, height=2, width=5, text="2")
btn_3 = Button(frameCalc, height=2, width=5, text="3")
btn_4 = Button(frameCalc, height=2, width=5, text="4")
btn_5 = Button(frameCalc, height=2, width=5, text="5")
btn_6 = Button(frameCalc, height=2, width=5, text="6")
btn_7 = Button(frameCalc, height=2, width=5, text="7")
btn_8 = Button(frameCalc, height=2, width=5, text="8")
btn_9 = Button(frameCalc, height=2, width=5, text="9")
btn_0 = Button(frameCalc, height=2, width=5, text="0")
btn_00 = Button(frameCalc, height=2, width=5, text="00")
btn_add = Button(frameCalc, height=2, width=5, text="+")
btn_sub = Button(frameCalc, height=2, width=5, text="-")
btn_div = Button(frameCalc, height=2, width=5, text="/")
btn_multi = Button(frameCalc, height=2, width=5, text="*")
btn_clear = Button(frameCalc, height=2, width=5, text="C")
btn_off = Button(frameCalc, height=2, width=5, text="OFF")
btn_result = Button(frameCalc, height=2, width=5, text="=")
btn_proc = Button(frameCalc, height=2, width=5, text="%")
btn_dot = Button(frameCalc, height=2, width=5, text=",")


if __name__ == '__main__':
    root.mainloop()
