print('Конкатинация параметров String в одну общую переменную')
print('Укажите первый параметр')
str1: str = input ()
print('Укажите второй параметр')
str2: str = input ()
if len (str1) > len (str2): #Сравнение длины строк
    result = str1 + " " + str2 #Без указания параметра кавычек текст выдается слитно
    print (result.title()) #При любом изначальном указании, результат будет указываться с заглавной буквы
else:
    result = str2 + " " + str1
    print (result.title())
