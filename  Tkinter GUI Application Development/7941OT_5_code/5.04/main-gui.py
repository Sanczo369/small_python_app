"""
Code illustration: 5.04

NEW ATTRIBUTES ADDED HERE
----------------------------


NEW METHODS ADDED HERE:
-------------------------
create_console_frame - to display the top display console
launch_play - to update display every time a new track is played
update_clock_and_progressbar - to update the clock and progressbar periodically when a track is playing.

METHODS MODIFIED:
-----------------------
identify_track_to_play
prev_track
next_track
- rather than calling playthread directly these 3 methods now call the
launch_play() method which takes care of console updation.

@Tkinter GUI Application Development Hotshot
"""
from Tkinter  import *
import tkFileDialog
import tkMessageBox
import ttk
import os
import time

import player

class GUI:
    alltracks = []
    indx=0
    currentTrack = ''
    timer = [0, 0] #corresponding to minutes and seconds
    timepattern = '{0:02d}:{1:02d}'

    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk()
        self.root.title('Media Player')
        self.root.iconbitmap('../icons/mp.ico')
        self.create_console_frame()
        self.create_button_frame()
        self.create_list_frame()
        self.create_bottom_frame()
        self.root.mainloop()

    def create_console_frame(self):
        cnslfrm = Frame(self.root)
        photo = PhotoImage(file='../icons/glassframe.gif')
        self.canvas = Canvas(cnslfrm, width=370, height=90)
        self.canvas.image = photo
        self.canvas.grid(row=1)
        self.console = self.canvas.create_image(0, 10, anchor=NW, image=photo)
        self.clock = self.canvas.create_text(32, 34, anchor=W, fill='#CBE4F6', font="DS-Digital 20",
                                             text="00:00")
        self.songname = self.canvas.create_text(115, 37, anchor=W, fill='#9CEDAC', font="Verdana 10",
                                                text='\"Currently playing: none [00.00] \"')
        self.progressBar = ttk.Progressbar(cnslfrm, length=1, mode="determinate")
        self.progressBar.grid(row=2, columnspan=10, sticky='ew', padx=5)

        cnslfrm.grid(row=1, pady=1, padx=0)

    def create_button_frame(self):
        buttonframe = Frame(self.root)
        previcon = PhotoImage(file='../icons/previous.gif')
        prevbtn=Button(buttonframe, image=previcon, borderwidth=0, padx=0, command=self.prev_track)
        prevbtn.image = previcon
        prevbtn.grid(row=3, column=1, sticky='w')

        rewindicon = PhotoImage(file='../icons/rewind.gif')
        rewindbtn=Button(buttonframe, image=rewindicon, borderwidth=0, padx=0, command=self.player.rewind)
        rewindbtn.image = rewindicon
        rewindbtn.grid(row=3, column=2, sticky='w')

        self.playicon = PhotoImage(file='../icons/play.gif')
        self.stopicon = PhotoImage(file='../icons/stop.gif')
        self.playbtn=Button(buttonframe, text ='play', image=self.playicon, borderwidth=0, padx=0, command=self.toggle_play_pause)
        self.playbtn.image = self.playicon
        self.playbtn.grid(row=3, column=3)

        fast_fwdicon = PhotoImage(file='../icons/fast_fwd.gif')
        fast_fwdbtn=Button(buttonframe, image=fast_fwdicon, borderwidth=0, padx=0, command=self.player.fast_fwd)
        fast_fwdbtn.image = fast_fwdicon
        fast_fwdbtn.grid(row=3, column=4)

        nexticon = PhotoImage(file='../icons/next.gif')
        nextbtn = Button(buttonframe, image=nexticon, borderwidth=0, padx=0, command=self.next_track)
        nextbtn.image = nexticon
        nextbtn.grid(row=3, column=5)

        self.muteicon = PhotoImage(file='../icons/mute.gif')
        self.unmuteicon = PhotoImage(file='../icons/unmute.gif')
        self.mutebtn=Button(buttonframe, image=self.unmuteicon, text='unmute', borderwidth=0,padx=0, command=self.toggle_mute)
        self.mutebtn.image = self.unmuteicon
        self.mutebtn.grid(row=3, column=6)

        self.volscale = ttk.Scale(buttonframe, from_=0.0, to=1.0, command=self.vol_update)
        self.volscale.set(0.6)
        self.volscale.grid(row=3, column=7, padx=5)

        buttonframe.grid(row=3, columnspan=5, sticky='w', pady=4, padx=5)

    def create_list_frame(self):
        list_frame = Frame(self.root)
        self.listbox = Listbox(list_frame, activestyle='none', cursor='hand2', bg='#1C3D7D', fg='#A0B9E9',
                               selectmode=EXTENDED, width=60, heigh=10)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.listbox.bind("<Double-Button-1>", self.identify_track_to_play)
        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        list_frame.grid(row=4, padx=5)

    def create_bottom_frame(self):
        bottomframe = Frame(self.root)
        add_fileicon = PhotoImage(file='../icons/add_file.gif')
        add_filebtn = Button(bottomframe, image=add_fileicon, borderwidth=0, padx=0, text='Add File',
                             command=self.add_file)
        add_filebtn.image = add_fileicon
        add_filebtn.grid(row=5, column=1)

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

        bottomframe.grid(row=5, sticky='w', padx=5)

    def add_file(self):
        filename = tkFileDialog.askopenfilename(
            filetypes=[('All supported', '.mp3 .wav'), ('.mp3 files', '.mp3'), ('.wav files', '.wav')])
        if filename:
            self.listbox.insert(END, filename)
            self.alltracks = list(self.listbox.get(0, END))

    def add_dir(self):
        path = tkFileDialog.askdirectory()
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
        while len(self.listbox.curselection())>0:
            self.listbox.delete(self.listbox.curselection()[0])
        self.alltracks = list(self.listbox.get(0, END))







