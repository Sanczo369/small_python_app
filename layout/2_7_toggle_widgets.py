import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Hide widgets')

# place
# def toggle_label_place():
# 	global label_visible

# 	if label_visible:
# 		label.place_forget()
# 		label_visible = False
# 	else:
# 		label_visible = True
# 		label.place(relx = 0.5, rely = 0.5, anchor = 'center')

# button = ttk.Button(window, text = 'toggle Label', command = toggle_label_place)
# button.place(x = 10, y = 10)

# label_visible = True
# label = ttk.Label(window, text= 'A label')
# label.place(relx = 0.5, rely = 0.5, anchor = 'center')

# grid
# def toggle_label_grid():
# 	global label_visible

# 	if label_visible:
# 		label.grid_forget()
# 		label_visible = False
# 	else:
# 		label_visible = True
# 		label.grid(column = 1, row = 0)

# run
window.mainloop()