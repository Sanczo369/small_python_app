import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import time

class Pomodoro:
	def __init__(self, root):
		self.root = root