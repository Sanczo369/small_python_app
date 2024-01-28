import tkinter as tk
from tkinter import messagebox
from time import sleep
import random

if __name__ == '__main__':
    InputUI = InputMessageUI()
    InputUI.run()

    message, n = InputUI.message, InputUI.n

    App = AppSimulator(n=n, message=message)
    App.run()