"""
Настройка содержимого Scrolledtext

для настройки текстового поля используем метод insert
для удаления содержимого текстового поля используем метод delete
"""
from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
# для настройки текстового поля используем метод insert:
txt.insert(INSERT, 'Текстовое поле')
# для удаления содержимого текстового поля используем метод delete
# txt.delete(1.0, END)  # мы передали координаты очистки
window.mainloop()