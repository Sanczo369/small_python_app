from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Mangement")
root.resizable(False,False)

Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri",33), width="300", height="2")


# MENU CARD
f=Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)
Label(f,text="Menu", font=("Gabriola", 40, "bold"),fg="black",bg="lightgreen").place(x=80, y=0)


# ENTRY WORK
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


# LABEL
lbl_food1=Label(f1,font=("arial",20,"bold"),text="Food1",width=12,fg="blue4")
lbl_food2=Label(f1,font=("arial",20,"bold"),text="Food2",width=12,fg="blue4")
lbl_food3=Label(f1,font=("arial",20,"bold"),text="Food3",width=12,fg="blue4")
lbl_food4=Label(f1,font=("arial",20,"bold"),text="Food4",width=12,fg="blue4")
lbl_food5=Label(f1,font=("arial",20,"bold"),text="Food5",width=12,fg="blue4")
lbl_food6=Label(f1,font=("arial",20,"bold"),text="Food6",width=12,fg="blue4")
lbl_food7=Label(f1,font=("arial",20,"bold"),text="Food7",width=12,fg="blue4")

lbl_food1.grid(row=1, column=0)
lbl_food2.grid(row=2, column=0)
lbl_food3.grid(row=3, column=0)
lbl_food4.grid(row=4, column=0)
lbl_food5.grid(row=5, column=0)
lbl_food6.grid(row=6, column=0)
lbl_food7.grid(row=7, column=0)


#ENTRY
entry_food1=Entry(f1, font=("arial", 20, "bold"), textvariable=food1, bd=6, width=8, bg="lightpink")
entry_food2=Entry(f1, font=("arial", 20, "bold"), textvariable=food2, bd=6, width=8, bg="lightpink")
entry_food3=Entry(f1, font=("arial", 20, "bold"), textvariable=food3, bd=6, width=8, bg="lightpink")
entry_food4=Entry(f1, font=("arial", 20, "bold"), textvariable=food4, bd=6, width=8, bg="lightpink")
entry_food5=Entry(f1, font=("arial", 20, "bold"), textvariable=food5, bd=6, width=8, bg="lightpink")
entry_food6=Entry(f1, font=("arial", 20, "bold"), textvariable=food6, bd=6, width=8, bg="lightpink")
entry_food7=Entry(f1, font=("arial", 20, "bold"), textvariable=food7, bd=6, width=8, bg="lightpink")
entry_food1.grid(row=1, column=1)
entry_food2.grid(row=2, column=1)
entry_food3.grid(row=3, column=1)
entry_food4.grid(row=4, column=1)
entry_food5.grid(row=5, column=1)
entry_food6.grid(row=6, column=1)
entry_food7.grid(row=7, column=1)
root.mainloop()