input = '848 352 675 98617 56 1 7 64810 145 97 904 2547 44181 4 6541 4911 78 57985 675 104 8 3 882 581 5162 10 10 3117 39 840 9 429 4 9816 8 4748 578 83526 1832 139 10 9 94133 706 -1'
input_split = input.split()
moves = 0
def bubble_in_array(array):
    global moves
    index = 0
    result = 0
    while index != len(array)-1:
        if array[index] > array[index+1]:
            array[index+1], array[index] = array[index], array[index+1]
            index += 1
            moves += 1
        else:
            index += 1
            continue

    for item in array:
        result = (result + int(item)) * 113
        if result >= 10000007:
            result %= 10000007
    return result
result = bubble_in_array(input_split[0:len(input_split)-1])
print(moves, result)
