# Итерируемые циклы for предназначенны для переберания данных в переменной
# Имеют синтаксис:
IterableString = 'String Value'     #Указание данных, над которыми будет проводиться итерация
IterableList = [1,2,3,4,5,6]
IterableTuple = (1,2,3,4,5,6)
IterableDictionary = {'key1': 1, 'key2': 2, 'key3': 3}
IterablePackedTuples = [(1,2,3),(4,5,6),(7,8,9)]
# Печать каждого символа в переменной string
for item_name in IterableString:
    print (item_name)
pass
#Печать всех пунктов списка, с указанием четности или нечетности пункта
for item_name in IterableList:
    if item_name % 2 == 0:
        print('Четное число: ', item_name)
    else:
        print ('Не четное число: ', item_name)
pass
# Печать каждого пункта списка, кроме пункта, равного 2 и 5, разными способами запроса, для них выдается печать слова 'два' и 'пять'
for item_name in IterableTuple:
    if item_name != 2:
        print (item_name)
    elif item_name == 5:
        print ('пять') 
    else:
        print ('два')
pass 
# Печать каждого ключа и параметра, привязанного к нему
for item in IterableDictionary: # Для получения доступа только к значениям, нужно указывать .values
    print (item)
pass
sum1 = 0
for (item1, item2, item3) in IterablePackedTuples:
    sum1 = item1 + item2 + item3 + sum1
print (sum1)