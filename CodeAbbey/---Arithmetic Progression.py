input_data = '13 11 39 12 19 16 6 1 93 20 1 60 11 0 80 8 14 77 4 8 67 9 7 80 29 18 70 24 12 29 19 16 86'
split = input_data.split()
lst = []
for item in split:
    lst.append(int(item))

def arithmetic_progression_sum(varuables):
    a = varuables[0]
    b = varuables[1]
    n = varuables[2]
    return (n / 2) * (2 * a + (n - 1)* b)

def arithmetic_progression():
    index = 0
    varuables = []
    answers = []
    while index < len(lst):
        varuables.append(lst[index])
        varuables.append(lst[index+1])
        varuables.append(lst[index+2])
        index += 3
        #print (varuables)
        answers.append(round(arithmetic_progression_sum(varuables)))
        varuables = []
        #print (answers)
    answer = ' '.join (str(item) for item in answers)
    print (answer)
arithmetic_progression()

#[ S_n = \frac{n}{2} \left(2a + (n - 1) \cdot d\right) ]
#Где:
#(S_n) - сумма первых (n) членов арифметической прогрессии.
#(a) - первый член прогрессии.
#(d) - разность между последовательными членами.