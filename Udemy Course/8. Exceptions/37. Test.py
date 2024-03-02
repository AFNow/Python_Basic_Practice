# Обработайте исключение, которое вызывает код ниже:
def ixx2():
    try:
        for i in ['a','b','c']:
            print (i**2)
    except:
        print ('Невозможно возвести в степень')
    

# Обработайте исключение, которое вызывает код ниже, а затем использовать finally для завершения.
def zero():    
    x = 5
    y = 0
    try:
        z = x/y
        print(z)
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
    finally:
        print('Завершение скрипта zero()')

# Напишите код, который просит ввести число, а потом возвращает это число в квадрате
def twice():
    while True:
        try:
            integer = float(input('Введите число для возведения в степень:'))
            print (integer**2)
            break
        except TypeError:
            print('Это не число')
            break
        except ValueError:
            print('Это не число')
            break
        finally:
            print('Завершение')
    pass

ixx2()
zero()
twice()