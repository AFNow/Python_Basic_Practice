def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    
    return inverted_dict

# Тестовые данные
print(invert_dict({'a': 1, 'b': 2, 'c': 2})) 
# должно вернуть {1: ['a'], 2: ['b', 'c']}
# Напишите функцию invert_dict, которая принимает словарь и возвращает новый словарь, в котором ключи и значения исходного словаря поменяны местами. 
# Если в исходном словаре есть одинаковые значения, то в возвращаемом словаре для этих значений создайте список ключей.