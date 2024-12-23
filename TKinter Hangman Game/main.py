class Application(Frame):
    """ GUI application which can retrieve an auto number to guess. """
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()