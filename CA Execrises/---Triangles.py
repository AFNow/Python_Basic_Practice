def triangles():
    input = '559 957 362 757 2737 1164 453 708 321 546 808 722 691 1690 1171 543 444 321 430 709 545 1912 709 770 386 1400 582 320 553 328 3583 1656 993 315 434 707 496 953 598 2386 729 961 1423 471 747 1587 354 679 845 341 245 452 267 376 545 347 191 323 759 257'
    split = input.split()
    lst = []
    for item in split:
        lst.append(int(item))
    index = 0
    triangle = []
    answer = ''
    while index < len(lst):
        triangle.append(lst[index])
        triangle.append(lst[index+1])
        triangle.append(lst[index+2])
        triangle.sort()
        c = triangle.pop()
        b = triangle.pop()
        a = triangle.pop()
        index += 3
        if (c < a + b) and (b < a + c) and (a < b + c):
            answer += '1 '
        else:
            answer += '0 '
    print (answer)
triangles()