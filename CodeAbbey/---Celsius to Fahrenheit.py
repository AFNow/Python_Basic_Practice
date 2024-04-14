def FtoC():
    input = '39 363 189 173 544 195 573 451 377 421 46 399 218 281 468 64 520 334 375 561 258 292 513 596 47 540 286 460 325 35 412 78 429 376 227 166 244'
    split = input.split()
    lst = []
    c = ''
    answerslst = []
    result = ''
    for item in split:
        lst.append(int(item))
    for item in lst:
        c =round((item - 32) / 1.8)
        answerslst.append(c)
    result = ' '.join(str(item) for item in answerslst)
    print (result)
FtoC()

#(Фаренгейт — 32) : 1,8 = Цельсий 