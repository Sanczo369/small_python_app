import tkinter
import pyshorteners


def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x150")
