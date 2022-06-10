"""
Добавление SpinBox (Виджет, который позволяет выбирать из фиксированного набора значений)
"""
from tkinter import *

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')

# задаем диапазон значений от/до: from_=0, to=100 и ширину виджета на экране:  width=5
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=0)

# можно указать числа для Spinbox, вместо использования всего диапазона следующим образом:
# spin = Spinbox(window, values=(3, 8, 11), width=5)
# Виджет покажет только эти 3 числа: 3, 8 и 11.

# если вам нужно задать значение по умолчанию для Spinbox,
# можно передать значение параметру textvariable следующим образом:#
# var = IntVar()
# var.set(36)
# spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

window.mainloop()