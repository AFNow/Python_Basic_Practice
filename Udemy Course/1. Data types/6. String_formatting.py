print('Форматирование строк позволяет встраивать переменные в заранее подготовленные строки.')
print('Первый - более старый метод - .format()')
print('Позволяет {1} {0} {2}, которыми также могут являться переменные' .format('форматируемые','добавлять','данные'))
print('Или {p} {i} {z} ' .format(p='присваивать',i='имена',z='значений'))
print('Также форматирование строки позволяет настроит выдачу данных float, в частности нецелых значений или в периоде')
print('z=x/y')
x=int (input ())
y=int (input ())
z=x/y
print('Результат без форматирования: {Z}' .format(Z=z))
print('Результат c форматированием: {Z:7.4}' .format(Z=z))
#Форматирование строится по типу "{value:width.precisionf}", где width - ширина строки целиком, а precision - это количество знаков после целого
print('Второй - f-strings')
print('Работает схоже, но упрощает оформление')
print(f'Результат: {z:{10}.{6}}')
