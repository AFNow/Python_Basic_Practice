print('Set - это тип данных, который сохраняет только уникальные значения в единичном виде.')
myset = set()
myset.add (1)
print ('Сет с одной ячейкой 1: ',myset)
print ('Добавление второй ячейки:')
a: str = input('')
a = int(a) 
myset.add (a)
print ('При добавлении идентичной ячейки остаются только уникальные данные:')
print ('Добавление третьей ячейки:',myset)
a: str = input('')
a = int(a) 
myset.add (a)
print ('Данные сохраняются в единичном экземпляре: ', myset)