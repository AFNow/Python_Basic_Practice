def min_of_two():
    full_lst = [8417970, 6710855,
                6778850, 9470770,
                -2116597, -8373121,
                2849066, 4227965,
                -7739335, -8019120,
                2247706, 3816577,
                8486903, 9379636,
                -8247224, -1691458,
                -4908523, -8598293,
                -7277868, 6955361,
                -2770604, 142621,
                -5523928, -4772974,
                -1560419, 7182453,
                5970961, -8486287,
                -3147758, 3377561,
                -6946934, -9766360,
                -5006734, -774778,
                6061303, -4291649,
                -182675, 6956583,
                19595, -8649336]
    minimal = [] 
    result = ''
    index = 0
    while index < len(full_lst):
        minimal.append(min(full_lst[index], full_lst[index+1]))
        result = ' '.join(str(x) for x in minimal)
        index += 2
    print (result)
min_of_two()