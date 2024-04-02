def divide():
    while True:
        try:
            num1 = input('First num: ')
            num1 = int(num1)
            num2 = input('Second num: ')
            num2 = int(num2)
            value = int(num1)/int(num2)
            print (value)
            answer = str(input('Continue? y/n '))
            if answer == 'y':
                continue
            else:
                break
        except TypeError:
                    print("It's not a num")
                    continue
        except ValueError:
                    print("It's not a num")
                    continue
        except ZeroDivisionError:
                    print("Zero division is unacceptable :<")
                    continue
divide()