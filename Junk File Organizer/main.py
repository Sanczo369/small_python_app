import os
import shutil
from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog

file_types={
   'Documents' : ('.pdf','.doc','.xls','txt','.csv','.xml','.zip', '.docx', '.DOCX', '.odt'),
   'Pictures' : ('.jpg','.jpeg','.png','.JPG', '.webp'),
   'Videos' : ('.mp4','.mkv','.3gp','.flv','.mpeg'),
   'Music' : ('.mp3','.wav','.m4a','.webm'),
   'Programs' : ('.py','.cpp','.c','.sh','.js'),
   'Apps' : ('.exe','.apk'),
}