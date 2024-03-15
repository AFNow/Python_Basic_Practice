def primenumbers():# Следующее простое число** - Программа продолжает находить простые числа до тех пор, пока пользователь не прекратит просить программу показать следующее простое число.   
# Простое число — натуральное число, имеющее ровно два различных натуральных делителя. Другими словами, натуральное число является простым, 
# если оно отлично от 1 и делится без остатка только на 1 и на само себя
    def is_prime(num): # Проверка через формулу (придумал не сам)
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primenum(): # Выдача ответа
        number = 2
        while True:
            if is_prime(number):
                print(number)
                answer = input('Продолжить? ')
                if answer.lower() != 'да':
                    break
            number += 1
    primenum()
primenumbers()