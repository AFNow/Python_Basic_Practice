# На входе дается число n, нужно определить, находится ли оно в диапазоне 10 шагов от или до 100 или 200.
def almost_there(n):
    if n > 90 and n < 110:
        print ('Число в диапазоне 90-110')
    elif n > 190 and n < 210:
        print ('Число в диапазоне 190-210')
    else:
        print ('Число вне диапазона')
n = 209
almost_there(n)
# almost_there (104)
# almost_there (150)
# almost_there (209)