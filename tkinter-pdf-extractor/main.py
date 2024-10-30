import tkinter, PyPDF2
from tkinter import filedialog


def openFile():
    filename = filedialog.askopenfilename(title="Open PDF file",
                                                  initialdir='D:\codefirst.io\Tkinter Extract PDF Text',
                                                  filetypes=[('PDF files', '*.pdf')])
    filename_label.configure(text=filename)
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range (reader.numPages):
        current_text = reader.getPage(i).extractText()
        outputfile_text.insert(tkinter.END, current_text)