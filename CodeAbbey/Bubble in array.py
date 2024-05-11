input = '10 6 52 9533 23 74296 92 66 4889 8106 841 8129 780 4 9 9 8892 21116 5245 764 4147 4 16 5 27 27 623 67 3 75103 32784 1 79 7107 30 8590 1 5 561 736 3 8785 12 239 636 91462 81899 -1'
input_split = input.split()
moves = 0
def bubble_in_array(array):
    global moves
    index = 0
    while index != len(array)-1:
        if array[index] > array[index+1]:
            array[index+1], array[index] = array[index], array[index+1]
            index += 1
            moves += 1
        else:
            index += 1
            continue
    return array
result= sum(list(map(int, bubble_in_array(input_split[0:len(input_split)-1]))))
answer = str(moves) + ' ' + str(result)
print(answer)
