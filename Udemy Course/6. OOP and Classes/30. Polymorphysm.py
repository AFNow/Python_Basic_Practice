# Полиморфизм - это функция python, которая позволяет использовать одинаково называемые функции в разных классах, без получения ошибок в процессе исполнения кода.
from typing import Any


class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self): # Функция имеет аналогичное название из соседнего класса Cat
        return self.name + ' says woof!'
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self): # Функция имеет аналогичное название из соседнего класса Dog
        return self.name + ' says meow!'
niko = Dog('Niko')
felix = Dog('Felix')
print (niko.speak())
print (felix.speak())
# Примером полиморфизма является использование итерируемого цикла:
for pet in [niko, felix]:
    print (type(pet)) # Как видно из результата запуска, тип успешно определил, к какому классу привязан объект, но метод функции был успешно применен в обоих случаях
    print (type(pet.speak()))
    print (pet.speak())
# Вне контекста примера, у обоих классов могло быть на порядок больше функций, но именно соответствующие обоим могли бы вызываться по одному общему названию функции
    
class Animal(): # Отдельной темой может являться наследование полиморфизма, которое подразумевает вызов ошибки. 
    def __init__(self,name):
        self.name = name
    def speak(self):
        # В данном случае подразумевается, что этот класс будет использоваться для наследования другими классами, а при указании переменной через класс Animal,
        # вне наследуемого класса, будет вызывать ошибку.
        raise NotImplementedError("Subclass mus implement this abstract method")
    # Команда raise предназначена для вызова кастомной ошибки с ручным описанием

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return self.name + ' speaks woof!'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return self.name + ' speaks meow!'
    
sparkie = Dog("Sparkie")
cherry = Cat("Cherry")
print(cherry.speak())
print(sparkie.speak())
