"""
Установка состояния виджета Checkbutton (второй способ)

Используйте IntVar вместо BooleanVar и установите значения 0 и 1.
"""
from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
# chk_state = BooleanVar() так было
# так стало:
chk_state = IntVar()
chk_state.set(0)    # False - галки нет
# chk_state.set(1)  # True  - галка есть

chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()
