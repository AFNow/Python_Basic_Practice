# Декораторы - это функции, которые могут применять свои свойства, в другие функции или поверх них.
# Пример:
def decorator_function(func):
    def wrapper():
        print('Код декоратора до основной функции')
        func()
        print('Код декоратора после второстепенной функции')
    return wrapper

# Также для использования декораторов можно указывать специальный синтаксис в виде:
@decorator_function
def primary_function():
    print ('Код основной функции')
primary_function()

# Функциональный пример:
def benchmark(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')
fetch_webpage()

# Или:
def benchmark(iters):
    def actual_decorator(func):
        import time
        
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper
    return actual_decorator

@benchmark(iters=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')