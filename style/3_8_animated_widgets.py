import customtkinter as ctk
from random import choice

# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')


def move_btn():
    global button_x
    button_x += 0.001
    button.place(relx=button_x, rely=0.5, anchor='center')

    if button_x < 0.9:
        window.after(10, move_btn)

    # configure
    # colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
    # color = choice(colors)
    # button.configure(fg_color = color)

def infinite_print():
	global button_x
	button_x += 0.5
	if button_x < 10:
		print('infinite')
		print(button_x)
		window.after(100, infinite_print)

# animated widget
animated_panel = SlidePanel(window, 1.0, 0.7)
ctk.CTkLabel(animated_panel, text = 'Label 1').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkLabel(animated_panel, text = 'Label 2').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkButton(animated_panel, text = 'Button', corner_radius = 0).pack(expand = True, fill = 'both', pady = 10)
ctk.CTkTextbox(animated_panel, fg_color = ('#dbdbdb','#2b2b2b')).pack(expand = True, fill = 'both', pady = 10)

# button
button_x = 0.5
button = ctk.CTkButton(window, text = 'toggle sidebar', command = animated_panel.animate)
button.place(relx = button_x, rely = 0.5, anchor = 'center')

# run
window.mainloop()