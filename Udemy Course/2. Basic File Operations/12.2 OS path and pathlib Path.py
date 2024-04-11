# Функция abspath() модуля os.path вернет нормализованную абсолютную версию пути. 
# На большинстве платформ это эквивалентно вызову функции os.path.normpath() следующим образом: os.path.normpath(join(os.getcwd(),path)).
# Абсолютный - это полный путь от корневой директории диска, до файла. 
from os import path 
    # os.path.abspath(path) - возвращает нормализованный абсолютный путь.
    # os.path.basename(path) - базовое имя пути (эквивалентно os.path.split(path)[1]).
    # os.path.commonprefix(list) - возвращает самый длинный префикс всех путей в списке.
    # os.path.dirname(path) - возвращает имя директории пути path.
    # os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
    # os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.
    # os.path.expandvars(path) - возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name). Несуществующие имена не заменяет. На Windows также заменяет %name%.
    # os.path.getatime(path) - время последнего доступа к файлу, в секундах.
    # os.path.getmtime(path) - время последнего изменения файла, в секундах.
    # os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).
    # os.path.getsize(path) - размер файла в байтах.
    # os.path.isabs(path) - является ли путь абсолютным.
    # os.path.isfile(path) - является ли путь файлом.
    # os.path.isdir(path) - является ли путь директорией.
    # os.path.islink(path) - является ли путь символической ссылкой.
    # os.path.ismount(path) - является ли путь точкой монтирования.
    # os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
    # os.path.normcase(path) - нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).
    # os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.
    # os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).
    # os.path.relpath(path, start=None) - вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).
    # os.path.samefile(path1, path2) - указывают ли path1 и path2 на один и тот же файл или директорию.
    # os.path.sameopenfile(fp1, fp2) - указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.
    # os.path.split(path) - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
    # os.path.splitdrive(path) - разбивает путь на пару (привод, хвост).
    # os.path.splitext(path) - разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.
    # os.path.supports_unicode_filenames - поддерживает ли файловая система Unicode

# directory = '.' # Текущая директория
# abs = path.abspath(directory)# Этот метод позволяет получить абсолютный путь к текущей директории
# print (abs)
# print (path.isdir(abs))


from pathlib import Path # Аналогично работает pathlib, но только через класс объекта, с созданием пути как объекта
cwd = Path('.') # . Означает текущую директорию
print (Path.cwd()) # Вызов адреса Current Working Directory
print (cwd.absolute())
newpath = (Path ('G:/') / 'My Drive' / 'Code' / 'Python Course' / 'NewDirectory')
if not newpath.exists():
    newpath.mkdir() # Создание нового каталога
cwd = Path ('G:\My Drive\Code\Python Course\Basics\Python_Basic_Practice')
print([dir for dir in cwd.iterdir() if dir.is_dir()]) # Показывает все доступные в текущей директории папки
# https://docs.python.org/3/library/pathlib.html - More about the pathlib module
with open ('textfile.txt', 'r+', encoding='utf-8') as file:
    for line in file:
        print (line)
