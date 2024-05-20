alphabetEng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
alphabetRus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
print (alphabetRus)
print (alphabetEng)
'''
Шифр Цезаря - Функции для зашифровывания и расшифровывания сообщений.
Шифр Цезаря (лат. notae Caesarianae), шифр сдвига, код Цезаря, схема Цезаря — шифр, при использовании которого каждая буква из 
открытого текста заменяется на такую букву, которая в алфавите находится на некотором постоянном числе позиций левее или правее от рассматриваемой буквы. 
Например, при сдвиге букв русского алфавита вправо на 3 позиции
'''

def CaesarCypher():
    input_str = input('Шифруемое сообщение: ')
    string_upper = input_str.upper()
    print(string_upper)
    shift = input ('Сдвиг: ')
    for item in string_upper:
        if item in alphabetEng:
            print (alphabetEng[(alphabetEng.index(item) + int(shift)) % len(alphabetEng)], end = '')
        elif item in alphabetRus:
            print (alphabetRus[(alphabetRus.index(item) + int(shift)) % len(alphabetRus)], end = '')
        else:
            print ('Something wrong')
            
CaesarCypher()