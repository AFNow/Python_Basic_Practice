# List Comprehensions позволяет эффективно уменьшать часть кода, сохраняя ее полноценное значение
# Пример:
string = 'Hello'
lst = []
for letter in string:
    lst.append (letter)
print (lst)
# Пример этого кода может быть заметно уменьшен, благодаря написания операции for ... in в одну строку:
lst2 = [letter for letter in string] # таким образом к названию переменной lst2 присваивается итерируемая переменная из string
print (lst2)
# Также это позволяет уменьшать количество строк для генератора range
lst3 = [num for num in range(1,11,2)]
print (lst3)
# Также подобное сокращение позволяет выполнять операции с временной переменной внутри кода, то есть:
lst4 = [num**3 for num in range(1,5)] # То есть теперь в переменную lst4 записываются числа из range в третьей степени
print (lst4)
# В дальнейшем в это сокращение можно добавить условие if:
lst4 = [num**3 for num in range(1,5) if num%2 == 0] # То есть теперь в переменную lst4 записываются числа из range в третьей степени
print (lst4)
# Кроме того, это позволяет паковать двойные циклы по примеру:
lst5 = []
for num1 in [2,4,6]: # Сам двойной цикл выполняет последовательное умножение пунктов по очереди в списке: (2*10, 2*100, 2*1000...)
    for num2 in [10,100,1000]:
        lst5.append(num1*num2)
print (lst5)
# Упаковать его можно по типу:
lst6 = [x*y for x in [2,4,6] for y in [10,100,1000]]
print (lst6)