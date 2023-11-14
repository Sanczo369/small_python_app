from tkinter import *

app = Tk()
app.title("Shopping List")

def createListinListBox(shopping):
    for elem in shopping:
        theList.insert(END,elem[0] + "-" + str(elem[1]))

def listIndex(shopping, item):
    index = -1
    for i in range(len(shopping)):
        if shopping[i][0] == item:
            index = i
    return index

def addList(shopping, item, index):
    if index == -1:
        shopping.append([item,1])
    else:
        shopping[index][1] += quantity.get()

def removeList(shopping, index):
    del(shopping[index])

def add():
    index = listIndex(shopping, item.get())
    addList(shopping, item.get(), index)
    if index >=0:
        theList.delete(index)
        theList.insert(index,shopping[index][0] + "-" + str(shopping[index][1]))
    else:
        theList.insert(END,item.get() + "-" + str(quantity.get()))

def remove():
    index = theList.index(ACTIVE)
    print(index)
    removeList(shopping, index)
    theList.delete(index)

theList = Listbox(app, selectmode=SINGLE)
theList.grid(row=0, column=0, columnspan=2, sticky=E)

item=StringVar()
quantity=IntVar()

quantity.set(1)

Label(app, text="Item:").grid(row=1, column=0, sticky=E)
Entry(app, textvariable=item).grid(row=1, column=1, sticky=W)

Label(app, text="Quantity:").grid(row=2, column=0, sticky=E)
Entry(app, textvariable=quantity).grid(row=2, column=1, sticky=W)

Button(app, text="Add").grid(row=3, column=0, columnspan=3)
Button(app, text="Remove").grid(row=0, column=3)

app.mainloop()