def prime_factors(n):# Разложение на простые делители** - Пользователь вводит число, программа находит все простые делители этого числа (если такие есть), и отображает их.
    result = []
    cycle = 2
    while cycle <= n:
        if n % cycle == 0:
            result.append(cycle)
            n = n / cycle
        else:
            cycle += 1
    print (result)
prime_factors(30)