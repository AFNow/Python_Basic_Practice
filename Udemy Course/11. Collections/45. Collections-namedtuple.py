# Namedtuple - объект, который является кортежем, но позволяет проименовать объекты внутри своей последовательности, по функционалу похож на менее обширный класс объекта. 
# Синтаксис: collections.namedtuple(typename, field_names, *, 
#                                   rename=False, defaults=None, module=None)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y', 'z']) # Указание названия самого класса кортежа, а потом его переменных
p = Point(x=1, y=2, z=3)
print (p)
print (p.x)
# Аналогично в этом кортеже работает вызов через индекс переменной
print (p[0])