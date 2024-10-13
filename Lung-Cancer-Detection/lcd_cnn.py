class LCD_CNN:
    def __init__(self,root):
        self.root=root
        #window size
        self.root.geometry("1006x500+0+0")
        self.root.resizable(False, False)
        self.root.title("Lung Cancer Detection")
