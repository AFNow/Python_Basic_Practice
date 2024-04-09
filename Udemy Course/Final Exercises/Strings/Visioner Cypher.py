# Шифр Виженера - Функции для зашифровывания и расшифровывания сообщений.
def VisionerCypher():
    def CypherOperandCheck():
        kirillic_alphabeth = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        kirillic_alphabeth_dict = {k : v for k, v in enumerate(kirillic_alphabeth.lower())}
        latin_alphabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        latin_alphabeth_dict = {k : v for k, v in enumerate(latin_alphabeth.lower())}
        cypher = input ('Введите шифруемую строку: ')
        for item in cypher.lower()[0]:
            if item in kirillic_alphabeth_dict.values():
                print ("Используется кириллический алфавит")
                CypherPreparing()
            elif item in latin_alphabeth_dict.values():
                print("Используется латинский алфавит")
                CypherPreparing()
    CypherOperandCheck()


    def CypherPreparing():
        pass

# https://inventwithpython.com/hacking/chapter19.html