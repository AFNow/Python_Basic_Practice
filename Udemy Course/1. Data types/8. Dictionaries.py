print ("Словари - это неупорядоченный маппинги данных по типу {'key1':'value1','key2':'value2'}")
dictionary = {
'name':'Pavel','number':'+7 777 777 77 77','email':'address@mail.cc'
}
print ("Для обращения к данным в словаре требуется их ключ по типу")
print (dictionary['name'])
print (dictionary['number'])
print (dictionary['email'])

# Распаковка словаря - оператор, позволяющий добавлять данные из одного словаря в другой
dictionary2 = {**dictionary,
'card': '9283042981721'
}
print (dictionary2)
# Если использовать уже имеющийся ключ, то его значение будет перезаписано

# Также для объединения двух словарей может быть использован оператор |
dictionary3 = {
'pin':'324'    
}
full_dict = dictionary2 | dictionary3
print (full_dict)
# Важность имеют последовательности их объединения, при повторяющихся ключах, их данные также перезаписываются

# Dictionary Unpacking
profile = {
    'name' : 'Drew'
    ,'qty'  : 50
    }

def user_info(name, qty=0): # Функция распаковывает ключи и данные словаря, назначая их на имена переменных
    if not qty:
        return f"{name} has no qty"
    return f"{name} has {qty}"
print (user_info(**profile)) # Для распаковки используется оператор **, ограничением ивляется количество пунктов в словаре