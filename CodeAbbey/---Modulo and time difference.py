input = ''' 9 5 19 54 17 22 52 45
            3 8 40 18 26 18 50 14
            17 17 49 52 27 12 29 38
            2 15 46 46 17 21 6 21
            4 19 58 55 9 8 11 51
            12 22 17 17 13 13 43 18
            2 20 51 34 3 13 34 42
            6 5 39 33 13 16 57 56
            22 7 56 16 26 22 37 17
            8 16 5 11 8 20 57 47
            20 23 24 0 25 5 41 38
            14 8 2 31 16 1 19 33
            0 16 11 30 14 19 16 58
            20 12 44 18 26 8 34 55
            5 12 3 58 24 22 2 41'''
# Day, hour, minute, second
input_split = input.split()
grouped_numbers = [input_split[i:i+4] for i in range(0, len(input_split), 4)]
index = 0
answer = ''
while index != len(grouped_numbers):
    date1 = (int(grouped_numbers[index][0]) * 86400) + (int(grouped_numbers[index][1]) * 3600) + (int(grouped_numbers[index][2]) * 60) + (int(grouped_numbers[index][3]))
    date2 = (int(grouped_numbers[index+1][0]) * 86400) + (int(grouped_numbers[index+1][1]) * 3600) + (int(grouped_numbers[index+1][2]) * 60) + (int(grouped_numbers[index+1][3]))
    index += 2
    difference = abs(date1 - date2)
    dif_days = difference//86400
    dif_hours = (difference//3600) - (dif_days * 24)
    dif_minutes = (difference//60) - (dif_days * 24 * 60) - (dif_hours * 60)
    dif_seconds = difference%60
    group ='(' + str(dif_days) +' '+ str(dif_hours) +' '+ str(dif_minutes) +' '+ str(dif_seconds) + ') '
    answer += group
print(answer)