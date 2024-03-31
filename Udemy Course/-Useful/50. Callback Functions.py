def number_info1(num):
    if num % 2 == 0:
        print ('This is an even number')
    elif num % 2 != 0:
        print ('This is an odd number')


def is_happy(num):
    
    '''
    #Square by 2 each of its digits.
    #Sum the squared digits.
    #Repeat steps 1–2 for the sum.
    #After unknown number of steps (the problem description says infinite), if we get the number 1 — then we can decide the original number is “happy”.
    '''
    num = str(num)
    digit = 0
    count = 0 
    while num != '1':
        for item in num:
            digit += (int(item) ** 2)
        num =  int(digit)
        num = str (num)
        #print (f"{digit} number")
        digit = 0
        count += 1
        #print (f"{count} iteration")
        if count == 25:
            print ('This is not an happy number')
            break
    else:
        print ('This is a happy number!')

def process(number, callback_func1, callback_func2):
    callback_func1 (number)
    callback_func2 (number)

enter_number = int(input ('Введите число: '))

process (enter_number, number_info1, is_happy)