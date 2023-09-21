from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")
label1 = Label(root,text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)
f=Frame(root, bg="Black", bd=5, width=440, height=210)
f.place(x=10, y=118)
text1=Text(f,font="Robote 20", bg="white",width=430, height=200, relief=GROOVE, wrap=WORD)
text1.place(x=0,y=0)
scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")
label2 = Label(root,text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)
f1=Frame(root, bg="Black", bd=5, width=440, height=210)
f1.place(x=620, y=118)
text2=Text(f,font="Robote 20", bg="white",width=430, height=200, relief=GROOVE, wrap=WORD)
text2.place(x=0,y=0)
scrollbar2=Scrollbar(f)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)
root.configure(bg="white")
root.mainloop()
