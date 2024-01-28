import tkinter as tk
from tkinter import messagebox
from time import sleep
import random

def cls_termninal() -> None:
    import sys, subprocess

    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    elif operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)

def processing_text_input(text: str) -> tuple[list[str], list[str]]:
    splitted_text = text.split(" ")
    return ['  '.join(word) for word in splitted_text], ['\n'.join(column) for column in zip(*splitted_text)]

def get_widget_size(widget: tk.Label | tk.Button) -> tuple[int, int]:
    return widget.winfo_reqwidth(), widget.winfo_reqheight()


def generate_broken_message(array: list[str], indicator: list[bool], orient: str) -> tuple[list[str], list[bool]]:
    """
    array       : list of words/packets
    indicator   : [True, False, ...]
    orient      : 'row' | 'col'
    """

    orient = orient.lower()
    n = len(array)

    result = [None] * n

    text_length = len(array[0])
    for i in range(n):
        if indicator[i]:
            if orient == 'row':
                result[i] = "#" * text_length
            elif orient == 'col':
                current_message = array[i].replace('\n', '')

                result[i] = "#\n" * len(current_message)
                result[i] = result[i][:-1]
            else:
                raise TypeError('orient parameter only take \'row\' or \'col\'')
        else:
            result[i] = array[i]

    return result, indicator


class InputMessageUI():
    def __init__(self) -> None:
        self.message: str = 0
        self.n: int = 0

        self.root = tk.Tk()
        self.message_label = None
        self.small_note = None
        self.message_entry = None

        self.n_label = None
        self.n_entry = None

        self.lets_go_button = None
        self.error_input_text = None

        # self.is_input_correct = False

        self.WIN_WIDTH = 920
        self.WIN_HEIGHT = 508
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        x = (self.screenwidth // 2) - (self.WIN_WIDTH // 2)
        y = (self.screenheight // 2) - (self.WIN_HEIGHT // 2)

        # small_icon = tk.PhotoImage(file="assets/icons8-thin-client-70.png")
        # large_icon = tk.PhotoImage(file="assets/icons8-thin-client-70.png")
        # self.root.iconphoto(False, large_icon, small_icon)
        self.root.title("Computer Network Interleaving Simulator")
        self.root.configure(bg="#93B1A6")
        self.root.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}+{x}+{y}")

    def validate_input(self):
        splitted_message = self.message.split(" ")
        longest_string = max(splitted_message, key=len)

        if len(self.message) == 0:
            self.error_input_text.config(text="Please provide a message", fg="blue")
            self.error_input_text.pack(side="top", pady=(40, 0))
            return False
        elif len(longest_string) > 8:
            self.error_input_text.config(text="Packets with more than 8 characters is not allowed!", fg="red")
            self.error_input_text.pack(side="top", pady=(40, 0))
            return False
        elif len(splitted_message) > 8:
            self.error_input_text.config(text="Please input no more than 8 words/packets", fg="blue")
            self.error_input_text.pack(side="top", pady=(40, 0))
            return False
        elif len(self.n) == 0:
            self.error_input_text.config(text="Please input number of broken words/packets", fg="blue")
            self.error_input_text.pack(side="top", pady=(40, 0))
            return False
        elif int(self.n) > min(len(longest_string), len(splitted_message)):
            self.error_input_text.config(text="Number of broken packets is too big!", fg="red")
            self.error_input_text.pack(side="top", pady=(40, 0))
            return False
        elif int(self.n) < 0:
            self.error_input_text.config(text="Number of broken packets must be positive!", fg="red")
            self.error_input_text.pack(side="top", pady=(40, 0))
            return False

        splitted = self.message.split(" ")
        if len(splitted) < 8:
            splitted.extend(["_" * 8] * (8 - len(splitted)))

        temp = " ".join([s.ljust(8, "_") for s in splitted])
        # print(temp)
        self.message = temp

        self.n = int(self.n)
        return True


if __name__ == '__main__':
    InputUI = InputMessageUI()
    InputUI.run()

    message, n = InputUI.message, InputUI.n

    App = AppSimulator(n=n, message=message)
    App.run()