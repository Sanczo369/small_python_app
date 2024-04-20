import customtkinter as ctk
from PIL import Image
from os import walk

# exercise:
# create an animation that runs forever

class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, light_path, dark_path):
        # animation logic setup
        self.frames = self.import_folders(light_path, dark_path)
        self.frame_index = 0
        self.animation_length = len(self.frames) - 1
        self.animation_status = ctk.StringVar(value='start')

        self.animation_status.trace('w', self.animate)


# window
window = ctk.CTk()
window.title('Animations')
window.geometry('300x200')
# ctk.set_appearance_mode('light')

AnimatedButton(window, 'black', 'yellow')

# run
window.mainloop()