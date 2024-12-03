import openpyxl
from docxtpl import DocxTemplate
import datetime

# Load data from Excel
path = "D:\codefirst.io\Excel Sheet to Word Documents\student_data.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

list_values = list(sheet.values)
print(list_values)