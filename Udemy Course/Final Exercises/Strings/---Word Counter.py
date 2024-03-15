def countwords():# Подсчёт количества слов в строке** - Подсчитать количество отдельных слов в строке. Для увеличенной сложности, прочитайте строки из текстового файла.
    counter = 0
    symbols = ['-','—']
    textfile = open ("Strings.txt", 'r', encoding='utf-8')
    contents = textfile.read()
    textfile.close()
    split = contents.split()
    for item in split:
        if item not in symbols:
            counter += 1
    print (f"В файле содержится {counter} слов")
countwords()