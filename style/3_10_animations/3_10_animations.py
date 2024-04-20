import customtkinter as ctk
from PIL import Image
from os import walk

# exercise:
# create an animation that runs forever



# window
window = ctk.CTk()
window.title('Animations')
window.geometry('300x200')
# ctk.set_appearance_mode('light')

AnimatedButton(window, 'black', 'yellow')

# run
window.mainloop()