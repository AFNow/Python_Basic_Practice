input = '36 130 140 2699 381 35 3296 2277 16 242 13 447 42 24487 38 128 1202 4162 92 29'
input_split = input.split()
input_int = list(map(int, input_split))
counter = 0
result = []
answer = ''
for item in input_int:
    while item != 1:
        if item %2 == 0:
            item = item / 2
            counter += 1
            continue
        else:
            item = 3 * item + 1
            counter += 1
            continue
    else:
        result.append(counter)
        counter = 0
answer = ' '.join(str(item) for item in result)
print(answer)
