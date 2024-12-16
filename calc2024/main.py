import tkinter
from tkinter import *

root=Tk()
root.title("CALCULATOR")
root.geometry("570x600")
root.resizable(False,False)
root.configure(bg="#17161b")
root.iconbitmap(r'C:\coding in different different languages\PYTHON\CALCULATOR\Calculator-icon.ico')

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation =""
    label_result.config(text=equation)