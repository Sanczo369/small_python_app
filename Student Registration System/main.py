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



root.mainloop()