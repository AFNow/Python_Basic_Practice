input = '17 6 1 13 12 19 11 8 15 18 16 5 4 9 3 14 10 2 7'
input_split = input.split()
input_split = [int(num) for num in input_split]
def bubble_sort(array):
    moves = 0
    passes = 0
    while True:
        sorted = True
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                sorted = False
                moves += 1
        passes += 1
        if sorted:
            break
        else:
            continue
    print(passes, moves)
bubble_sort(input_split)
