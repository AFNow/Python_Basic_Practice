# Напишите функцию, которая переводит в верхний регист первую и четвертую буквы имени
def old_macdonald (name):
    name_list = list(name)
    name_list[0] = name_list[0].upper()
    name_list[3] = name_list[3].upper()
    # return ''.join(name_list)
    name_edt = ''.join(name_list)
    print (name_edt)
name = str(input())
old_macdonald (name)