"""
Добавление панели меню
"""
from tkinter import *
from tkinter import Menu

def clicked():
    pass # или что-то делать при выборе пункта меню

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
menu = Menu(window)
# меню с пунктирной линией, отделяющей меню в окно:
new_item = Menu(menu)
# чтобы отключить пунктирную линию есть команда tearoff=0
# new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый')
# при необходимости ставим разделитель между пунктами
new_item.add_separator()
new_item.add_command(label='Изменить')
# можно ввести любой код, который работает, при нажатии пользователем на элемент меню,
# задавая свойство команды command
new_item.add_command(label='Новый', command=clicked)

menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
window.mainloop()
