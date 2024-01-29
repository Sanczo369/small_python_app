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

    def lets_go_button_event(self):
        self.message = str(self.message_entry.get()).strip()
        self.n = str(self.n_entry.get()).strip()

        is_verified = self.validate_input()

        if is_verified:
            # print("DONE")
            self.error_input_text.pack_forget()
            self.root.destroy()

    def initialize(self):
        # Message
        self.message_label = tk.Label(
            self.root,
            text="Input message",
            font=("Fira Code", 14, "bold"),
            width=25
            )
        self.message_label.pack(side='top', pady=(92,0))
        self.small_note = tk.Label(
            self.root,
            text="max. 8 words/packets",
            font=("Fira Code", 9),
            width=22
            )
        self.small_note.pack(side='top', pady=(0,0))
        self.message_entry = tk.Entry(
            self.root,
            width=74,
            justify='center',
            font=("Fira Code", 14)
            )
        self.message_entry.insert(0, "matahari membakar sebagian material berwarna kebiruan 01234567")
        self.message_entry.pack(side='top')

        # n
        self.n_label = tk.Label(
            self.root,
            text="Number of broken packets",
            font=("Fira Code", 14, "bold"),
            width=29
        )
        self.n_label.pack(side='top', pady=(30, 0))
        self.n_entry = tk.Entry(
            self.root,
            width=25,
            justify='center',
            font=("Fira Code", 14)
        )
        self.n_entry.insert(0, 3)
        self.n_entry.pack(side='top')

        # Let's go button
        self.lets_go_button = tk.Button(
            self.root,
            text="Let's go",
            font=("Fira Code", 14, "bold"),
            width=16,
            command=self.lets_go_button_event
        )
        self.lets_go_button.pack(side='top', pady=(50, 0))

        # error message
        self.error_input_text = tk.Label(
            self.root,
            text="",
            font=("Fira Code", 10),
            width=57
        )

    def run(self):
        self.initialize()
        self.root.mainloop()


class AppSimulator():
    def __init__(self, n: int, message: str):
        self.root = tk.Tk()
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.row_message, self.col_message = processing_text_input(message)

        self.is_running = False
        self.font_FiraCode = "Fira Code"

        # -------------------------------------------------------------
        # font_root = font.Font(family="Inter", size=60)

        # self.root.option_add("*Font", font_root)
        self.bg_root = "#93B1A6"
        self.xy_color_label = "#ffffff"
        self.root.configure(bg=self.bg_root)

        self.root.title("Computer Network Interleaving Simulator")
        self.root.attributes('-fullscreen', True)
        # self.root.geometry(f"{int(self.screenwidth/1.15)}x{int(self.screenheight/1.15)}")
        # self.root.state('zoomed')  # Maximize screen

        # Icon App
        # small_icon = tk.PhotoImage(file="assets/icons8-thin-client-70.png")
        # large_icon = tk.PhotoImage(file="assets/icons8-thin-client-70.png")
        # self.root.iconphoto(False, large_icon, small_icon)
        # -------------------------------------------------------------

        self.x = []
        self.y = []
        self.x_start, self.x_initial = 138, 138
        self.y_start, self.y_initial = 250, 250

        # Exit button
        self.exit_button = None

        # Header label
        self.header = None

        self.sender_text = None
        self.info_text, self.info_text_indicator = None, []
        self.reciever_text = None
        self.interleaving_explenation_text = None
        self.post_text = None

        # Normal simulation button
        self.normal_button = None

        # Reset button
        self.restart_button = None

        # Interleaving simulation button
        self.simulation_button = None

        # x label
        self.x_labels = []
        self.x_label_width = 0  # 260
        self.x_label_height = 0  # 50

        # y label
        self.y_labels = []
        self.y_label_width = 0
        self.y_label_height = 0

        # Create random broken message
        indicator = [True] * n + [False] * (abs(8 - n))
        random.shuffle(indicator)

        self.broken_row_message, self.row_indicator = generate_broken_message(self.row_message, indicator, orient='row')
        self.broken_col_message, self.col_indicator = generate_broken_message(self.col_message, indicator, orient='col')

        # self.col_message = self.broken_col_message
        # self.row_message = self.broken_row_message

    def wait_in_the_middle(self, n:int=100):
        for _ in range(n):
            if self.is_running:
                self.root.update()
                sleep(0.002)
            else:
                return "RESTART"

    def pop_up_info_text(self, i):
        # pop up info text
        self.info_text_indicator.append(i+1)
        self.info_text = tk.Label(self.root,
            text=f"Oops! Paket data ke {self.info_text_indicator} rusak",
            font=(self.font_FiraCode, 11),
            fg='red'
            )
        _info_text_width = get_widget_size(self.info_text)[0]
        self.info_text.place(x=self.screenwidth//2 - _info_text_width//2, y=160, width=_info_text_width + 30)
if __name__ == '__main__':
    InputUI = InputMessageUI()
    InputUI.run()

    message, n = InputUI.message, InputUI.n

    App = AppSimulator(n=n, message=message)
    App.run()