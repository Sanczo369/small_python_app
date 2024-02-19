
from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="white", fg="Black", relief=GROOVE)
        title.pack(fill=X)

        # ================variables=======================

        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()

        # ============grocery==============================

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()

        # =============coldDtinks=============================

        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()

        # ==============Total product price================

        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        # ==============Customer==========================

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ===============Tax================================

        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        # =============customer retail details======================

        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#badc57", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#badc57", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

        # ===================Medical====================================

        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        dettol_lbl = Label(F2, text="Dettol", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        dettol_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        dettol_txt = Entry(F2, width=10, textvariable=self.dettol, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        dettol_txt.grid(row=3, column=1, padx=10, pady=10)

        newsprin_lbl = Label(F2, text="Newsprin", font =('times new roman', 16, 'bold'), bg = "#badc57", fg = "black")
        newsprin_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        newsprin_txt = Entry(F2, width=10, textvariable=self.newsprin, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        newsprin_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)


root = Tk()

root.mainloop()