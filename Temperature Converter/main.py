import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("420x180")

# Celsius to Fahrenheit conversion function
def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    result_label.config(text=f"{celsius}°C = {fahrenheit}°F")