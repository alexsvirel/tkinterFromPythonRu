"""
Показ диалоговых окон с выбором варианта
"""
from tkinter import *
from tkinter import messagebox


def clicked():
    """
    Можно выбрать соответствующий стиль сообщения согласно вашим потребностям.
    Кроме того, можно проверить, какая кнопка нажата, используя переменную результата.

    Если вы кликнете OK, yes или retry, значение станет True,
    а если выберете NO или Cancel, значение будет False.

    Единственной функцией, которая возвращает одно из трех значений,
    является функция askyesnocancel; она возвращает True/False/None.
    """
    messagebox.askquestion('Заголовок', 'Текст')
    # messagebox.askyesno('Заголовок', 'Текст')
    # messagebox.askyesnocancel('Заголовок', 'Текст')
    # messagebox.askokcancel('Заголовок', 'Текст')
    # messagebox.askretrycancel('Заголовок', 'Текст')


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
btn = Button(window, text='Клик', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()
