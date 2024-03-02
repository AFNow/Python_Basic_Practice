# Вернуть сумму чисел в массиве, кроме набора чисел, который начинается на 6 и продолжается до 9 (для каждого числа 6 далее будет число 9), вернуть 0 если чисел нет
def summer_69(n):
    total = 0
    cont = True
    for item in n:
        while cont:
            if item != 6:
                total += item
                break
            else:
                cont = False
        while not cont:
            if item != 9:
                break
            else:
                cont = True
                break
    print (total)
    return (total)
n = (2,1,6,9,11)
summer_69(n)
# summer_69(1,3,5) > 9
# summer_69(4,5,6,7,8,9) > 9 
# summer_69(2,1,6,9,11) > 14