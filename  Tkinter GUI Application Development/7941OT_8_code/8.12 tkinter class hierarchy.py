"""
Code illustration: 8.12
Tkinter Class Hierarchy Inspect
Tkinter GUI Application Development Hotshot
"""
import tkinter
import inspect

print('Class Hierarchy for Frame Widget')
for i, classname in enumerate(inspect.getmro(tkinter.Frame)):
    print(f'{i}: {classname}')
