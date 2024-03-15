def consonants(sentence):# Подсчёт гласных** - Введите строку, и программа должна подсчитать количество гласных букв в этом тексте. Также можно указать количество для каждой гласной буквы отдельно.
    consonantsRus = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ']
    vowelsRus = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
    consonantsEng = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowelsEng = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = 0
    vowels = 0
    for item in sentence:
        if item.lower() in consonantsRus or item.lower() in consonantsEng:
            consonants += 1
        if item.lower() in vowelsRus or item.lower() in vowelsEng:
            vowels += 1
    print (f"В предложении {consonants} согласных и {vowels} гласных")
sentence = 'Я выжил, потому что огонь внутри меня горел ярче, чем вокруг меня'
consonants (sentence)  