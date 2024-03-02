# Напиши программу, которая запрашивает у пользователя числа до тех пор, пока он не введет слово “стоп”. 
# После этого программа должна вывести на экран сумму всех введенных чисел.
x = 0
while x != -1:
    i = input('Введите число для суммирования: ')
    if i == 'stop':
        break
    try:
        number = int(i) 
        x = x + number
    except ValueError:
        print('Неверное значение')
print (x)
