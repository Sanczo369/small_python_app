'''
METHODS ADDED
--------------------------------
next_track
prev_track

METHODS MODIFIED
--------------------------------
create_button_frame - added all control buttons
'''
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import os
import player
class GUI:
    alltracks = []
    indx = 0
    currentTrack = ''
    timer = [0, 0]  # corresponding to minutes and seconds
    timepattern = '{0:02d}:{1:02d}'
    loopchoices = [("No Loop", 1), ("Loop Current", 2), ("Loop All", 3)]
    selectedloopchoice = 3  # deafult 'no loop'
    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk()
        self.create_button_frame()
        self.create_list_frame()
        self.create_bottom_frame()
        self.root.mainloop()

    def create_button_frame(self):
        buttonframe = Frame(self.root)
        previcon = PhotoImage(file='../icons/previous.gif')
        prevbtn=Button(buttonframe, image=previcon, borderwidth=0, padx=0, command=self.prev_track)
        prevbtn.image = previcon
        prevbtn.grid(row=3, column=1, sticky='w')

        del_selectedicon = PhotoImage(file='../icons/del_selected.gif')
        del_selectedbtn=Button(bottomframe,image=del_selectedicon,borderwidth=0,padx=0, text='Delete', command=self.del_selected)
        del_selectedbtn.image = del_selectedicon
        del_selectedbtn.grid(row=5, column=2 )

        add_diricon = PhotoImage(file='../icons/add_dir.gif')
        add_dirbtn=Button(bottomframe,image=add_diricon,borderwidth=0,padx=0, text='Add Dir', command=self.add_dir)
        add_dirbtn.image = add_diricon
        add_dirbtn.grid(row=5, column=3 )

        delallicon = PhotoImage(file='../icons/delall.gif')
        delallbtn=Button(bottomframe, image=delallicon,borderwidth=0,padx=0, text='Clear All', command=self.clear_list)
        delallbtn.image = delallicon
        delallbtn.grid(row=5, column=4 )

        bottomframe.grid(row=5, sticky='w',padx=5)

    def add_file(self):
        filename = tkinter.filedialog.askopenfilename(filetypes=[('All supported', '.mp3 .wav'), ('.mp3 files', '.mp3'), ('.wav files', '.wav')])
            if filename:
                self.listbox.insert(END, filename)
                self.alltracks = list(self.listbox.get(0, END))


    def add_dir(self):
        path = tkinter.filedialog.askdirectory()
        if path:
            tfileList = []
            for (dirpath, dirnames, filenames) in os.walk(path):
                for tfile in filenames:
                    if tfile.endswith(".mp3") or tfile.endswith(".wav"):
                        tfileList.append(dirpath + "/" + tfile)
            for item in tfileList:
                self.listbox.insert(END, item)
            self.alltracks = list(self.listbox.get(0, END))


    def del_selected(self):
        while len(self.listbox.curselection()) > 0:
            self.listbox.delete(self.listbox.curselection()[0])
        self.alltracks = list(self.listbox.get(0, END))


    def clear_list(self):
        self.listbox.delete(0, END)
        self.alltracks = list(self.listbox.get(0, END))


