from tkinter import *
import speedtest

root=Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(bg="#1a212d")

# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)
def Check():
    test=speedtest.Speedtest()

    Uploading=test.upload()
    print(Uploading)
    downloading= test.download()
    print(downloading)
    servernames=[]

    test.get_servers(servernames)
    print(test.results.ping)

Check()

root.mainloop()