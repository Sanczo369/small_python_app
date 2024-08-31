import Tkinter as tk


class GUIFramework(object):
    """
    GUIFramework is a class that provides a higher level of abstraction for
    the development of Tkinter graphic user interfaces (GUIs).
    Every class that inherits from GUIFramework can define its own menuitems
    attribute, which is a tuple of a form where each item is a string of the
    format 'MenuName - MenuButtonName/Accelrator/Commandcallback/Underlinenumber'.
    MenuSeparator is denoted by a string 'Sep'.

    For instance, passing this tuple as an argument to this method

        mymenuitems = (
                      'File - &New/Ctrl+N/new_file, &Open/Ctrl+O/openfile, &Save/Ctrl+S/save, Save&As//saveas, Sep, Exit/Alt+F4/close',
                      'Edit - Cut/Ctrl+X/cut, Copy/Ctrl+C/copy, Paste/Ctrl+V/paste, Sep',
                      )

    will generate a File and Edit Menu Buttons with listed menu items for each of the buttons.
    """
    menuitems = None

    def __init__(self, root):
        self.root = root
        if self.menuitems is not None:
            self.build_menu()

    def build_menu(self):
        self.menubar = tk.Menu(self.root)
        for v in self.menuitems:
            menu = tk.Menu(self.menubar, tearoff=0)
            label, items = v.split('-')
            items = map(str.strip, items.split(','))
            for item in items:
                self.__add_menu_command(menu, item)
            self.menubar.add_cascade(label=label, menu=menu)
        self.root.config(menu=self.menubar)

    def __add_menu_command(self, menu, item):
        if item == 'Sep':
            menu.add_separator()
        else:
            name, acc, cmd = item.split('/')
            try:
                underline = name.index('&')
                name = name.replace('&', '', 1)
            except ValueError:
                underline = None
            menu.add_command(label=name, underline=underline,
                           accelerator=acc, command=eval(cmd))
