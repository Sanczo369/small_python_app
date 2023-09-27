from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def get_weather():
    try:
        city=textfield.get()
        geolocator= Nominatim(user_agent="xxxx")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result= obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home= pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="AKTUALNA POGODA")

        api=f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&xxxx"
        json_data=requests.get(api).json()

        if 'weather' in json_data:
            condition = json_data['weather'][0]['main']
            clouds = json_data['clouds']['all']
            temp = int(json_data["main"]["temp"]-273.15)
            pressure = json_data["main"]["pressure"]
            humidity = json_data['main']["humidity"]
            wind =json_data['wind']["speed"]

            t.config(text=f"{temp}°")
            c.config(text=f"{condition}| FEELS LIKE {temp}°")
            w.config(text=f"{wind}m/s")
            h.config(text=f"{humidity}%")
            d.config(text=f"{clouds}%")
            p.config(text=f"{pressure}hPa")
        else:
            t.config(text="N/A")
            c.config(text="N/A")
            w.config(text="N/A")
            h.config(text="N/A")
            d.config(text="N/A")
            p.config(text="N/A")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")

root=Tk()
root.title("Weather_App")
root.geometry('900x500+300+200')
root.resizable(False,False)
root.iconbitmap('logo.ico')

#search box
textfield = tk.Entry(root, justify='center', width=17, font=("poppins", 25, "bold"), bg="#404040", fg="white")
textfield.place(x=50, y=40)
textfield.focus()

#search icon
Search_icon=PhotoImage(file="lupa.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=get_weather)
myimage_icon.place(x=359, y=40)


# Bottom box
Frame_image = PhotoImage(file='box.png')
frame_myimage=Label(image=Frame_image)
frame_myimage.place(x=50, y=398)

# time
name=Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock=Label(root,font=("Helvetica", 20))
clock.place(x=30, y=130)

#label
label1=Label(root, text="WIATR", font=("Helvetica", 15, "bold"), fg="white",bg="#1ab5ef")
label1.place(x=60, y=400)

label2=Label(root, text="WILGOTNOŚĆ", font=("Helvetica", 15, "bold"), fg="white",bg="#1ab5ef")
label2.place(x=220, y=400)

label3=Label(root, text="ZACHMURZENIE", font=("Helvetica", 15, "bold"), fg="white",bg="#1ab5ef")
label3.place(x=400, y=400)

label4=Label(root, text="CIŚNIENIE", font=("Helvetica", 15, "bold"), fg="white",bg="#1ab5ef")
label4.place(x=600, y=400)

t=Label(font=("arial", 40, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c=Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w=Label(text="", font=("arial", 20, "bold"), fg="white", bg="#1ab5ef")
w.place(x=60, y=430)
h=Label(text="", font=("arial", 20, "bold"), fg="white", bg="#1ab5ef")
h.place(x=220, y=430)
d=Label(text="", font=("arial", 20, "bold"), fg="white", bg="#1ab5ef")
d.place(x=400, y=430)
p=Label(text="", font=("arial", 20, "bold"), fg="white", bg="#1ab5ef")
p.place(x=600, y=430)
root.mainloop()