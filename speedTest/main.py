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

    Uploading=round(test.upload()/(1024*1024),2)
    upload.config(text=Uploading)

    downloading=round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    mainValue.config(text=downloading)

    servernames=[]
    test.get_servers(servernames)
    upload.config(text=test.results.ping)

topLabel = Label(root, text="SpeedTest",font=("arial",40,"bold"), fg="#ffffff", bg="#1a212d")
topLabel.pack(pady=(40,0))

mainImg=PhotoImage(file="main.png")
mainLabel = Label(root, image=mainImg, fg="#ffffff", bg="#1a212d")
mainLabel.pack(pady=(40,0))

startBtn=Button(root, text="START",font=("arial",20,"bold"),fg="#ffffff", bg="#1a212d", bd=3, activebackground="#1a212d",activeforeground="#ffffff", cursor="hand2",command=Check)
startBtn.pack(pady=(100,0))

# Label
Label(root, text="PING", font=("arial", 15, "bold"), fg="#ffffff", bg="#1a212d").place(x=20, y=380)
Label(root, text="DOWNLOAD", font=("arial", 15, "bold"), fg="#ffffff", bg="#1a212d").place(x=110, y=380)
Label(root, text="UPLOAD", font=("arial", 15, "bold"), fg="#ffffff", bg="#1a212d").place(x=260, y=380)

Label(root, text="MS", font=("arial", 10, "bold"), fg="#ffffff", bg="#1a212d").place(x=60, y=420)
Label(root, text="MBPS", font=("arial", 10, "bold"), fg="#ffffff", bg="#1a212d").place(x=185, y=420)
Label(root, text="MBPS", font=("arial", 10, "bold"), fg="#ffffff", bg="#1a212d").place(x=300, y=420)

Label(root, text="Download", font=("arial", 15, "bold"), fg="#ffffff", bg="#1a212d").place(x=129, y=240)
Label(root, text="MBPS", font=("arial", 15, "bold"), fg="#ffffff", bg="#1a212d").place(x=145, y=330)

# Value
ping=Label(root, text="00", font=("arial", 13, "bold"),fg="#ffffff", bg="#1a212d").place(x=35, y=418)
download=Label(root, text="00", font=("arial", 13, "bold"),fg="#ffffff", bg="#1a212d").place(x=160, y=418)
upload=Label(root, text="00", font=("arial", 13, "bold"),fg="#ffffff", bg="#1a212d").place(x=275, y=418)

# Main Value
mainValue=Label(root, text="000", font=("arial", 30, "bold"),fg="#ffffff", bg="#1a212d").place(x=143, y=278)
root.mainloop()