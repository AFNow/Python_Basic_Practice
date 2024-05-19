import math

input = ''' 161826419 4315029 3
            15229 15513 60594
            162956 392692 2184
            9078 7648 51697
            13178975 12423574 68
            1 1 507464610
            1454168 1276392 660
            9075102 10303012 77
            1159839 376813 826
            7494017 9422131 77
            2 6 87659106
            1386324 2773422 84
            31997227 234578549 4
            1 1 840117751
            1381473 551901 50
            464 60 1755779
            2160 1998 414365
            33919402 109291636 6'''
input_split = input.split()
input_split = [int(num) for num in input_split]
grouped_numbers = [input_split[i:i+3] for i in range(0, len(input_split), 3)]
index = 0
results = []
for index in (range(len(grouped_numbers))):
    x = grouped_numbers[index][0]
    y = grouped_numbers[index][1]
    n = grouped_numbers[index][2]
    t = min((math.ceil((max((x,y)) / float(x+y)) * n) * min((x,y)), math.ceil((min((x,y)) / float(x+y)) * n) * max((x,y))))
    index += 1
    results.append(t)
answer = ' '.join(str(item) for item in results)
print(answer)

'''
Параллельная печать:
t1 - время печати на первом принтере со скоростью x
t2 = время печати на втором принтере со скоростью y

Общее количество страниц:
n1 + n2 = input_split[index[2]]
Где n1 - количество страниц, напечатанных первым принтером, а n2 - вторым

Минимальное время:
Нужно найти n1 и n2, чтобы 
t1 = n1/x
t2 = n2/y

Общее время печати будет равно:
T = max(t1, t2), где
T = n1/x
T = n2/y
'''