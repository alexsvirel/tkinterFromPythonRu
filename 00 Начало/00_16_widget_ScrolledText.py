"""
Добавление виджета ScrolledText (текстовая область Tkinter)

Сразу задать размеры текстовой области!
"""
from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
# нужно задать ширину и высоту виджета, иначе она заполнит все окно
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
window.mainloop()