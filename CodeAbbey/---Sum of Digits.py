input = '168 95 45 395 74 84 335 14 163 24 76 29 345 175 148 238 49 24 294 182 142 216 234 153 132 271 92 319 244 157 223 88 149 83 36 75'
split = input.split()
index = 0
results = []
answers = []
def convert_to_digits(result):
    digits = []
    while result > 0:
        digit = result % 10
        digits.append(digit)
        result //= 10
    return digits[::-1]

while index != len(split):
    a = split[index]
    b = split[index+1]
    c = split[index+2]
    index += 3
    result = int(a) * int(b) + int(c)
    results = (convert_to_digits(result))
    sum = 0
    for item in results:
        sum += int(item)
    answers.append(sum)
answer = ' '.join(str(item) for item in answers)
print(answer)
