import customtkinter as ctk
from random import choice

# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

# animated widget
animated_panel = SlidePanel(window, 1.0, 0.7)
ctk.CTkLabel(animated_panel, text = 'Label 1').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkLabel(animated_panel, text = 'Label 2').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkButton(animated_panel, text = 'Button', corner_radius = 0).pack(expand = True, fill = 'both', pady = 10)
ctk.CTkTextbox(animated_panel, fg_color = ('#dbdbdb','#2b2b2b')).pack(expand = True, fill = 'both', pady = 10)

# run
window.mainloop()