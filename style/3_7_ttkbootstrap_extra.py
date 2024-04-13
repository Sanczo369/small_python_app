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

for i in range(100):
	frame = ttk.Frame(scroll_frame)
	ttk.Label(frame, text = f'Label: {i}').pack(fill = 'x', side = 'left')
	ttk.Button(frame, text = f'Button :{i}').pack(fill = 'x', side = 'left')
	frame.pack(fill = 'x', expand = True)

# toast
toast = ToastNotification(
	title = 'This is a message title',
	message = 'This is the actual message',
	duration = 2000,
	bootstyle = 'dark',
	position = (50, 100, 'ne'))

ttk.Button(window, text = 'show toast', command = toast.show_toast).pack(pady = 10)

# run
window.mainloop()