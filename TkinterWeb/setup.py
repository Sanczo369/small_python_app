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

if __name__ == '__main__':
    InputUI = InputMessageUI()
    InputUI.run()

    message, n = InputUI.message, InputUI.n

    App = AppSimulator(n=n, message=message)
    App.run()