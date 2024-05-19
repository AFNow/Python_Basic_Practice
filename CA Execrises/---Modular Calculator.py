input = '''* 9
        * 1957
        * 517
        + 68
        * 296
        + 2813
        * 734
        + 59
        * 93
        + 9
        * 2595
        * 1964
        + 2099
        * 76
        + 489
        + 930
        * 574
        + 5
        + 271
        * 5
        * 3
        * 748
        * 8
        * 1
        + 2
        + 86
        + 17
        + 1
        * 2045
        * 51
        + 60
        * 3
        * 1337
        * 658
        + 83
        + 769
        * 92
        * 1
        + 4437
        + 171
        + 4154
        * 150
        * 632
        + 8603
        * 2
        + 573
        + 1
        * 2358
        * 5276
        * 9357
        + 44
        * 4
        * 37
        % 6885'''
integer = 547
def pairing(input):
    input_split = input.split()
    pairs = [input_split[index:index+2] for index in range(0, len(input_split), 2)]
    return pairs
pairing(input)

def calculations(pairs, integer):
    index = 0
    while index != len(pairs):
        if pairs[index][0] == '+':
            integer += int(pairs[index][1])
        elif pairs[index][0] == '-':
            integer -= int(pairs[index][1])
        elif pairs[index][0] == '*':
            integer *= int(pairs[index][1])
        elif pairs[index][0] == '%':
            integer %= int(pairs[index][1])
        index += 1
    return integer
result = calculations(pairing(input), integer)
print(result)