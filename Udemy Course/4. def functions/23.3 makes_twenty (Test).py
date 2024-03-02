# На входе два числа, функция возвращает True, если сумма этих чисел равна 20, или одно из чисел равно 20. В противном случае возвращает False
def makes_twenty (n1,n2):
    if n1 == 20 or n2 == 20:
        print ('True')
    elif n1 + n2 == 20:
        print ('True')
    else:
        print('False')
n1, n2 = map(int, input('Введите два числа через пробел: ').split())
makes_twenty (n1,n2)