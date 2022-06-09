"""
Изменение цвета текста и фона у Button
"""
"""
Добавление виджета Button (кнопки)
"""
from tkinter import *

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

btn = Button(window, text="Не нажимать!", bg="black", fg="red")
btn.grid(column=1, row=0)

window.mainloop()

