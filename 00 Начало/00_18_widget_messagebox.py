"""
Создание всплывающего окна с сообщением, предупреждением, сообщением об ошибке
"""
from tkinter import *
from tkinter import messagebox


def clicked():
    # всплывающее окно с сообщением
    messagebox.showinfo('Заголовок', 'Текст')
    # либо всплывающее окно с пердупреждением
    messagebox.showwarning('Заголовок', 'Текст')  # показывает предупреждающее сообщение
    # либо всплывающее окно с сообщением об ошибке
    messagebox.showerror('Заголовок', 'Текст')  # показывает сообщение об ошибке


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
btn = Button(window, text='Клик', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()
