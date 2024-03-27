dictionary = {}
count = 0
while count < 3:
    count += 1
    key = input ('Название ключа: ')
    value = input ('Его значение ')
    dictionary[key] = value
print (dictionary)
key = input ('Название ключа запроса: ')
print (dictionary.get(key, 'Такого ключа не найдено'))