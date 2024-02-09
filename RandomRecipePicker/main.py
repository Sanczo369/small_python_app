import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet

# set colours
bg_colour = "#3d6466"


def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

def fetch_db():
	# connect an sqlite database
	connection = sqlite3.connect("data/recipes.db")
	cursor = connection.cursor()

	# fetch all the table names
	cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
	all_tables = cursor.fetchall()

	# choose random table idx
	idx = random.randint(0, len(all_tables)-1)

	# fetch records from table
	table_name = all_tables[idx][1]
	cursor.execute("SELECT * FROM " + table_name + ";")
	table_records = cursor.fetchall()

	connection.close()

	return table_name, table_records

# initiallize app with basic settings
root = tk.Tk()
root.title("Recipe Picker")
# create a frame widgets
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)



# run app
root.mainloop()