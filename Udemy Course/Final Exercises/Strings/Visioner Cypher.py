# Шифр Виженера - Функции для зашифровывания и расшифровывания сообщений.
# https://inventwithpython.com/hacking/chapter19.html
def VisionerCypher():
    kirillic_alphabeth = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890'
    latin_alphabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    def encrypt(text, key, lang): # Шифровка текста
        pass

    def decrypt(text, key, lang): # Дешифровка текста
        pass

    def mode_check(text, key, key_lang): # Выбор режима шифровки/дешифровки
        print('Режим шифровки/дешифровки?: 1/2')
        mode = input()
        if mode == '1':
            encrypt(text, key, key_lang)
        elif mode == '2':
            decrypt(text, key, key_lang)
        else:
            print ('Выбор режима:')
            mode_check(text, key, key_lang)

    def key_operand_check(text, lang): # Проверка операнда для работы шифра, ключ должен быть в такой же раскладке, что и текст
        key = input('Введите ключ: ')
        for item in key:
            if lang == 'kirillic' and kirillic_alphabeth.find(item.upper()):
                mode_check(text, key, lang)
            elif lang == 'latin' and latin_alphabeth.find(item.upper()):
                mode_check(text, key, lang)
            else:
                print ('Ключ и текст должны быть в одной алфавитной системе')
    
    def cypher_operand_check(): # Проверка операнда для работы шифра, текст должен быть в такой же раскладке, что и ключ
        text = input ('Введите строку для шифровки/дешифровки: ')
        lang = 0
        for item in text:
            if kirillic_alphabeth.find(item.upper()) != -1:
                lang += 1
            elif latin_alphabeth.find(item.upper()) != -1:
                lang -= 1
        if lang >=  len(text)/2:
            lang = 'kirillic'
            print ("Используется кириллический алфавит")
            key_operand_check(text, lang)
        elif lang <= (-len(text)/2):
            lang = 'latin'
            print ("Используется латинский алфавит")
            key_operand_check(text, lang)
        else:
            answer = input('Текст не в одной раскладке, продолжить в кириллической или латинской раскладке? 1/2')
            if answer == '1':
                key_operand_check(text, lang='kirillic')
            elif answer == '2':
                key_operand_check(text, lang='latin')
                pass

    cypher_operand_check()

VisionerCypher()