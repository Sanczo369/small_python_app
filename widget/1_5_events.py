import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# window.bind('<Motion>', get_pos)

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# exercise :
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

# run
window.mainloop()