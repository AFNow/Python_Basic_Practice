def decorator(func):
    def wrapper(a,b):
        print(a, '**' ,b)
        func(a,b)
        print('Calc is done')
    return wrapper
