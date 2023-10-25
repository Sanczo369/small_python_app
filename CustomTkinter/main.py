from customtkinter import *
from PIL import Image
app = CTk()
app.geometry("500x400")

# Tryby Wyglądu
set_appearance_mode("dark")
# set_appearance_mode("light")

# Przyciski
# btn = CTkButton(master=app, text="Click Me")
# btn.place(relx= 0.2, rely = 0.1, anchor = "n")
#
# btn2 = CTkButton(master=app, text="Click Me", corner_radius=32)
# btn2.place(relx= 0.5, rely = 0.1, anchor = "n")
#
# btn3 = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0")
# btn3.place(relx= 0.8, rely = 0.1, anchor = "n")
#
# btn4 = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2)
# btn4.place(relx= 0.2, rely = 0.3, anchor = "n")
#
# img = Image.open("icon.png")
# btn5 = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", border_color="#FFCC70", border_width=2, image=CTkImage(dark_image=img, light_image=img))
# btn5.place(relx= 0.5, rely = 0.3, anchor = "n")

# Label
# label= CTkLabel(master=app, text="Some Text...", font=("Arial", 20), text_color="#FFCC70")
# label.place(relx=0.5, rely=0.5, anchor="center")

# Combobox
# combobox = CTkComboBox(master=app, values=["option 1", "option 2", "option 3"])
# combobox.place(relx=0.5, rely=0.5, anchor="center")

# Switch
# checkbox = CTkCheckBox(master=app, text= "Option")
# checkbox.place(relx=0.5, rely=0.5, anchor="center")
#
# checkbox = CTkCheckBox(master=app, text= "Option", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=36)
# checkbox.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()