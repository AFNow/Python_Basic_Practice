print('Элемент списков позволяет составлять небольшой массив данных, указанный в виде str, int или float')
list1 = []
print('Рост:')
data= (input ())
list1.append(data)
print('Вес:')
data= (input ())
list1.append(data)
print('Пол')
data= (input ())
list1.append(data)
print(list1)
print('Данные укзааны в одном общем списке')
print('Также к спискам может быть применена индексация, срезы и конкотинация')
list2 = []
print('Указать имя')
name= (input ())
list2.append(name)
print('Указать фамилию')
lastname= (input ())
list2.append(lastname)
print('Указать год рождения')
year= (input ())
list2.append(year)
print(list2[:2]) #Срез после первого индекса
print('Фамилия -',list2[1], ', Имя - ',list2[0], ', год - ',list2[2]) #Непоследовательная индексация
summary = list2 + list1 #Конкотинация списков
print('Пол - ',summary[5], ', Рост - ',summary[3], ', Вес - ',summary[4], ', Фамилия - ',summary[1], ', Имя - ',summary[0], ', Год рождения - ',summary[2] )
