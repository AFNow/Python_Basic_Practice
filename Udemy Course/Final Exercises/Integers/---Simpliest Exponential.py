def exponentiation():# Быстрое возведение в степень** - Пользователь вводит 2 целых числа, и программа вычисляет a^b (a в степени b, со сложностью по времени O(lg n).
    x = int(input('Введите число для возведения в степень: '))
    y = int(input('Введите степень: '))
    z = x**y
    print (z)
exponentiation()