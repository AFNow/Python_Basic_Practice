# Напишите функцию, которая берет список чисел и возвращает true, если в списке содержатся числа 0 0 7 в указанном порядке
def spy_game(n):
    code = [0,0,7,'x']
    for item in n:
        if item == code[0]:
            code.pop(0)
    if len(code) == 1:
        print('True')
    else:
        print('False')
    return len(code) == 1 
n = [1,7,2,0,4,5,1]
spy_game(n)


# spy_game([1,2,4,0,0,7,5])
# spy_game([1,2,0,4,0,5,7])
# spy_game([1,7,2,0,4,5,1])