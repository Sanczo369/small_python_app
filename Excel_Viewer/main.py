from tkinter import *
from tkinter import ttk, messagebox, filedialog

import pandas as pd

root = Tk()
root.title("Excel Viewer")
root.geometry("1100x400+200+200")
root.configure(bg='#107C41')
root.iconbitmap('logo.ico')

def Open():
    filename= filedialog.askopenfilename(title="Open a File", filetypes=(("Open a File", ".*xlsx"), ("All files", "*.")))

    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except:
            messagebox.showerror("Error", "You can't access this file!")
# Frame
frame = Frame(root)
frame.pack(pady=25)

# Treeview
tree = ttk.Treeview(frame)
tree.pack()

# Button
button = Button(root, text='Open', width=60, height=2, font=30, fg="white", bg="#0078d7", command=Open)
button.pack(padx=10, pady=20)
root.mainloop()