# Меньшее из двух четных чисел:
# напишите функцию, которая возвращает меньшее из двух чисел, если оба этих числе четные, 
# иначе возвращает большее из двух чисел, если одно или оба из них нечетные.

def lesser_of_two_events(A, B):
    if A % 2 == 0 and B % 2 == 0:
        if A > B:
            print("Меньшее из четных чисел: ", B)
        else:
            print("Меньшее из четных чисел: ", A)
    else:
        if A > B:
            print("Большее число: ", A)
        else:
            print("Большее число: ", B)

A, B = map(int, input('Введите два числа через пробел: ').split())
lesser_of_two_events(A, B)