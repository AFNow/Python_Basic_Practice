# Генераторы - функции с более оптимизированным способом итерации, который позволяет не сохранять все данные функции, а использовать только выборочные. 
# Наиболее явно это можно увидеть на примере функций, которые в себе обрабатывают большое количество данных.
# Примером может послужить расчет формулы фибоначчи в большом объеме:
def fibonacci(x): # Данная функция с таймером выполняет итерацию и запись числа фибоначчи в рэндже до 10000 и не являясь генератором занимает больший объем памяти
    import time
    start = time.time()
    a = 1
    b = 1
    out = []
    for item in range(x+1): 
        out.append(a)
        a,b = b, a+b
    print(out)
    end = time.time()
    print('Время выполнения: {} секунд.'.format(end - start))
fibonacci(10000)

def genfibonacci(x): # Это аналогичная функция, но исполняемая через генератор, который оптимизирует скорость выполнения функции более чем в три раза
    import time
    start = time.time()
    a = 1
    b = 1
    genout = []
    for item in range(x+1): 
        yield a
        genout.append(item)
        a,b = b, a+b
    end = time.time()
    print('Время выполнения: {} секунд.'.format(end - start))
    return genout
print(list(genfibonacci(10000)))
genfibonacci (10000)

# Также одной из функций генераторов является команда next, которая возвращает записанное в последовательности генератора значение:
def gen():
    for item in range(0, 3):
        yield item
g = gen()
print(next(g))
print(next(g))
print(next(g))


