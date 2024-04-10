import math # Модули в Python позволяют испортировать операции из заранее заготовленных файлов через встроенную команду from ... import ...
from Package import Other_Module as decorators # Это доступно как для встроенных модулей, так и самостоятельно написанных, упакованных в пакеты или находящихся рядом с исполняемым файлом


print (dir(math))


@decorators.decorator # Как пример -  работа декоратора, который находится вне исполняемого файла
def power (a,b):
    print (pow(a,b))


power (5,3)