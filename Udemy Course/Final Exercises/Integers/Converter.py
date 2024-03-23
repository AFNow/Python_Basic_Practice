# Перевод единиц измерения (температура, валюта, объем, масса и т.д.)** - Конвертировать различные единицы измерения между собой. Пользователь вводит тип исходной единицы измерения, в какую единицу измерения нужно перевести, и само значение. Затем программа выполняет конвертацию.
def lenght_operation(value, operation, lenght_operations): 
    answer = value * (float (lenght_operations[operation]))
    return answer

def temperature_operation(value, operation, temperature_operations):
    if operation.lower() == 'цельсий > кельвин' or operation.lower() == 'фаренгейт > ранкин':
        answer = value + float(temperature_operations[operation])
        return answer
    elif operation.lower() == 'фаренгейт > цельсий':
        answer = (value-32) * float(temperature_operations[operation])
        return answer
    elif operation.lower() == 'фаренгейт > кельвин':
        answer = (value-32) * 5/9 + float(temperature_operations[operation])
        return answer
    elif operation.lower() == 'кельвин > цельсий':
        answer = value - float(temperature_operations[operation])
    elif operation.lower() == 'кельвин > фаренгейт':
        answer = (value - 273.15) * float(temperature_operations[operation])
    else:
        answer = value * float(temperature_operations[operation])
        return answer

def converter(): # Выбор способа конвертации
    lenght_varuables = ['Сантиметр','Метр','Километр','Дюйм','Фут','Ярд','Миля']
    #pressure_varuables = ['Атмосфера', 'Бар', 'Паскаль', 'Торр']
    temp_varuables = ['Цельсий', 'Фаренгейт', 'Кельвин', 'Ранкин'] 
    lenght_operations = {'сантиметр > метр': 0.01, 'сантиметр > километр':  0.00001, 'сантиметр > дюйм': 0.3937, 'сантиметр > фут': 0.0328, 'сантиметр > ярд': 0.0109, 'сантиметр > миля': 0.000006,
                        'метр > сантиметр': 100, 'метр > километр': 1000, 'метр > дюйм': 39.37, 'метр > фут': 3.2808, 'метр > ярд': 1.0936, 'метр > миля': 0.0006,
                        'километр > сантиметр': 100000, 'километр > метр': 1000, 'километр > дюйм': 39370.07, 'километр > фут': 3280.83, 'километр > ярд': 1093.61, 'километр > миля':0.6213,
                        'дюйм > сантиметр': 2.54, 'дюйм > метр': 0.0254, 'дюйм > километр': 0.0000254, 'дюйм > фут': 0.0833, 'дюйм > ярд': 0.0277, 'дюйм > миля': 0.000015,
                        'фут > сантиметр': 30.48, 'фут > метр': 0.3048, 'фут > километр': 0.0003048, 'фут > дюйм': 12, 'фут > ярд': 0.333, 'фут > миля': 0.0001893, 
                        'ярд > сантиметр': 91.44, 'ярд > метр': 0.9144, 'ярд > километр': 0.0009144, 'ярд > дюйм': 36, 'ярд > фут': 3, 'ярд > миля': 0.00056, 
                        'миля > сантиметр': 160934.4, 'миля > метр': 1609.344, 'миля > километр': 1.609344, 'миля > дюйм': 63360, 'миля > фут': 5280, 'миля > ярд': 1760}
    #pressure_operations= []
    temperature_operations = {'цельсий > фаренгейт': (9/5)+32, 'цельсий > кельвин': 273.15, 'цельсий > ранкин': (9/5)+491.67, 
                              'фаренгейт > цельсий': (5/9), 'фаренгейт > кельвин': 273.51, 'фаренгейт > ранкин': 459.67, 
                              'кельвин > цельсий': 273.15, 'кельвин > фаренгейт': (9/5)+32, 'кельвин > ранкин': (9/5)}
    print ("Выберите вариант конвертации по типу: Тип1 > Тип2")
    print ('Длина:', ", ".join(lenght_varuables))
    #print ('Давление:', ", ".join(pressure_varuables)) 
    print('Температура: ', ", ".join(temp_varuables))
    operation = input('Конвертация: ')
    value = float(input('Сколько: '))
    if operation.lower() in lenght_operations:
        print (lenght_operation(value, operation, lenght_operations))
    elif operation.lower() in temperature_operations:
        print (temperature_operation(value, operation, temperature_operations))
converter()


# https://infinitetools.io/ru/c/unit-converters/length/centimetre-to-mile