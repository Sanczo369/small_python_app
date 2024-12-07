import tkinter as tk
import pyshorteners
import os
import sys

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
        return os.path.join(bundle_dir, relative_path)
    base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)