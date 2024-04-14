import math
def rounding():
    input = '-1233561909 -128946 0 11745 -178719750 14500 -1597788547 -99734 1260877924 -88651 1076354006 -57148 -1244788685 -79341 -1521200800 190400 1738089741 -671466 0 -50238 1261202256 -194976 -1144779036 -65224 -655684890 -50696 -1265994590 -88060'
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
    print (result)
    for item in result:
        if item > 0:
            answer.append(round(item))
        elif item < 0:
            answer.append(math.floor(item))
        else:
            answer.append(item)
    answer = str(answer)
    print('result', result)
    print('answer',answer)
rounding()

# Expected answer 9567 0 -12326 16021 -14223 -18835 15689 -7990 -2589 0 -6469 17552 12934 14377