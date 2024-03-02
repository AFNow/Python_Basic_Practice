# Напишите функцию, которая вычисляет объем сферы по заданному радиусу:
# Формула 4/3*pi*r^3
# Через функцию def
import math
def vol(radius):
    vol = 0
    vol = 4 / 3 * math.pi * radius**3
    print (vol)
    return vol
vol(2)

# Напишите функцию, которая проверяет, содержится ли число в указанном диапазоне, включая верхнюю и нижнюю границы:
def ran_check(num, lower, higher):
    if num >= lower and num <= higher:
        print ('Число в диапазоне')
    else:
        print ('Число вне диапазона')
ran_check(1, 2, 7)

# А также вариант с булевым значением True/False
def bool_check(num, lower, higher):
    if num >= lower and num <= higher:
        print ('Число в диапазоне')
        return True
    else:
        print ('Число вне диапазона')
        return False
bool_check(1, 2, 7)

# Напишите функцию, которая принимает на вход строку и вычисляет количество букв в верхнем и нижнем регистре:
def up_low(string):
    lst = []
    for item in string:
        lst.append(item)
    countupper = []
    countlower = []
    for item in lst:
        if item.isupper():
            countupper.append(item)
        else:
            countlower.append(item)
    print (len(countupper))
    print (len(countlower))
    return (len(countupper))
up_low('Кроваво-черное ничто пустилось вить систему Клеток, связанных внутри Клеток, связанных внутри')

# Напишите функцию, которая принимает список, а возвращает новый список с уникальными данными из первого списка
def unique_list(lst):
    unique_set = set(lst)
    u_list = [unique_set]
    print (u_list)
    return u_list
unique_list([1,1,3,3,5,5,7,7,9,9,11,11])

# Напишите функцию, которая перемножает все числа в списке:
def multiply(lst):
    result = 1
    for item in lst:
        result *= item
    print (result)
    return result
multiply([1,2,3,4,5,6,7,8,9,0])

# Напишите функцию, которая определяет, является ли вводное строковое значение палиндромом:
def palindrome(string):
    check = string[::-1]
    print (check)
    print (string)
    if string.lower() == check.lower():
        print ('True')
        return True
    else:
        print ('False')
        return False
palindrome('Abba')

# Напишите функцию, которая определяет, является ли вводимое строковое значение панграммой:
import string
def is_pangram(str1):
    alphabeth = string.ascii_lowercase
    lst = []
    clean = []
    for item in alphabeth:
        lst.append(item)
    for item in str1:
        if item in lst:
            lst.remove(item)
    if lst == clean:
        print ('Слово является панграммой')
        return True
    else:
        print ('Слово не является панграммой')
        return False
is_pangram('The quick brown fox jumps over the lazy dog')