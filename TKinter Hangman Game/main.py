class Application(Frame):
    """ GUI application which can retrieve an auto number to guess. """
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """

        """ Instruction Label """

        # Create instruction label for Program
        self.inst_lbl = Label(self, text="Welcome to Guess the Word!")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        """ Guess Input """

        # Create label for entering Guess
        self.guess_lbl = Label(self, text="Enter your Guess:")
        self.guess_lbl.grid(row=2, column=0, sticky=W)

        # Create entry widget to accept Guess
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        # Create a space
        self.gap1_lbl = Label(self, text = " ")
        self.gap1_lbl.grid(row = 3, column = 0, sticky = W)

        """ Submit Button """

        # Creating a submit button
        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=6, column=0, sticky=W)

        # Create a space
        self.gap2_lbl = Label(self, text = " ")
        self.gap2_lbl.grid(row = 7, column = 0, sticky = W)

        """ RESET """

        # Creating a reset button
        self.reset_bttn = Button(self, text="Reset", command=self.reset)
        self.reset_bttn.grid(row=6, column=1, sticky=W)

        """ Display """

        # Create text widget to display welcome_msg
        self.display1_txt = Text(self, width=45, height=1, wrap=WORD)
        self.display1_txt.grid(row=8, column=0, columnspan=2, sticky=W)

        # Create text widget to display guess_msg
        self.display2_txt = Text(self, width=45, height=1, wrap=WORD)
        self.display2_txt.grid(row=9, column=0, columnspan=2, sticky=W)

        # Create text widget to display result_msg
        self.display3_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display3_txt.grid(row=10, column=0, columnspan=2, sticky=W)

        # Create text widget to display tries_msg
        self.display4_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display4_txt.grid(row=11, column=0, columnspan=2, sticky=W)

        # Create text widget to display word_msg
        self.display5_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display5_txt.grid(row=12, column=0, columnspan=2, sticky=W)
