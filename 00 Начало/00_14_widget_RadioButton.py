"""
Добавление виджетов Radio Button
"""
from tkinter import *
from tkinter.ttk import Radiobutton

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
# добавляем три Radiobutton.
# Нужно установить уникальный value для каждой radio кнопки,
# иначе они не будут работать.
rad1 = Radiobutton(window, text='Первый', value=1)
rad2 = Radiobutton(window, text='Второй', value=2)
rad3 = Radiobutton(window, text='Третий', value=3)
# можно задать command любой из этих кнопок для определенной функции.
# Если пользователь нажимает на такую кнопку, она запустит код функции:
# rad1 = Radiobutton(window,text='Первая', value=1, command=clicked)
# def clicked():
#    # делает что нужно

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
window.mainloop()
