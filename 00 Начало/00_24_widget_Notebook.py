"""
Добавление виджета Notebook (Управление вкладкой)
"""
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')
lbl1 = Label(tab1, text= 'Вкладка 1')
lbl1a = Label(tab1, text='Вкладка 1a')
lbl1.grid(column=0, row=0)
lbl1a.grid(column=0, row=1)
# виджетам можно задавать отступы для элементов управления, чтобы они
# выглядели хорошо организованными с использованием свойств padx иpady
lbl2 = Label(tab2, text='Вкладка 2', padx=5, pady=5)
lbl2a = Label(tab2, text='Вкладка 2', padx=5, pady=5)
lbl2.grid(column=0, row=0)
lbl2a.grid(column=0, row=1)
tab_control.pack(expand=1, fill='both')
window.mainloop()

