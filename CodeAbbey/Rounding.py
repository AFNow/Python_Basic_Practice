import math
def rounding():
    input = '-106571979 -136894 360186108 -25224 316154467 -36962 -1736405749 -74381 727383920 -71776 2024088441 166722 -324523637 -16462 0 11758 0 -26946 114222596 -10408 -194133120 -25164'
    split = input.split()
    lst = []
    for item in split:
        lst.append(int(item))

    index = 0
    pair = []
    result = []
    answer = ''
    while index < len(lst):
        pair.append(lst[index])
        pair.append(lst[index+1])
        result.append(math. ceil((pair[0] / pair[1])))
        pair = []
        answer = " ".join(str(x) for x in result) 
        index += 2
    print(answer)
rounding()