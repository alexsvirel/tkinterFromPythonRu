"""
Добавление виджета Progressbar (панель для отображения хода выполнения задачи)
"""
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
style = ttk.Style()
style.theme_use('default')
# Задаем стиль Progressbar:
style.configure("black.Horizontal.TProgressbar", background='black')
# Сзодаем Progressbar:
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
# ecnfyjdrf pyfxtybz Progressbar:
bar['value'] = 70
bar.grid(column=0, row=0)
window.mainloop()