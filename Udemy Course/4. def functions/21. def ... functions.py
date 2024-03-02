# Функции в Python - это блок кода, который всегда может быть повторно вызван без необходимости его повторно переписывать или указывать построчно.
# Синтаксис функций def... (definition):
def name_of_function():
    '''
Docstring - описание функции, которе лучше указывать, оно в последствии будет полезно для опознания предзназначения функции
Хорошим тоном является указать, что эта функция принимает и что выдает:
INPUT: None
OUTPUT: Something
'''
    print ('Something')
name_of_function() # Команда, которая вызывает функцию
# Или с указанием функции возврата return, которая запишет конечные данные функции в виде переменной, сохраненной в самой функции
def function(num1,num2):
    return num1+num2
result = function(1,2)
print (result) # 3
# Пример:
word = input('Word:')
def pig_latin():
    '''
    Функция поросячьей латыни:
    Берется слово на латинице, если первая буква гласная, то в конце добавляется 'ay'. 
    Если первая буква согласная, то она переносится в конец слова и после добавляется 'ay'.
    '''
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
pig_word = pig_latin()
print (pig_word)
