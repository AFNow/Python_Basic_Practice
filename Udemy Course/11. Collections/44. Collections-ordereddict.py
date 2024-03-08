# Ordereddict - это объект, который является словарем, с функцией записи последовательности записанных данных.
# *** Последние версии Python имеют эту функцию заранее встроенной в обыкновенный dict объект, но в ранних версиях порядок добавленных данных мог меняться при вызове
# Пример:
from collections import OrderedDict
dictionary1 = OrderedDict()
dictionary1['one'] = 1
dictionary1['two'] = 2
dictionary2 = OrderedDict()
dictionary1['two'] = 2
dictionary1['one'] = 1
print (dictionary1 == dictionary2)

# Более актуальным примером может послужить функция класса, который запоминает последний порядок вставки ключей. 
# Если новая запись перезаписывает существующую запись, исходная позиция вставки изменяется и перемещается в конец:
class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
dictionary1 = LastUpdatedOrderedDict()
dictionary1['one'] = 1
dictionary1['two'] = 2
dictionary1['one'] = 1
print (dictionary1)