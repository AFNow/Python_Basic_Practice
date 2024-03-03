# Создайте генератор, который возвращает квадраты чисел, вплодь до n
def squaregen(n):
    for item in range(0, n):
        x = item**2
        yield x
for item in squaregen(10+1):
    print (item)

# Создайте генератор, который возвращает n случайных чисел между нижней и верхней границами.
def randomnumber(lower, higher, n):
    import random
    while n >= 0:
        n -= 1
        x =  random.randrange(lower, higher)
        yield x
        continue
for item in randomnumber(1, 15, 12):
    print (item)

# Используя функцию iter() сделать строку итерируемой:
def iterator(text):
    textiter = iter(text)
    for item in textiter:
        yield item
for item in iterator('TEXT'):
    print (item)
