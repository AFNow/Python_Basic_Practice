input ='''155637 4416561 50 65666 854241 6551 412 303 19719729 98495 48916069 2 911859669 5874 4845 63505830 851 66217176 31160 74400808 3018247 9 49981362 989721 41208672 714 967706'''
def array_checksum(input):
    input_split = input.split()
    result = 0
    for item in input_split:
        result = (result + int(item)) * 113
        if result >= 10000007:
            result %= 10000007
    return result
print(array_checksum(input))