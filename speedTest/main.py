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

topLabel = Label(root, text="SpeedTest",font=("arial",40,"bold"), fg="#ffffff", bg="#1a212d")
topLabel.pack(pady=(40,0))

mainImg=PhotoImage(file="main.png")
mainLabel = Label(root, image=mainImg, fg="#ffffff", bg="#1a212d")
mainLabel.pack(pady=(40,0))

startBtn=Button(root, text="START",font=("arial",20,"bold"),fg="#ffffff", bg="#1a212d", bd=3, activebackground="#1a212d",activeforeground="#ffffff", cursor="hand2")
startBtn.pack(pady=(40,0))
root.mainloop()