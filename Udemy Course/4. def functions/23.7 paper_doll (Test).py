# На входе строка, вернуть строку где каждый символ исходной строки повторяется три раза
def paper_doll(word):
    lst = []
    for item in word:
        itemx3 = (item*3)
        lst.append(itemx3)
    word2 = ''.join(lst)
    print (word2)
word = str(input('Введите слово:'))
paper_doll(word)

# Hello > HHHeeellllllooo
# Mississippi