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

if __name__ == '__main__':
    InputUI = InputMessageUI()
    InputUI.run()

    message, n = InputUI.message, InputUI.n

    App = AppSimulator(n=n, message=message)
    App.run()