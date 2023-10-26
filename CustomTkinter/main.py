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

# Slider
# slider = CTkSlider(master=app)
# slider.place(relx=0.5, rely=0.5, anchor="center")
# slider = CTkSlider(master=app, from_=0, to=100, number_of_steps=5, button_color="#C850C0", progress_color="#C850C0", orientation="vertical")
# slider.place(relx=0.5, rely=0.5, anchor="center")

# Entry
# entry= CTkEntry(master=app)
# entry.place(relx=0.5, rely=0.5, anchor="center")

# entry= CTkEntry(master=app, placeholder_text="Start typing...", width=300, text_color="#FFCC70")
# entry.place(relx=0.5, rely=0.5, anchor="center")

# textbox
# textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70")
# textbox.place(relx=0.5, rely=0.5, anchor="center")

# textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16, border_color="#FFCC70", border_width=2)
# textbox.place(relx=0.5, rely=0.5, anchor="center")


# Event Handling
# def click_handler():
#     print("Button Clicked")
# btn = CTkButton(master=app, text="Click Me", command=click_handler)
# btn.place(relx= 0.5, rely = 0.5, anchor = "center")

# def click_handler(value):
#     print(f"Button Clicked {value}")
# btn = CTkComboBox(master=app, values=["Opt1", "Opt2", "Opt3"], command=click_handler)
# btn.place(relx= 0.5, rely = 0.5, anchor = "center")

# def click_handler():
#     print(f"Button Clicked {entry.get()}")
#
# entry=CTkEntry(master=app, placeholder_text="Type anything...")
# btn = CTkButton(master=app, text="Submit", command=click_handler)
#
# entry.pack(anchor="s", expand=True, pady=10)
# btn.pack(anchor = "n", expand=True)

# Frame
# frame = CTkFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
# frame.pack(expand=True)
# label = CTkLabel(master=frame, text="This is a frame")
# entry= CTkEntry(master=frame, placeholder_text="Type something...")
# btn = CTkButton(master=frame, text="Submit")
#
# label.pack(anchor="s", expand=True, pady=10, padx=30)
# entry.pack(anchor="s", expand=True, pady=10, padx=30)
# btn.pack(anchor="n", expand=True, pady=30, padx=20)



# TabView
tabview= CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("Tab 1")
tabview.add("Tab 2")
tabview.add("Tab 3")

label_1 = CTkLabel(master=tabview.tab("Tab 1"), text="This is a frame 1")
label_1.pack(pady=20, padx=20)

label_2 = CTkLabel(master=tabview.tab("Tab 2"), text="This is a frame 2")
label_2.pack(pady=20, padx=20)

label_3 = CTkLabel(master=tabview.tab("Tab 3"), text="This is a frame 3")
label_3.pack(pady=20, padx=20)



app.mainloop()