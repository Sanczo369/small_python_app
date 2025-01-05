import os
import glob
from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk, filedialog

# File Extensions: You can modify it as per your requirements
file_types = ['.jpg', 'jpeg', '.png', '.mp3', '.mp4', '.pdf']


class File_Renamer:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("720x500")
        self.window.title('File Renamer - PySeek')
        self.window.resizable(width = False, height = False)
        self.window.configure(bg='gray90')

        # Declaring some variables
        self.Selected_Folder = ''
        self.SaveTo_Loc = ''
        self.File_List = list()
        # Python Dictionary to store the file name corresponding
        # with the file path
        self.File_Dict = dict()

        # Frame 1: For the Logo
        self.frame_1 = Frame(self.window,bg='gray90',\
        width=280, height=70)
        self.frame_1.pack()
        self.frame_1.place(x=20, y=20)

        # Calling the function to display the logo
        self.Display_Logo()

        # About Button
        About_Btn = Button(self.window, text="About", \
        font=("Kokila", 10, 'bold'), bg="dodger blue", \
        fg="white", width=5, command=self.About_Window)
        About_Btn.place(x=600, y=20)

        # Exit Button
        Exit_Btn = Button(self.window, text="Exit", \
        font=("Kokila", 10, 'bold'), bg="dodger blue", \
        fg="white", width=5, command=self.Exit_Window)
        Exit_Btn.place(x=600, y=60)

        # Frame 2: For the Main Window Widgets
        self.frame_2 = Frame(self.window, bg="white",\
        width=720,height=480)
        self.frame_2.place(x=0, y=110)

        # Calling the function to display main window widgets
        self.Main_Window()

    # This function displays the File Renamer Logo
    def Display_Logo(self):
        # Opening the logo image
        image = Image.open('Images/File_Renamer.png')
        # Resizing the image
        resized_image = image.resize((280, 70))
        # Create an object of tkinter ImageTk
        self.img_1 = ImageTk.PhotoImage(resized_image)
        # Create a Label Widget to display the text or Image
        label = Label(self.frame_1, bg='gray90',image=self.img_1)
        label.pack()

    # This function displays all the widgets in the 'self.frame_2'
    # related to File Renaming Operation
    def Main_Window(self):
        Filetype_Label = Label(self.frame_2, text="File Type: ", \
        font=("Kokila", 12, 'bold'), bg='white')
        Filetype_Label.place(x=50, y=30)

        self.f_type = StringVar()
        # Combo Box for showing the file extensions
        self.File_Type = ttk.Combobox(self.frame_2, \
        textvariable=self.f_type, font=("times new roman",13),width=8)
        self.File_Type['values'] = file_types
        self.File_Type.current(0)
        self.File_Type.place(x=150,y=30)

        # Button for selecting the directory (where
        # the desired files are presented)
        Folder_Button = Button(self.frame_2, text="Select Folder", \
        font=("Kokila", 10, 'bold'), bg="gold", width=10, \
        command=self.Select_Directory)
        Folder_Button.place(x=20, y=70)

        self.Folder_Entry = Entry(self.frame_2, \
        font=("Helvetica", 12), width=30)
        self.Folder_Entry.place(x=150, y=75)

        SaveTo_Button = Button(self.frame_2, text="Save To", \
        font=("Kokila", 10, 'bold'), bg="green", fg='white', \
        width=10, command=self.SaveTo_Directory)
        SaveTo_Button.place(x=20, y=125)

        self.SaveTo_Entry = Entry(self.frame_2, font=("Helvetica", 12), width=30)
        self.SaveTo_Entry.place(x=150, y=130)

        ResultFile_Label = Label(self.frame_2, \
        text="Result File: ", font=("Kokila", 12, 'bold'), bg='white')
        ResultFile_Label.place(x=35, y=175)

        self.ResultFile_Entry = Entry(self.frame_2, \
        font=("Helvetica", 12))
        self.ResultFile_Entry.place(x=150, y=175)

        Status = Label(self.frame_2, text="Status: ", \
        font=("Kokila", 12, 'bold'), bg='white')
        Status.place(x=70, y=215)

        self.Status_Label = Label(self.frame_2, text="Not Started Yet", \
        font=("Kokila", 12), bg="white", fg="red")
        self.Status_Label.place(x=150, y=215)

        # ListBox Label
        Listbox_Label = Label(self.frame_2, text="Selected Files", \
        font=("Times New Roman", 14, 'bold'), bg='white')
        Listbox_Label.place(x=515, y=30)

        # Listbox for showing the selected files for renaming
        self.File_ListBox = Listbox(self.frame_2,width=30, height=14)
        self.File_ListBox.place(x=450, y=60)

        Add_Button = Button(self.frame_2, text='Add', \
        font=("Kokila", 9, 'bold'), width=6, command=self.Add_File)
        Add_Button.place(x=450, y=322)

        Delete_Button = Button(self.frame_2, text='Delete', \
        font=("Kokila", 9, 'bold'), width=6, command=self.Delete_File)
        Delete_Button.place(x=530, y=322)

        Start_Button = Button(self.frame_2, text="Start", \
        font=("Kokila", 13, 'bold'), bg="dodger blue", fg="white", \
        width=8, command=self.Threading)
        Start_Button.place(x=120, y=260)

    def Select_Directory(self):
        self.Clear_Listbox()
        self.Selected_Folder = filedialog.askdirectory(title = "Select a location")
        self.Folder_Entry.insert(0, self.Selected_Folder)
        # If the user selects a directory
        if self.Selected_Folder != '':
            self.Files_in_Listbox()

    def SaveTo_Directory(self):
        self.SaveTo_Loc = filedialog.askdirectory(title = "Select a location")
        self.SaveTo_Entry.insert(0, self.SaveTo_Loc)

    def Files_in_Listbox(self):
        self.File_List = \
        glob.glob(f"{self.Selected_Folder}/*{self.File_Type.get()}")
        for path in self.File_List:
            # Storing the file name with the corresponding file
            # path to the 'self.File_Dict' dictionary
            self.File_Dict[os.path.basename(path)] = path
            self.File_ListBox.insert(END, os.path.basename(path))

    def Add_File(self):
        File_Path = filedialog.askopenfilenames(initialdir = "/", \
        title = "Select PDF Files", filetypes = \
        ((f"{self.File_Type.get()} files",f"*{self.File_Type.get()}*"),))

        for Path in File_Path:
            # Adding the file path to the 'self.File_List'
            self.File_List.append(Path)
            # Adding the file name(as Key) and path(as Value)
            # to the 'self.File_Dict'
            self.File_Dict[os.path.basename(Path)] = Path
            # Adding the File Name to the ListBox
            self.File_ListBox.insert(END, os.path.basename(Path))

    def Delete_File(self):
        try:
            if len(self.File_List) < 1:
                messagebox.showwarning('Warning!', \
                'There are no more files to delete')
            else:
                for item in self.File_ListBox.curselection():
                    self.File_List.remove(\
                    self.File_Dict[self.File_ListBox.get(item)])
                    self.File_Dict.pop(self.File_ListBox.get(item))

                    self.File_ListBox.delete(item)
        except Exception:
            messagebox.showwarning('Warning!', "Please select PDFs first")