def int_to_words():# Написание числа словами** - Напишите число словами. Например: 123 это "сто двадцать три". 
    #Можете использовать уже существующую реализацию, или создать свою собственную, но реализуйте поддержку чисел хотя бы до миллиона. 
    #*Опционально: реализуйте поддержку чисел, отличающихся от положительных целых чисел (например нуль, отрицательные целые числа, числа с плавающей точкой).*
    class Words:
        def __init__(self): 
                self.integer = 0
                self.words = {'один':1,'два':2,'три':3,'четыре':4,'пять':5,'шесть':6,'семь':7,'восемь':8,'девять':9,'десять':10,
                              'одиннадцать':11,'двенадцать':12,'тринадцать':13,'четырнадцать':14,'пятнадцать':15,'шестнадцать':16,'семнадцать':17,'восемнадцать':18,'девятнадцать':19,
                              'двадцать':20,'тридцать':30,'сорок':40,'пятьдесят':50,'шестьдесят':60,'семьдесят':70,'восемьдесят':80,'девяносто':90,'сто':100,
                              'двести':200,'триста':300,'четыреста':400,'пятьсот':500,'шестьсот':600,'семьсот':700,'восемсот':800,'девятьсот':900,'тысяча':1000}
                pass
        def __str__(self): 
                pass
                #return f"----"
int_to_words(15)    