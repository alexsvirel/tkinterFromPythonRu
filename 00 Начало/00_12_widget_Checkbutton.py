"""
Добавление виджета Checkbutton (чекбокса)

С целью создания виджета checkbutton, используйте класс Checkbutton:
from tkinter.ttk import Checkbutton
chk = Checkbutton(window, text='Выбрать')

Кроме того, вы можете задать значение по умолчанию, передав его в параметр var в Checkbutton
"""
from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
chk_state = BooleanVar()
chk_state.set(True)  # в чекбоксе проставлена галка
# chk_state.set(False)  # в чекбоксе пусто
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()
