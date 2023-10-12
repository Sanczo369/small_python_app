from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Mangement")
root.resizable(False,False)

Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri",33), width="300", height="2")


#MENU CARD
f=Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)
Label(f,text="Menu", font=("Gabriola", 40, "bold"),fg="black",bg="lightgreen").place(x=80, y=0)


#ENTRY WORK
f1=Frame(root,bd=5, height=370, width=300, relief=RAISED)
f1.pack()

food1=StringVar()
food2=StringVar()
food3=StringVar()
food4=StringVar()
food5=StringVar()
food6=StringVar()
food7=StringVar()
Total_bill=StringVar()


root.mainloop()