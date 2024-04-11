def sums_in_loop():
    lst1 = [88942, 255559]
    lst2 = [545881, 727178]
    lst3 = [984663, 19697]
    lst4 = [576314, 149103]
    lst5 = [506030, 200765]
    lst6 = [667991, 990645]
    lst7 = [380690, 435912]
    lst8 = [388900, 21155]
    lst9 = [575135, 901400]
    lst10 = [434547, 937441]
    lst11 = [39848, 571838]
    lst12 = [146434, 863558]
    lst13 = [246499, 477410]
    lst14 = [866409, 933683]
    lst15 = [827621, 162472]
    summary = 0
    resultlst = []
    result = ''
    for item in lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, lst13, lst14, lst15:
        summary = sum(item)
        resultlst.append(summary)
    result = "".join(str(x) for x in resultlst) 
    print (result)
    return result
sums_in_loop()