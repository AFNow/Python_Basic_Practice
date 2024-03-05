def primenum():
    number = 2
    while True:
        if number < 2:
            return False
        for item in range(2, int(number**0.5) + 1):
            if number % item == 0:
                break
        else:
            print(number)
        answer = input('Продолжить? ')
        if answer.lower() != 'да':
            break
        number += 1

primenum()