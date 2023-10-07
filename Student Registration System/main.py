from tkinter import *
from xlsxwriter import Workbook
import pathlib
background = '#06283D'
framebg= '#EDEDED'
framefg= '#06283D'

root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.resizable(False,False)
root.iconbitmap('img/logo.ico')
root.config(bg=background)

#Weryfikacja czy istnieje Student_data.xlsx
file_path = 'Student_data.xlsx'
file = pathlib.Path(file_path)
if file.exists():
    pass
else:
    workbook = Workbook(file_path)
    sheet = workbook.add_worksheet()
    sheet.write('A1',"Registration No.")
    sheet.write('B1',"Name")
    sheet.write('C1',"Class")
    sheet.write('D1',"Gender")
    sheet.write('E1',"DOB")
    sheet.write('F1',"Date Of Registration")
    sheet.write('G1',"Religion")
    sheet.write('H1',"Skill")
    sheet.write('I1',"Father Name")
    sheet.write('J1',"Mother Name")
    sheet.write('K1',"Father's Occupation")
    sheet.write('L1',"Mother's Occupation")
    workbook.close()

#Górna Belka
Label(root,text="Email:admin@gmail.com", width=10, height=3, bg='#f0687c', anchor='e').pack(side=TOP, fill=X)
Label(root,text="STUDENT REGISTRATION", width=10, height=2, bg='#c36464', fg='#fff', font='arial 20 bold').pack(side=TOP, fill=X)

# Wyszukiwarka
Search=StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font="arial 20").place(x=820, y=70)
imageicon3= PhotoImage(file="img/lupa.png")
Srch=Button(root,text="Search", compound=LEFT, image=imageicon3, width=123, bg="#68ddfa", font='arial 13 bold')
Srch.place(x=1060, y=66)

# Przycisk odśwież
imageicon4=PhotoImage(file='img/arrow.png')
Update_button=Button(root, image=imageicon4,bg='#c36464')
Update_button.place(x=110, y=64)

root.mainloop()