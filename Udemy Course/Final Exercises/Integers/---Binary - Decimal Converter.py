def Converter():# Перевод бинарных чисел в десятичные и обратно** - Напишите программу, которая переводит десятичное число в бинарное, или бинарное число в десятичное.
    binary_to_decimal = None
    answer = input ('Требуется перевод из десятичной системы в двоичную? ')
    if answer.lower() == 'да':
        binary_to_decimal = False
        number = input('Введите число: ')
    else:
        binary_to_decimal = True
        number = input('Введите число: ')

    def binary_decimal(binary_to_decimal, number):
        answer = ''
        if binary_to_decimal == False: # Десятичное число в бинарное
            number = int(number)
            print ('Десятичное число', number, 'в бинарное')
            while number > 1:
                number = int(number)
                number = number / 2
                if number.is_integer():
                    answer += '0'
                    continue
                else:
                    answer += '1'
                    continue
            else:
                print(answer[::-1])
        else: # Бинарное в десятичное 
            answer = 0
            print ('Бинарное число ', number,'в десятичное')
            number_list = list(number)
            count = len(number_list)-1
            print (count)
            print (number_list)
            for item in number_list:
                answer += int(item) * (2**count)
                count -= 1
                continue
            print (answer)
    binary_decimal(binary_to_decimal, number)
Converter()