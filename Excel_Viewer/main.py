from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Excel Viewer")
root.geometry("1100x400+200+200")
root.configure(bg='#107C41')
root.iconbitmap('logo.ico')


# Frame
frame = Frame(root)
frame.pack(pady=25)

# Treeview
tree = ttk.Treeview(frame)
tree.pack()