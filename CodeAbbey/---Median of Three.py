input = '7 849 460 119 114 96 1 93 4 1007 5 976 1425 869 874 81 1 82 20 1 6 240 3 715 78 40 612 22 70 80 1343 1342 627 8 61 858 235 53 238 619 639 629 409 443 454 97 502 521 75 145 96 234 4 16 27 965 5 107 89 94'
split = input.split()
input_lst = []
for item in split:
    input_lst.append(int(item))
index = 0
triplet = []
median_int = []
while index < len(split):
    triplet.append(input_lst[index])
    triplet.append(input_lst[index+1])
    triplet.append(input_lst[index+2])
    triplet.sort()
    median_int.append(triplet[1])
    triplet = []
    index += 3
result = ' '.join(str(item) for item in median_int)
print (result)