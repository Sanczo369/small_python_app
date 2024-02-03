from datetime import datetime, timedelta
from time import strftime
import requests
from tkinter import Frame, Label, Tk, messagebox, PhotoImage
from base64 import b64decode
from os import remove

WIDTH = 400
HEIGHT = 380

class MainApplication(Frame):
    def __init__(self, parent):
    	# INIT
        Frame.__init__(self, parent)
        self.parent = parent
        self.currentTime = strftime('%H:%M')
        self.req = self.getData()
        self.azzanName = "Unknown"
        self.azzanTime = "Unknown"
        self.azzanIndex = self.getNextAzzanIndex(self.req)
        self.azzanName = self.getAzzanName(self.req, self.azzanIndex)
        self.azzanTime = self.getAzzanTime(self.req, self.azzanIndex)
        self.azzanTableArr = []

        # GUI PART
        Label(self.parent, text="Next Azzan is:", font=("arial", 16)).pack()
        self.lblAzzanName = Label(self.parent, text=self.azzanName, font=("arial", 32))
        self.lblAzzanName.pack()

        self.lblAzzanTime = Label(self.parent, text=self.calculateDifference(), font=("arial", 32))
        Label(self.parent, text="It will be in:", font=("arial", 16)).pack()
        self.lblAzzanTime.pack()

        for x, y in self.req["data"]["timings"].items():  # iterates over your nums
            y_in = datetime.strptime(y, "%H:%M")
            y = datetime.strftime(y_in, "%I:%M %p")
            text = x + ": " + str(y)
            label = Label(self.parent, text=text, font=("arial", 16))  # set your text
            label.pack(anchor="w")
            self.azzanTableArr.append(label)  # appends the label to the list for further use

if __name__ == "__main__":
    root = Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (WIDTH / 2))
    y_cordinate = int((screen_height / 2) - (HEIGHT / 2))

    root.resizable(0, 0)

    root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_cordinate, y_cordinate))
    root.title("Azzan times | Made by Omar Hosam")

    MainApplication(root)

    root.mainloop()