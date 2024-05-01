input = '16 9 8 16 16 1 6 18 2 1 6 8 6 9 18 12 16 3 2 11 16 10 2 16 13 8 10 14 4 2 13 6 4 4 9 10 17 13 4 9 18 15 11 14 15 10 9 10 7 14 10 14 4 13 17 8 5 2 14 16 7 12 9 7 10 4 4 18 16 4 14 2 16 2 2 17 3 13 1 2 2 9 15 12 5 7 18 10 7 11 12 7 13 14 12 3 9 5 7 10 11 7 7 14 1 16 15 13 10 11 8 17 6 17 18 3 11 10 5 8 18 7 12 5 5 17 10 9 3 8 5 2 18 6 16 4 8 16 12 1 17 17 13 10 18 2 10 6 12 17 17 3 11 9 8 10 13 2 15 14 18 9 14 2 7 11 4 11 16 8 17 4 18 15 5 16 6 13 13 12 13 12 9 6 14 9 13 13 13 1 17 16 12 5 18 14 9 8 12 10 2 15 5 5 7 14 7 2 18 4 12 17 6 12 12 17 17 16 5 9 9 5 14 11 12 1 11 5 11 9 16 2 10 7 4 8 12 11 7 2 15 6 11 5 3 16 5 6 4 11 9 12 9 6 8 6 3 13 9 16 11 15 6 9 9 17 10 12 6 13 13 11 9 8 18 10 7 8 3 4 17'
input_split = list(map(int, input.split()))
input_split.sort()
ref_integer = []
counter = 1
results = []
for item in input_split:
    if item not in ref_integer:
        ref_integer.append(item)
        results.append(counter)
        counter = 1
    else:
        counter += 1
results.append(counter)
results.pop(0)
result = ' '.join(str(item) for item in results)
print(result)