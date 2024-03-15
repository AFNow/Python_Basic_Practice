def happy_numbers():# Счастливые числа (happy numbers, не путать в lucky numbers)** - Счастливое число определяется следующим образом. Начинаем с любого положительного числа. 
# Берём это число, и заменяем его суммой квадратов всех его цифр. Повторяем процесс до тех пор, пока число не станет равным 1. Например, число 19 является счастливым:
# Если процесс бесконечно продолжается и не заканчивается на 1, то такое число не считается счастливым. Найдите первые 8 счастливых чисел.
    def is_happy(num): # Проверка через формулу (придумал не сам)
        if num == 2:
            return False
        
        #for i in range(2, int(num**0.5) + 1):
            #if num % i == 0:
                #return False
        #return True

    def happynum(): # Цикл выдачи числа
        number = 2
        while True:
            if is_happy(number):
                print(number)
                answer = input('Продолжить? ')
                if answer.lower() != 'да':
                    break
            number += 1
    happynum()
    pass
happy_numbers()