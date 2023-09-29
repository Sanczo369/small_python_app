from tkinter import *
from tkinter import ttk, messagebox, filedialog
import numpy
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
    tree.delete(*tree.get_children())

    # nagłówek arkusza danych
    tree["column"]= list(df.columns)
    tree['show'] = "headings"

    # tytuły nagłówków
    for col in tree["column"]:
        tree.heading(col, text=col)

    #wprowadzone danych
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)
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