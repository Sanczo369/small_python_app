import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

# window
window = ttk.Window(themename = 'darkly')
window.title('extra widgets')

# scrollable frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand = True, fill = 'both')

# run
window.mainloop()