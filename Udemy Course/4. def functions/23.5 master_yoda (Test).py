# На входе фраза, на выходе слова в обратном порядке
def master_yoda (text):
    text_low = text.lower()
    listedtext = text_low.split()
    listedtext = list(reversed(listedtext)) 
    text2 = ' '.join(listedtext)
    text2 = text2.capitalize()
    print (text2)
text = str(input())
master_yoda (text)