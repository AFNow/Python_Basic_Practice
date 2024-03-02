# Создание модулей и пакетов позволяет запускать скриптовые файлы из других файлов, а также заимствовать отдельные модули функций, или данные.
# Модулями являются сами скрипты .py, а пакетами является директория, в которой находятся связанные между собой файлы модулей .py
# В данном случае иерархия программы запустит последовательно два скрипта в файлах SupScript.py и MainScript.py, которые находятся в соседних папках от этой темы курса. 
from MainFolder.MainScript import maindef
from MainFolder.SubFolder.SubScript import subscript
maindef()
subscript()
# Таким образом оба эти модуля были запущены из этого конкретного файла.
# Также важным замечанием является файл __init__.py
# Файл __init__.py - это особый файл в Python, который используется для указания, 
# что директория, содержащая файл, является пакетом. В этом файле можно объявлять функции, 
# классы, переменные и импортировать другие модули, чтобы их можно было использовать внутри пакета.
