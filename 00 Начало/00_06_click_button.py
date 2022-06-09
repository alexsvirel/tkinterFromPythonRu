"""
Click button. Нажатие кнопки.
"""
from tkinter import *


# функция, которая будет выполнена при нажатии кнопки
def clicked():
    lbl.configure(text="Я же просил...")


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
# передача кнопке команды, назначенной для обработки события нажатия.
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
