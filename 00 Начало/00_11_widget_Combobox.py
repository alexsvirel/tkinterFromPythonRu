"""
Добавление виджета Combobox из ttk - виджет поля с выпадающем списком

добавляем элементы combobox, используя значения tuple.
Чтобы установить выбранный элемент, можно передать индекс нужного элемента текущей функции.
Чтобы получить элемент select, можно использовать функцию get: combo.get()

"""
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=0)
window.mainloop()
