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