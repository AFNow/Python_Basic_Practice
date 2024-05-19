input = '921 40364 795 34820 -108 126 -799 1508 152 -2105 -843 16800 -68 -2739 -826 -33059 318 26714 171 14513 -653 36711 248 -13745 -253 985 -349 1369 75 6397 -565 -47363 358 -9911 937 -26702 646 -40354 939 -58520 -949 -29999 170 4690 -629 41933 -922 61564 251 9623 -735 -29817 -421 6018 -873 11894 -478 8008 963 -16489'

def linear_function():
    split = input.split()
    index = 0
    answer = ''
    while index != len(split):
        x1 = int(split[index])
        y1 = int(split[index+1])
        x2 = int(split[index+2])
        y2 = int(split[index+3])
        index += 4
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        answer += f'({round(a)} {round(b)}) '
    print (answer)
linear_function()
