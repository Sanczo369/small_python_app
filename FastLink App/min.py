import tkinter as tk
import pyshorteners
import os
import sys

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
        return os.path.join(bundle_dir, relative_path)
    base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.delete(0, tk.END)
    shorturl_entry.insert(0, short_url)


root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")