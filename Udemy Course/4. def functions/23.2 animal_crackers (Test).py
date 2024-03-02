# Напишите функцию, которая будет принимать на входе строку из двух слов, а потом возвращать True, если оба слова начинаются с одной и той же буквы

def animal_crackers(text):
    text_lower = text.lower()
    splitted_text = text_lower.split()
    if len(splitted_text) == 2:
        if splitted_text[0][0] == splitted_text[1][0]:
            print('True')
        else:
            print('False')
    else:
        print('Ошибка: список должен содержать ровно 2 элемента.')

text = input('Введите два слова: ')
animal_crackers(text)