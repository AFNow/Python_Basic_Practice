# Defaultdict - это объект, схожий по методике со словарем, который позволяет выдать стандартные данные для значения по умолчанию.
# Пример:
from collections import defaultdict
dictionary = defaultdict(int) # Выдача методики стандартного значения
lst = ['zero', 'zero', 'one', 'two', 'three', 'two']
for key in lst: # Внесение данных в словарь по методике [ключ] += 1, если значение повторяется
    dictionary[key] += 1
print(dictionary) #defaultdict(<class 'int'>, {'zero': 2, 'one': 1, 'two': 2, 'three': 1})

# Или способ сортировки значений из словаря по типу:
lst = [('one', 1), ('two', 2), ('one', 3), ('two', 4), ('three', 1)]
dictionary = {}
for key, value in lst:
    dictionary.setdefault(key, []).append(value)
sorted(dictionary.items())
print(dictionary)