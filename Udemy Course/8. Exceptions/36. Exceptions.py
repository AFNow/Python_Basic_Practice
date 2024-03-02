# Система ошибок и исключений позволяет использовать встроенные ошибки python в самом коде, чтобы планировать исходы их появления.
# При появлении в коде ошибки, происходит остановка работы всего скрипта, но при использовании системы исключений, можно избежать или создать предупреждение самой ошибки
# Для этого есть три ключевые команды:
# try: - Попытка использовать часть кода, который может в последствии привести к ошибке.
# except: - Часть кода, которая выполняется в случае, если произошла ошибка в предыдущем блоке кода
# finally: - Финальный код, который выполняется вне зависимости, произошла ошибка, или нет
# Пример:
# n1 = int(input('Введите число n1')) Примером может послужить ошибка TypeError, возникающая при сложении разых типов данных
#     n2 = input('Введите число n2')
#     x = n1+n2
#     print (x)
# Исправить его можно таким образом:
try:
    n1 = int(input('Введите число n1:'))
    n2 = input('Введите число n2:')
    x = n1+n2
    print (x)
except ValueError: # Может быть указан конкретный вид ошибки, или же общее except:, которое будет выдавать единый ответ на любые возникающие ошибки
    print ('Одна из переменных не является числом')
finally:
    print('Конец программы')
# Схожим примером может быть такая ситуация:
try:
    with open('testfile', 'w+', encoding='utf-8') as file: # Файл создается, но в последствии, если изменить его режим на "только для чтения", исключение начнет работать
        userinput = input('Введите строку для добавления в файл:')
        file.write(userinput)
        file.seek(0)  # Перемещаем указатель в начало файла
        print(file.read())
        file.close()
except OSError:
    print ('Файл находится в режиме "только для чтения"')
finally:
    print('Запись окончена')

# Также примером применения является рабоат цикла:
def ask_for_int ():
    while True:
        try:
            integer = int(input('Введите число:'))
        except:
            print('Это не число')
            continue
        else:
            print ('Число введено')
            break
ask_for_int ()
