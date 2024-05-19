import math
def rounding():
    input = '0 84129 -971514810 -3265596 895540010 43220 1184275589 -77375 1411933827 151878 2012311275 8024 -930508769 17408 -924204333 67834 -176377593 31754 -1387640618 -455188 1856747307 127266 0 -11055 -582693380 1104632'
    split = input.split()
    lst = []
    for item in split:
        lst.append(int(item))

    index = 0
    pair = []
    result = []
    answer = []
    while index < len(lst):
        pair.append(lst[index])
        pair.append(lst[index+1])
        result.append(((pair[0] / pair[1]))) 
        index += 2
        pair = []
    lst = []
    for item in result:
        if item % 1 >= 0.5 and item < 0:
            lst.append(math.floor(item))
        elif item % 1 >= 0.5 and item > 0:
            lst.append(math.ceil(item))
        else:
            lst.append(round(item))
    answer = " ".join(str(x) for x in lst) 
    print(str(answer))
rounding()
