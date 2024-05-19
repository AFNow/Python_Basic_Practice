input = '45 1 184536604 2 772 32538 90411 44477 7951 168039 16096 10865795 13083501 251 61888002 16 3444247 61795746 6690 7 25 204 3827 597153375 33951550 6223713 25490429 95181 11621 1750420 48717280 411810 37886 2435'
index = 0
split = input.split()
def convert_to_digits(num):
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10
    return digits[::-1]

result_sum = []
while index != len(split):
    digits = convert_to_digits(int(split[index]))
    local_index = 1
    result = []
    for item in digits:
        result.append(item * local_index)
        local_index += 1
    index += 1
    result_sum.append(sum(result))
answer = ''
answer = ' '.join(str(item) for item in result_sum)
print(answer)