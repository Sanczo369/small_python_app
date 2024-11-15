import customtkinter as ctk

def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    entry.delete(0, ctk.END)
