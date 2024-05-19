input = ''' 65 1.85
            87 2.20
            98 1.72
            45 1.79
            110 2.19
            106 2.25
            99 1.88
            66 1.97
            83 1.50
            62 1.68
            109 2.18
            101 2.90
            115 2.40
            52 1.19
            50 1.39
            94 1.77
            44 1.48
            104 1.80
            93 1.79
            87 1.60
            48 1.21
            85 2.30
            47 1.32
            108 3.13
            115 1.90
            52 1.32
            46 1.18
            90 2.02
            94 2.07
            50 1.31
            107 2.07
            49 1.18
            57 1.54
            75 2.17
            93 2.21 '''
input_split = input.split()
index = 0
dataset = []
result = ''
while index != len(input_split):
    dataset.append(input_split[index])
    dataset.append(input_split[index+1])
    index += 2
    print(dataset)
    bmi = float(dataset[0]) / (float(dataset[1])**2)
    print(round((bmi), 2))
    if bmi < 18.5:
        result += 'under '
    elif bmi >= 18.5 and bmi < 25.0:
        result += 'normal '
    elif bmi >= 25.0 and bmi < 30.0:
        result += 'over '
    elif bmi > 30.0:
        result += 'obese '
    dataset = []
print (result)


# Underweight     -           BMI < 18.5      (недостаточная масса)
# Normal weight   -   18.5 <= BMI < 25.0      (норма)
# Overweight      -   25.0 <= BMI < 30.0      (избыточная масса)
# Obesity         -   30.0 <= BMI             (ожирение)
# under, normal, over, obese 
# BMI = вес / рост^2