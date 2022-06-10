"""
Добавление поля загрузки файла (filedialog)
"""
# Возможность указания типа файлов доступна при использовании параметра filetypes,
# однако при этом важно указать расширение в tuples.
#
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
#
# Вы можете запросить каталог, используя метод askdirectory :
#
# dir = filedialog.askdirectory()
#
# Вы можете указать начальную директорию для диалогового окна файла, указав initialdir следующим образом:
#
# from os import path
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
