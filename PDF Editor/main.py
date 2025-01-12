import os
import PyPDF2
import os.path
from tkinter import *
from functools import partial
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from tkinter import ttk, messagebox
from PyPDF2.pdf import PdfFileWriter

class PDF_Editor:
    def __init__(self, root):
        self.window = root
        self.window.geometry("740x480")
        self.window.title('PDF Editor')

        # Color Options
        self.color_1 = "white"
        self.color_2 = "gray30"
        self.color_3 = "black"
        self.color_4 = 'orange red'

        # Font Options
        self.font_1 = "Helvetica"
        self.font_2 = "Times New Roman"
        self.font_3 = "Kokila"

        self.saving_location = ''

        # ================Menubar Section===============
        self.menubar = Menu(self.window)

        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Split PDF',command=partial(self.SelectPDF, 1))
        edit.add_command(label='Merge PDFs',command=self.Merge_PDFs_Data)
        edit.add_separator()
        edit.add_command(label='Rotate PDFs',command=partial(self.SelectPDF, 2))

        # Adding About Menu
        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=about)
        about.add_command(label='About', command=self.AboutWindow)

        # Exit the Application
        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Exit', menu=exit)
        exit.add_command(label='Exit', command=self.Exit)

        # Configuring the menubar
        self.window.config(menu=self.menubar)
        # ===================End=======================

        # Creating a Frame
        self.frame_1 = Frame(self.window,bg=self.color_2,width=740,height=480)
        self.frame_1.place(x=0, y=0)
        # Calling Home Page Window
        self.Home_Page()

    # Home Page: It consists Three Buttons
    def Home_Page(self):
        self.ClearScreen()

        # ================Buttons Section===============
        self.split_button = Button(self.frame_1, text='Split',
        font=(self.font_1, 25, 'bold'), bg="yellow", fg="black", width=8,
        command=partial(self.SelectPDF, 1))
        self.split_button.place(x=260, y=80)

        # Merge Button
        self.merge_button = Button(self.frame_1, text='Merge',
        font=(self.font_1, 25, 'bold'), bg="yellow", fg="black",
        width=8, command=self.Merge_PDFs_Data)
        self.merge_button.place(x=260, y=160)

        # Merge Button
        self.rotation_button = Button(self.frame_1, text='Rotate',
        font=(self.font_1, 25, 'bold'), bg="yellow", fg="black",
        width=8, command=partial(self.SelectPDF, 2))
        self.rotation_button.place(x=260, y=240)
        # ===================End=======================

# Select the PDF for Splitting and Rotating
    def SelectPDF(self, to_call):
        self.PDF_path = filedialog.askopenfilename(initialdir = "/",
        title = "Select a PDF File", filetypes = (("PDF files", "*.pdf*"),))
        if len(self.PDF_path) != 0:
            if to_call == 1:
                self.Split_PDF_Data()
            else:
                self.Rotate_PDFs_Data()

    # Select PDF files only for merging
    def SelectPDF_Merge(self):
        self.PDF_path = filedialog.askopenfilenames(initialdir = "/",
        title = "Select PDF Files", filetypes = (("PDF files", "*.pdf*"),))
        for path in self.PDF_path:
            self.PDF_List.insert((self.PDF_path.index(path)+1), path)


    # Select the directory where the result PDF
    # file/files will be stored
    def Select_Directory(self):
        # Storing the 'saving location' for the result file
        self.saving_location = filedialog.askdirectory(title =
        "Select a location")
        self.Update_Path_Label()

    # Get the data from the user for splitting a PDF file
    def Split_PDF_Data(self):
        pdfReader = PyPDF2.PdfFileReader(self.PDF_path)
        total_pages = pdfReader.numPages

        self.ClearScreen()
        # Button for getting back to the Home Page
        home_btn = Button(self.frame_1, text="Home",
        font=(self.font_1, 10, 'bold'), command=self.Home_Page)
        home_btn.place(x=10, y=10)

        # Header Label
        header = Label(self.frame_1, text="Split PDF",
                       font=(self.font_3, 25, "bold"), bg=self.color_2, fg=self.color_1)
        header.place(x=265, y=15)


        # Label for showing the total number of pages
        self.pages_label = Label(self.frame_1,
                                 text=f"Total Number of Pages: {total_pages}",
                                 font=(self.font_2, 20, 'bold'), bg=self.color_2, fg=self.color_3)
        self.pages_label.place(x=40, y=70)


        # From Label: the page number from where the
        # user want to split the PDF pages
        From = Label(self.frame_1, text="From",
                     font=(self.font_2, 16, 'bold'), bg=self.color_2, fg=self.color_1)
        From.place(x=40, y=120)

        self.From_Entry = Entry(self.frame_1, font=(self.font_2, 12, 'bold'),
                                width=8)
        self.From_Entry.place(x=40, y=160)

        # To Label
        To = Label(self.frame_1, text="To", font=(self.font_2, 16, 'bold'),
        bg=self.color_2, fg=self.color_1)
        To.place(x=160, y= 120)

        self.To_Entry = Entry(self.frame_1, font=(self.font_2, 12, 'bold'),
        width=8)
        self.To_Entry.place(x=160, y= 160)

        Cur_Directory = Label(self.frame_1, text="Storing Location",
        font=(self.font_2, 16, 'bold'), bg=self.color_2, fg=self.color_1)
        Cur_Directory.place(x=300, y= 120)

        # Constant
        self.path_label = Label(self.frame_1, text='/',
        font=(self.font_2, 16, 'bold'), bg=self.color_2, fg=self.color_3)
        self.path_label.place(x=300, y= 160)

        # Button for selecting the directory
        # where the splitted PDFs will be stored
        select_loc_btn = Button(self.frame_1, text="Select Location",
        font=(self.font_1, 8, 'bold'), command=self.Select_Directory)
        select_loc_btn.place(x=320, y=200)

        split_button = Button(self.frame_1, text="Split",
        font=(self.font_3, 16, 'bold'), bg=self.color_4, fg=self.color_1,
        width=12, command=self.Split_PDF)
        split_button.place(x=250, y=250)

        # Get the data from the user for Merge PDF files

    def Merge_PDFs_Data(self):
        self.ClearScreen()
        # Button for get back to the Home Page
        home_btn = Button(self.frame_1, text="Home",
                          font=(self.font_1, 10, 'bold'), command=self.Home_Page)
        home_btn.place(x=10, y=10)

        # Header Label
        header = Label(self.frame_1, text="Merge PDFs",
        font=(self.font_3, 25, "bold"), bg=self.color_2, fg=self.color_1)
        header.place(x=265, y=15)

        select_pdf_label = Label(self.frame_1, text="Select PDFs",
        font=(self.font_2, 20, 'bold'), bg=self.color_2, fg=self.color_3)
        select_pdf_label.place(x=40, y=70)

        open_button = Button(self.frame_1, text="Open Folder",
        font=(self.font_1, 9, 'bold'), command=self.SelectPDF_Merge)
        open_button.place(x=55, y=110)

        Cur_Directory = Label(self.frame_1, text="Storing Location",
        font=(self.font_2, 18, 'bold'), bg=self.color_2, fg=self.color_1)
        Cur_Directory.place(x=40, y= 150)

        # Constant
        self.path_label = Label(self.frame_1, text='/',
        font=(self.font_2, 16, 'bold'), bg=self.color_2, fg=self.color_3)
        self.path_label.place(x=40, y= 190)

        # Button for selecting the directory
        # where the splitted PDFs will be stored
        select_loc_btn = Button(self.frame_1, text="Select Location",
        font=(self.font_1, 8, 'bold'), command=self.Select_Directory)
        select_loc_btn.place(x=320, y=200)

        split_button = Button(self.frame_1, text="Split",
        font=(self.font_3, 16, 'bold'), bg=self.color_4, fg=self.color_1,
        width=12, command=self.Split_PDF)
        split_button.place(x=250, y=250)

    # Get the data from the user for Merge PDF files
    def Merge_PDFs_Data(self):
        self.ClearScreen()
        # Button for get back to the Home Page
        home_btn = Button(self.frame_1, text="Home",
                          font=(self.font_1, 10, 'bold'), command=self.Home_Page)
        home_btn.place(x=10, y=10)