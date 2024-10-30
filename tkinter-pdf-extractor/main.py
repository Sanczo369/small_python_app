import tkinter, PyPDF2
from tkinter import filedialog


def openFile():
    filename = filedialog.askopenfilename(title="Open PDF file",
                                                  initialdir='D:\codefirst.io\Tkinter Extract PDF Text',
                                                  filetypes=[('PDF files', '*.pdf')])