# Объектно-ориентированное программирование - позволяет создавать свои объекты с методами и атрибутами, 
# как для строк, списков и других объектов используются команды .method_name().
# Эти методы работают как функции, которые используют информацию об объекте и сам объект для получения результата или изменения самого объекта
# Пример:
class NameOfClass(): # Пример синтаксиса
    def __init__(self,parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
    def some_method(self):
        # Выполнение некоего действия
        print (self.parameter1)
pass

class Dog(): # Собака, порода etc. 
    # Class object attribute
    # Will be same for any instance of class
    species_class = 'mammal'
    def __init__(self, breed, name, spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # Spots needs to be Boolean True/False
        self.spots = spots
    def bark(self):
        print ('Bark! My name is ',self.name)
my_dog = Dog(breed='Huskie', name='Puppy', spots=False)

class Circle():# Площадь и длина окружности
    def __init__(self, radius = 1):
        self.radius = radius
    def get_circumference(self):
        import math
        print (self.radius * math.pi * 2)
        return self.radius * math.pi * 2
    def get_area(self):
        import math
        print (self.radius * self.radius * math.pi)
        return self.radius * self.radius * math.pi
my_circle = Circle (100)

print (my_dog.breed)
print (my_dog.name)
print (my_dog.spots)
print(my_dog.species_class)
my_dog.bark()
my_circle.get_circumference()
my_circle.get_area()

