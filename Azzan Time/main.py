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

        self.frm1 = Frame(self.parent)
        self.frm1.pack()

        self.lblHijriMonthNum = Label(self.frm1, text=self.req["data"]["date"]["hijri"]["day"], font=("arial", 16))
        self.lblHijriMonthName = Label(self.frm1, text=self.req["data"]["date"]["hijri"]["month"]["en"],
                                       font=("arial", 16))
        self.lblHijriYear = Label(self.frm1, text=self.req["data"]["date"]["hijri"]["year"], font=("arial", 16))

        self.lblHijriMonthNum.grid(row=0, column=0)
        self.lblHijriMonthName.grid(row=0, column=1)
        self.lblHijriYear.grid(row=0, column=2)

        self.parent.after(1000, self.update)

    def calculateDifference(self):
        s1 = strftime("%H:%M:%S")
        s2 = self.azzanTime + ":00"

        FMT = "%H:%M:%S"
        # print(s2, s1)
        tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)

        if tdelta.days < 0:
            tdelta = timedelta(
                days=0,
                seconds=tdelta.seconds,
                microseconds=tdelta.microseconds
            )

        # print(tdelta)
        return str(tdelta)

    def update(self):
        # check if the clock is exactly at 12:00 AM
        if datetime.now().strftime("%H:%M:%S") == "00:00:00":
            self.req = self.getData()
            index = 0
            for x, y in self.req["data"]["timings"].items():  # iterates over your nums
                y_in = datetime.strptime(y, "%H:%M")
                y = datetime.strftime(y_in, "%I:%M %p")
                text = x + ": " + str(y)
                self.azzanTableArr[index].config(text=text)  # appends the label to the list for further use
                index += 1
            self.lblHijriMonthNum.config(text=self.req["data"]["date"]["hijri"]["day"])
            self.lblHijriMonthName.config(text=self.req["data"]["date"]["hijri"]["month"]["en"])
            self.lblHijriYear.config(text=self.req["data"]["date"]["hijri"]["year"])
        self.currentTime = strftime('%H:%M')
        self.azzanIndex = self.getNextAzzanIndex(self.req)
        self.azzanName = self.getAzzanName(self.req, self.azzanIndex)
        self.azzanTime = self.getAzzanTime(self.req, self.azzanIndex)
        x = self.calculateDifference()
        x = x.split(":")
        if (int(x[0]) > 9):
            self.azzanName = "Any second now..."
            self.lblAzzanTime.config(text="Any second now...")
            self.lblAzzanName.config(text=self.azzanName)
        else:
            self.lblAzzanTime.config(text=self.calculateDifference())
            self.lblAzzanName.config(text=self.azzanName)
        self.parent.after(1000, self.update)

    def getData(self):
        try:
            response = requests.get("http://api.aladhan.com/v1/timingsByCity?country=Egypt&city=Giza")
            data = response.json()
            del data["data"]["timings"]["Sunset"]
            del data["data"]["timings"]["Imsak"]
            del data["data"]["timings"]["Midnight"]
            return data
        except Exception as e:
            messagebox.showerror("Failed to connect to the server.", "Check if your internet is working correctly.")
            exit()


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